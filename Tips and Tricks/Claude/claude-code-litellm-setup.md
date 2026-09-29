# Claude Code with a LiteLLM Proxy

This guide explains how to configure **Claude Code** to use a **LiteLLM proxy** as its API gateway.

The setup is useful when you want Claude Code requests to go through an organization's LiteLLM server for centralized authentication, routing, logging, budgets, rate limits, or model selection.

---

## Architecture

```text
Claude Code
    |
    | Anthropic-compatible API
    v
LiteLLM Proxy
    |
    | Provider API
    v
Anthropic / OpenAI / Gemini / Other Model Provider
```

Claude Code communicates with LiteLLM using the Anthropic-compatible API. LiteLLM then routes the request to the configured model provider.

---

## Prerequisites

You need:

- Claude Code installed
- A running LiteLLM proxy
- A LiteLLM virtual/API key
- A model configured in LiteLLM
- The LiteLLM proxy URL

Example:

```text
LiteLLM URL:
https://litellm.example.com

LiteLLM API key:
sk-xxxxxxxx

LiteLLM model name:
my-claude
```

The `my-claude` value must correspond to the `model_name` exposed by your LiteLLM configuration.

---

# 1. Configure LiteLLM

A basic LiteLLM configuration might look like:

```yaml
model_list:
  - model_name: my-claude
    litellm_params:
      model: anthropic/claude-sonnet-4-5
      api_key: os.environ/ANTHROPIC_API_KEY
```

In this example:

- `my-claude` is the model name exposed to clients.
- `anthropic/claude-sonnet-4-5` is the underlying provider/model.
- Claude Code does not need to know the underlying provider configuration.

Your organization's LiteLLM configuration may already exist, so you may not need to modify it.

---

# 2. Configure Claude Code

## Windows PowerShell

Set the environment variables:

```powershell
$env:ANTHROPIC_BASE_URL="https://litellm.example.com"
$env:ANTHROPIC_AUTH_TOKEN="sk-xxxxxxxx"
$env:ANTHROPIC_MODEL="my-claude"
```

Then start Claude Code:

```powershell
claude
```

The variables have the following purpose:

| Variable | Purpose |
|---|---|
| `ANTHROPIC_BASE_URL` | LiteLLM proxy URL |
| `ANTHROPIC_AUTH_TOKEN` | LiteLLM virtual/API key |
| `ANTHROPIC_MODEL` | LiteLLM `model_name` |

---

# 3. Important: Use `ANTHROPIC_AUTH_TOKEN`

When using LiteLLM, use:

```powershell
$env:ANTHROPIC_AUTH_TOKEN="sk-xxxxxxxx"
```

rather than configuring the LiteLLM key as:

```powershell
$env:ANTHROPIC_API_KEY="sk-xxxxxxxx"
```

If `ANTHROPIC_API_KEY` is already configured in your environment, it can interfere with the proxy configuration.

Check whether it exists:

```powershell
Get-ChildItem Env:ANTHROPIC*
```

If necessary, remove it from the current PowerShell session:

```powershell
Remove-Item Env:ANTHROPIC_API_KEY -ErrorAction SilentlyContinue
```

Then configure:

```powershell
$env:ANTHROPIC_BASE_URL="https://litellm.example.com"
$env:ANTHROPIC_AUTH_TOKEN="sk-xxxxxxxx"
$env:ANTHROPIC_MODEL="my-claude"
```

---

# 4. Make the Configuration Persistent

The `$env:` commands only apply to the current PowerShell session.

You can configure the variables permanently using Claude Code's settings.

Create or edit:

```text
~/.claude/settings.json
```

Example:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://litellm.example.com",
    "ANTHROPIC_AUTH_TOKEN": "sk-xxxxxxxx",
    "ANTHROPIC_MODEL": "my-claude"
  }
}
```

### Security consideration

Avoid committing this file to Git repositories.

More importantly, avoid storing production API keys in source-controlled files.

For enterprise environments, prefer your organization's approved secret-management mechanism.

---

# 5. Test the LiteLLM Proxy

Before troubleshooting Claude Code, verify that the LiteLLM proxy is reachable.

For example:

```powershell
curl.exe https://litellm.example.com/v1/models `
  -H "Authorization: Bearer sk-xxxxxxxx"
```

A successful response should return the models exposed by the proxy.

If this request fails, troubleshoot LiteLLM/network/authentication before troubleshooting Claude Code.

---

# 6. Start Claude Code

Once the environment variables are configured:

```powershell
claude
```

You can check or change the Claude Code model using:

```text
/model
```

If your Claude Code version supports gateway model discovery, you may also enable:

```powershell
$env:CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY="1"
```

This can allow Claude Code to discover models exposed through the gateway.

---

# 7. Using a Non-Anthropic Model

One of the benefits of LiteLLM is that Claude Code can potentially route through other providers supported by LiteLLM.

For example:

```yaml
model_list:
  - model_name: my-gpt
    litellm_params:
      model: openai/gpt-5
      api_key: os.environ/OPENAI_API_KEY
```

Claude Code can then be configured with:

```powershell
$env:ANTHROPIC_BASE_URL="https://litellm.example.com"
$env:ANTHROPIC_AUTH_TOKEN="sk-xxxxxxxx"
$env:ANTHROPIC_MODEL="my-gpt"
```

The conceptual flow becomes:

```text
Claude Code
     |
     v
LiteLLM
     |
     v
OpenAI GPT
```

Claude Code continues using the Anthropic-compatible interface while LiteLLM handles the provider-side routing.

---

# 8. Recommended Enterprise Configuration

For an enterprise environment, consider keeping provider credentials entirely on the LiteLLM server.

For example:

```yaml
model_list:
  - model_name: claude-primary
    litellm_params:
      model: anthropic/claude-sonnet-4-5
      api_key: os.environ/ANTHROPIC_API_KEY

  - model_name: gpt-primary
    litellm_params:
      model: openai/gpt-5
      api_key: os.environ/OPENAI_API_KEY
```

Claude Code only receives:

```text
LiteLLM URL
+
LiteLLM virtual key
+
Model name
```

This prevents individual developers from needing direct provider API credentials.

A typical enterprise architecture is:

```text
Developer
    |
    v
Claude Code
    |
    | LiteLLM virtual key
    v
Enterprise LiteLLM Proxy
    |
    +---- Authentication
    |
    +---- Authorization
    |
    +---- Model routing
    |
    +---- Rate limits
    |
    +---- Budgets
    |
    +---- Logging / observability
    |
    +---- Guardrails
    |
    +---- Provider API
```

---

# 9. Troubleshooting

## Claude Code is ignoring LiteLLM

Check:

```powershell
Get-ChildItem Env:ANTHROPIC*
```

Make sure:

```text
ANTHROPIC_BASE_URL
ANTHROPIC_AUTH_TOKEN
ANTHROPIC_MODEL
```

are configured correctly.

Also check that an unintended `ANTHROPIC_API_KEY` is not present.

---

## 401 Unauthorized

Check:

1. LiteLLM API key is valid.
2. The key is authorized to access the configured model.
3. The proxy URL is correct.
4. The Authorization header is accepted by your LiteLLM deployment.

Test independently:

```powershell
curl.exe https://litellm.example.com/v1/models `
  -H "Authorization: Bearer sk-xxxxxxxx"
```

---

## 404 Not Found

Check the proxy URL.

The base URL should point to the LiteLLM server/API endpoint expected by Claude Code.

For example:

```text
https://litellm.example.com
```

rather than accidentally using an unrelated application URL.

---

## Model Not Found

Verify the LiteLLM `model_name`.

For example:

```yaml
model_list:
  - model_name: my-claude
```

Then use:

```powershell
$env:ANTHROPIC_MODEL="my-claude"
```

The value must match the exposed LiteLLM model name.

---

## Streaming or tool-calling problems

Claude Code relies on API functionality beyond a simple text completion.

If basic requests work but Claude Code fails during tool use, streaming, or extended interactions, verify that your LiteLLM version and deployment correctly support the Anthropic-compatible endpoint and the features Claude Code requires.

---

# 10. Quick Setup

For a temporary PowerShell session:

```powershell
$env:ANTHROPIC_BASE_URL="https://litellm.example.com"
$env:ANTHROPIC_AUTH_TOKEN="sk-xxxxxxxx"
$env:ANTHROPIC_MODEL="my-claude"

claude
```

That's the minimum configuration.

---

# 11. Example Complete Setup

Assume:

```text
LiteLLM:
https://ai.company.com

Virtual Key:
sk-company-123456

Model:
claude-code
```

Run:

```powershell
$env:ANTHROPIC_BASE_URL="https://ai.company.com"
$env:ANTHROPIC_AUTH_TOKEN="sk-company-123456"
$env:ANTHROPIC_MODEL="claude-code"

claude
```

The resulting request path is conceptually:

```text
Claude Code
    |
    | ANTHROPIC_AUTH_TOKEN
    | ANTHROPIC_MODEL=claude-code
    v
https://ai.company.com
    |
    v
LiteLLM
    |
    v
Configured underlying model
```

---

# 12. Recommended `.env` Pattern for Development

If you need environment-specific configuration, keep secrets outside source control.

Example:

```text
ANTHROPIC_BASE_URL=https://litellm.example.com
ANTHROPIC_AUTH_TOKEN=sk-xxxxxxxx
ANTHROPIC_MODEL=my-claude
```

Add the environment file to `.gitignore`:

```gitignore
.env
.env.*
!.env.example
```

You can provide a non-secret example:

```text
ANTHROPIC_BASE_URL=https://your-litellm-server.example.com
ANTHROPIC_AUTH_TOKEN=your-litellm-key
ANTHROPIC_MODEL=your-model-name
```

Never commit a real API key.

---

# 13. Security Recommendations

For an organization using Claude Code through LiteLLM:

- Use separate LiteLLM keys for users, teams, or applications where appropriate.
- Apply per-key or per-team budgets.
- Restrict which models each key can access.
- Keep provider API keys on the LiteLLM server.
- Enable appropriate audit logging.
- Avoid logging sensitive prompts or responses unless required and properly protected.
- Use TLS/HTTPS for the proxy.
- Rotate LiteLLM keys periodically.
- Never commit API keys to Git.
- Use your organization's approved secret-management solution.
- Review data-retention and provider-routing policies before sending sensitive enterprise information through the proxy.
- If handling regulated or sensitive data, verify the organization's approved models, providers, and data-processing agreements.

---

# Quick Reference

```text
Claude Code environment variables
----------------------------------

ANTHROPIC_BASE_URL
    = LiteLLM proxy URL

ANTHROPIC_AUTH_TOKEN
    = LiteLLM virtual/API key

ANTHROPIC_MODEL
    = LiteLLM model_name
```

Minimal PowerShell configuration:

```powershell
$env:ANTHROPIC_BASE_URL="https://litellm.example.com"
$env:ANTHROPIC_AUTH_TOKEN="sk-xxxxxxxx"
$env:ANTHROPIC_MODEL="my-claude"

claude
```

---

## References

- LiteLLM Claude Code integration:
  https://docs.litellm.ai/docs/proxy/client_setup/claude_code

- LiteLLM documentation:
  https://docs.litellm.ai/

- Claude Code documentation:
  https://docs.anthropic.com/en/docs/claude-code

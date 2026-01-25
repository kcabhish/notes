# Open AI Agents SDK Fundamentals

## Minimal Terminology

- Agents represent LLMs.
- Handoffs represent interactions. (Interaction between Agents, Transfer of controls between two agents normally happen after 1 agent complets a task)
- Guardrails represents control. (Checks and controls to make sure agent is not going off track)

## Three Steps

- Create an instance of Agent.
- Use with trace() to track the agent. (Keep a log of interaction with LLM)
- Call runner.run() to run the agent.

## OpenAI Hosted Tools

- WebSearchTool lets an agent search the web.
- FileSearchTool allows retrieving information from your OpenAI Vector Stores.
- ComputerTool allows automating computer use tasks like taking screenshot and clicking.

## Vibe Coding Tips

- Good Vibes: propmt well - ask for short answers and latest APIs for today's date.
- Vibe but verify - ask 2 llms the same question.
- Step up the vibe - ask to break down your request into independently testable steps.
- Vibe and Validate - ask an LLM thn get another LLM to check
- Vibe with Variety - ask for 3 solutions to the same problem, pick the best.
# Running Ollama locally

# LLM APIs and Ollama - beyond OpenAI

_IMPORTANT: If you're not as familiar with APIs in general, and with Environment Variables on your PC or Mac, please review the APIs section in Guide 4 Technical Foundations before proceeding with this guide (topics 3 and 5 in Guide 4)._

## Crucial context for using models other than OpenAI - please read this first!

Throughout the course, we use APIs for connecting with the strongest LLMs on the planet.

The companies behind these LLMs, such as OpenAI, Anthropic, Google and DeepSeek, have built web endpoints. You call their models by making an HTTP request to a Web Address and passing in all the information about your prompts.

But it would be painful if we needed to build HTTP requests every time we wanted to call an API.

To make this simple, the team at OpenAI wrote a python utility known as a "Python Client Library" which wraps the HTTP call. So you write python code and it calls the web.

And THAT is what the library `openai` is.

### What is the `openai` python client library

It is:
- A lightweight python utility
- Turns your python requests into an HTTP call
- Converts the results coming back from the HTTP call into python objects

### What it is NOT

- It's not got any code to actually run a Large Language Model! No GPT code! It just makes a web request
- There's no scientific computing code, and nothing particularly specialized for OpenAI

### How to use it:

```python
# Create an OpenAI python client for making web calls to OpenAI
openai = OpenAI()

# Make the call
response = openai.chat.completions.create(model="gpt-4.1-mini", messages=[{"role":"user", "content": "what is 2+2?"}])

# Print the result
print(response.choices[0].message.content)
```

### What does this do

When you make the python call: `openai.chat.completions.create()`  
It simply makes a web request to this url: `https://api.openai.com/v1/chat/completions`  
And it converts the response to python objects.

That's it.

Here's the API documentation if you make [direct web HTTP calls](https://platform.openai.com/docs/guides/text?api-mode=chat&lang=curl)  
And here's the same API documentation if you use the [Python Client Library](https://platform.openai.com/docs/guides/text?api-mode=chat&lang=python)

## With that context - how do I use other LLMs?

It turns out - it's super easy!

All the other major LLMs have API endpoints that are compatible with OpenAI.

And so OpenAI did everyone a favor: they said, hey look - you can all use our utility for converting python to web requests. We'll allow you to change the utility from calling `https://api.openai/com/v1` to calling any web address that you specify.

And so you can use the OpenAI utility even for calling models that are NOT OpenAI, like this:

`not_actually_openai = OpenAI(base_url="https://somewhere.completely.different/", api_key="another_providers_key")`

It's important to appreciate that this OpenAI code is just a utility for making HTTP calls to endpoints. So even though we're using code from the OpenAI team, we can use it to call models other than OpenAI.

Here are all the OpenAI-compatible endpoints from the major providers. It even includes using Ollama, locally. Ollama provides an endpoint on your local machine, and they made it OpenAI compatible too - very convenient.

```python
ANTHROPIC_BASE_URL = "https://api.anthropic.com/v1/"
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
GROK_BASE_URL = "https://api.x.ai/v1"
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OLLAMA_BASE_URL = "http://localhost:11434/v1"
```

## Here are examples for Gemini, DeepSeek, Ollama and OpenRouter

### Example 1: Using Gemini instead of OpenAI

1. Visit Google Studio to set up an account: https://aistudio.google.com/  
2. Add your key as GOOGLE_API_KEY to your `.env`  
3. Also add it a second time as GEMINI_API_KEY to your `.env` - this will be helpful later.

Then:

```python
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.getenv("GOOGLE_API_KEY")
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
response = gemini.chat.completions.create(model="gemini-2.5-flash-preview-05-20", messages=[{"role":"user", "content": "what is 2+2?"}])
print(response.choices[0].message.content)
```

### Example 2: Using DeepSeek API instead of OpenAI (cheap, and only $2 upfront)

1. Visit DeepSeek API to set up an account: https://platform.deepseek.com/  
2. You will need to add an initial $2 minimum balance.  
3. Add your key as DEEPSEEK_API_KEY to your `.env`  

Then:

```python
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
deepseek = OpenAI(base_url=DEEPSEEK_BASE_URL, api_key=deepseek_api_key)
response = deepseek.chat.completions.create(model="deepseek-chat", messages=[{"role":"user", "content": "what is 2+2?"}])
print(response.choices[0].message.content)
```

### Example 3: Using Ollama to be free and local instead of OpenAI

Ollama allows you to run models locally; it provides an OpenAI compatible API on your machine.  
There's no API key for Ollama; there's no third party with your credit card, so no need for any kind of key.

1. If you're new to Ollama, install it by following the instructions here: https://ollama.com   
2. Then in a Cursor Terminal, do `ollama run llama3.2` to chat with Llama 3.2  
BEWARE: do not use llama3.3 or llama4 - these are massive models not designed for home computing! They will fill up your disk.  

Then:

```python
!ollama pull llama3.2

from openai import OpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="anything")
response = ollama.chat.completions.create(model="llama3.2", messages=[{"role":"user", "content": "what is 2+2?"}])
print(response.choices[0].message.content)
```

### Example 4: Using the popular service [OpenRouter](https://openrouter.ai) which has an easier billing process instead of OpenAI

OpenRouter is very convenient: it gives you free access to many models, and easy access with small upfront to paid models.

1. Sign up at https://openrouter.ai
2. Add the minimum upfront balance as needed
3. Add your key as OPENROUTER_API_KEY to your `.env` file

Then:

```python
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openrouter = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=openrouter_api_key)
response = openrouter.chat.completions.create(model="openai/gpt-4.1-nano", messages=[{"role":"user", "content": "what is 2+2?"}])
print(response.choices[0].message.content)
```


### Using different API providers with Agent Frameworks

The Agent Frameworks make it easy to switch between these providers. You can switch LLMs and pick different ones at any point in the course. There are more notes below on each of them. For OpenAI Agents SDK, see a section later in this notebook. For CrewAI, we cover it on the course, but it's easy: just use the full path to the model that LiteLLM expects.

### Ollama: Free alternative to Paid APIs (but please see Warning about llama version)

Ollama is a product that runs locally on your machine. It can run open-source models, and it provides an API endpoint on your computer that is compatible with OpenAI.

First, download Ollama by visiting:
https://ollama.com

Then from your Terminal in Cursor (View menu >> Terminal), run this command to download a model:

```shell
ollama pull llama3.2
```

WARNING: Be careful not to use llama3.3 or llama4 - these are much larger models that are not suitable for home computers.

And now, any time that we have code like:  
`openai = OpenAI()`  
You can use this as a direct replacement:  
`openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')`  
And also replace model names like **gpt-4o-mini** with **llama3.2**.  

You don't need to put anything in your .env file for this; with Ollama, everything is running on your computer. You're not calling out to a third party on the cloud, nobody has your credit card details, so there's no need for a secret key! The code `api_key='ollama'` above is only required because the OpenAI client library expects an api_key to be passed in, but the value is ignored by Ollama.

Below is a full example:

```python
# You need to do this one time on your computer
!ollama pull llama3.2

from openai import OpenAI
MODEL = "llama3.2"
openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

response = openai.chat.completions.create(
 model=MODEL,
 messages=[{"role": "user", "content": "What is 2 + 2?"}]
)

print(response.choices[0].message.content)
```

You will need to make similar changes to use Ollama within any of the Agent Frameworks - you should be able to google for an exact example, or ask me.
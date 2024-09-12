import openai
import os
from promptflow.tracing import start_trace

start_trace()

# set an environment variable nameed OPENAI_API_KEY
os.environ['OPENAI_API_KEY'] = '9024cc8471da4d09a01706e6a6d73c54'

client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

completion = client.chat.completions.create(
    model="gpt-3.0-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are you?"},
    ]
)

print(completion.choices[0].message['content'])



# Step 0 - Load .env
from dotenv import load_dotenv
load_dotenv()

# Step 1 - Setup GROQ API key
import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Step 2 - Convert image to required format
import base64

image_path = "Acneimage.jpg"
image_file = open(image_path, "rb")
encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Step 3 - Setup Multimodal LLM
from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Is there anything wrong with my face?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url":f"data:image/jpeg;base64,{encoded_image}",
            }
          }
        ]
      },
    ],
    temperature=1.5,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")


import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.Client(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="The food was delicious and the service was excellent."
)

print(response.data[0].embedding)
from config import client, MODEL_NAME

response = client.models.generate_content(
    model=MODEL_NAME,
    contents="Say hello in one sentence."
)

print(response.text)
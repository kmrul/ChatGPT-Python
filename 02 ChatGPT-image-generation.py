import openai


openai.api_key = "<openai API keys>"

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print("Image URL:", image_url)
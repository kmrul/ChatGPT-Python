import openai


openai.api_key = "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"

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print("Image URL:", image_url)
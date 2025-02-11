from google import genai


client = genai.Client(api_key='AIzaSyDjwAGs-HHIN28BdG_OToGPptzx8CiIaRI')

response = client.models.generate_content(
    model='gemini-2.0-flash', contents='How does RLHF work?'
)
print(response.text)
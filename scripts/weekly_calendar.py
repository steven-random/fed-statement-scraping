from google import genai
import requests
import datetime


#url = "https://r.jina.ai/https://tradingeconomics.com/calendar"
url = 'https://r.jina.ai/https://www.forex.com/en-us/trading-tools/economic-calendar/'

try:
    response = requests.get(url)
    html_content = response.text

except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")

client = genai.Client(api_key='AIzaSyDjwAGs-HHIN28BdG_OToGPptzx8CiIaRI')

today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

content = f"Given the following data, summary this week's US economic calendar. Only use the above information. Only output the economic calendar, ignore bills and bonds. Only output US events. Do not output next week's event. Only output the most important events. Output in ET. Add a summary of key events at the end. Also put the analysis from the text at the end." + html_content

response = client.models.generate_content(
    model='gemini-2.0-flash', contents=content
)
print(response.text)

import requests
import json
import pandas as pd

class DiscordNotifier:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_dataframe(self, df, message="", filename="dataframe.csv"):
        """Sends a Pandas DataFrame to a Discord webhook as a file attachment."""
        try:
            csv_string = df.to_csv(index=False)
            files = {
                'file': (filename, csv_string.encode('utf-8'), 'text/csv')
            }
            data = {'content': message}
            response = requests.post(self.webhook_url, files=files, data=data)
            response.raise_for_status()
            print("DataFrame sent to Discord successfully!")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error sending DataFrame to Discord: {e}")
            try:
                error_data = response.json()
                print(f"Discord API Error Data: {error_data}")
            except (json.JSONDecodeError, AttributeError):
                print("Could not decode JSON error response from Discord or no response received.")
            return False


    def send_notification(self, message, embed=None):
        max_length = 2000
        messages = []

        for i in range(0, len(message), max_length):
            messages.append(message[i:i + max_length])

        for msg_part in messages:  # Send each part individually
            payload = {"content": msg_part}
            if embed and messages.index(msg_part) == 0:  # send embed only in the first message.
                payload["embeds"] = [embed]
            headers = {'Content-Type': 'application/json'}
            try:
                response = requests.post(self.webhook_url, data=json.dumps(payload), headers=headers)
                response.raise_for_status()
                print("Discord notification part sent successfully!")
            except requests.exceptions.RequestException as e:
                print(f"Error sending Discord notification part: {e}")
                if response.status_code != 204:
                    try:
                        error_data = response.json()
                        print(f"Discord API Error Data: {error_data}")
                    except json.JSONDecodeError:
                        print("Could not decode JSON error response from Discord.")
                return False
        return True


if __name__ == '__main__':
    # Example usage (replace with your actual webhook URL):
    webhook_url = "YOUR_DISCORD_WEBHOOK_URL"  # **REPLACE THIS WITH YOUR WEBHOOK URL**
    notifier = DiscordNotifier(webhook_url)  # Create an instance of the class
    message = "Hello, this is a test notification from my Python script!"

    # Example with an embed:
    my_embed = {
        "title": "Python Notification",
        "description": "This is an example embed sent from Python.",
        "color": 16751104,  # Example color (light orange)
        "fields": [
            {"name": "Field 1", "value": "Some Value"},
            {"name": "Field 2", "value": "Another Value", "inline": True}
        ]
    }

    # notifier.send_notification(message, my_embed)  # Use the instance to call methods

    df = pd.read_csv('../scripts/communications.csv') # Make sure this file exists in the same directory or provide full path
    df = df.iloc[:5]
    notifier.send_dataframe(df) # Use the instance to call methods
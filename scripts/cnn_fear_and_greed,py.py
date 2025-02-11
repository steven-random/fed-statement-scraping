import fear_and_greed
from backend.push_to_discord import DiscordNotifier
import datetime

if __name__ == '__main__':
    this_fear_and_greed = fear_and_greed.get()
    if this_fear_and_greed is not None:  # Check if it's not None
        this_value = this_fear_and_greed[0]
        this_description = this_fear_and_greed[1]

    webhook_url = 'https://discord.com/api/webhooks/1338593669195890738/VhJKQc2tOUuWgfXtxzYNqhu80vEZ29Iyr1Y6tZhsYAbMKg1YOfep4ytV7AVoG4wV3i_w'

    notifier = DiscordNotifier(webhook_url)

    text = (f"Date: {datetime.date.today()} \n CNN fear_and_greed is {this_value} \n Description is {this_description} \n"
            f"Update at {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")

    notifier.send_notification(text)

print(fear_and_greed.get())
import requests, time
from discord_webhook import DiscordWebhook

chuck = "https://api.chucknorris.io/jokes/random"
webhook_url = "URL"
# webhook_url = ['url', 'url2']

wait_time = int(input('Time interval between each joke (in seconds): '))
number_of_jokes = input('How many jokes you want to send? (number or "i" for infinity): ')

def sendjoke():
        webhook = DiscordWebhook(url=webhook_url, content=requests.get(chuck).json()["value"]).execute()
        time.sleep(wait_time)

if number_of_jokes == "i":
    while 1:
        sendjoke()
else:
    for i in range(int(number_of_jokes)):
        sendjoke()
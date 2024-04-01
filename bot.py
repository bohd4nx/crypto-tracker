import requests
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')
bot_token = config['Telegram']['bot_token']
chat_id = config['Telegram']['chat_id']
new_message = config.getboolean('Settings', 'new_message')


def send_message(message, message_id=None):
    if message_id is None:
        return send_new_message(message)
    else:
        return edit_message(message, message_id)


def send_new_message(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': message}
    response = requests.post(url, data=payload)
    return response.json()['result']['message_id']


def edit_message(message, message_id):
    url = f"https://api.telegram.org/bot{bot_token}/editMessageText"
    payload = {'chat_id': chat_id, 'message_id': message_id, 'text': message}
    response = requests.post(url, data=payload)
    return message_id

import configparser
import datetime
import requests

def confINFO(filename: str):
	""""""
	config = configparser.ConfigParser()
	config.read(filename)

	return config

def telegram_bot_send_text(info, msg: str):
	""""""
	token = info.get('TELEGRAM_chat_info', 'token')
	chatID = info.get('TELEGRAM_chat_info', 'chatID')

	sendText = f'https://api.telegram.org/bot{token}sendMessage?chat_id={chatID}&parse_mode=Markdown&text={msg}'
	response = requests.get(sendText)

	return response.json()

if __name__ == '__main__':
	auth = confINGO('alerts.conf')
	message = 'test message'
	telegram_bot_send_text(auth, message)

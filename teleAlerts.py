import configparser
from datetime import datetime
import requests

def confINFO(filename: str):
	"""Function for creating ConfigParser object holding Telegram Bot information.\n
	filename (required) ---> str | name with file extension : <filename>.conf"""
	config = configparser.ConfigParser()
	config.read(filename)

	return config

def telegram_bot_send_text(info, msg: str):
	"""Function for sending GET request to Telegram Bot API.\n
	info (required) ---> ConfigParser object\n
	msg (required) ---> str | message to be sent"""
	tk = info.get('TELEGRAM_chat_info', 'token')
	cid = info.get('TELEGRAM_chat_info', 'chatID')

	txt = f"https://api.telegram.org/bot{tk}/sendMessage?chat_id={cid}&parse_mode=Markdown&text={msg}"
	response = requests.get(txt)

	return response.json()

if __name__ == "__main__":
	auth = confINFO("alerts.conf")  # path to file
	message = input().strip("\t\v\r\b")
	header = f"*/>_* _{datetime.now()}_\n"

	if bool(message) is True:
		telegram_bot_send_text(auth, header+message)

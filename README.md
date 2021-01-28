# teleAlerts

Simple python program that sends a message for a Telegram bot.

An example of implementation would be to check a running program and send alerts when it encounters an error.


## Usage
Small sample for the creation of a .conf file to store Telegram's bot token and chat id. If you're using it on a production enviroment (or anything more serious than a personal project for that matter) I strongly sugest using other forms for storing those values. Or at the very least, storing criptographed values and implementing an interface for changing them if needed.

```python
import os
import configparser

config = configparser.RawConfigParser()
filename = 'alerts'

config['TELEGRAM_chat_info'] = {
	'token': '##########',
	'chatID': '**********'
}

with open(os.path.join(os.getcwd(), (filename + '.conf')), 'w') as configfile:
	config.write(configfile)

configfile.close()
```

If you want to use it to check output of a program in Linux, you should be able to redirect the output of the program (or another shell script that executes that program) to the input of teleAlerts.py. As an example:

```python
# function declarations are here (at least one would imagine they are) #

if __name__ == '__main__':
	auth = confINFO('mychat.conf')
	message = input()
	telegram_bot_send_text(auth, message)
```

```bash
#!/bin/bash

myrunningcommand | python teleAlerts.py
# remember that myrunningcommand has to have an output, otherwise the input of teleAlerts.py will be empty
```

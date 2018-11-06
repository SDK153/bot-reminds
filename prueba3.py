import telebot
import time
bot =telebot.TeleBot("732224348:AAEBv0jKGwwjWG10NT-yPLo8Fpsl5sOJYB4")
medicina=time.strftime("16:50:00")
medicina2=time.strftime("07:40:00")
hora=time.strftime("%X")
timer=0
inicio=False
def horas():
	global timer,corre
	chatid2=753932841
	bot.send_message(chatid2,"Recordatorio, toma tus medicamentos")
	bot.send_message(chatid2,"Feliz Dia")
	timer=0
while True:
	hora=time.strftime("%X")
	timer=timer+1
	time.sleep(1)
	print inicio
	print ("cronometro "+str(timer))
	print ("tiempo "+str(hora))
	if hora==medicina or hora==medicina2:
		horas()




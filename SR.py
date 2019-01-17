import speech_recognition as sr 

while True:
	x = input('Start program? y/n : ')
	if x == "n":
		break
	if x == "y":
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print('Say something : ')
			audio = r.listen(source)
			try:
				text = r.recognize_google(audio)
				print('You said : {}'.format(text))
			except:
				print('Sorry could not recognize your voice')







				





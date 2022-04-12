#import library
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
from os import path
from pydub import AudioSegment
from playsound import playsound
import os
import subprocess

#blank entry of what is said
Spoken = ""


def Banner():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("  ______     ")     
	print(" |  ____|      ")   
	print(" | |____   ____ _ ")
	print(" |  __\ \ / / _` |")
	print(" | |___\ V / (_| |")
	print(" |______\_/ \__,_|")
                  
                  
	return


def record(x):
	global Spoken
	fs = 44100  # Sample rate
	seconds = x  # Duration of recording
	print("Listening... for " + str(x) + " seconds")
	myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
	sd.wait()  # Wait until recording is finished
	write('Recording.wav', fs, myrecording)  # Save as WAV file 
	print("Done Listening")

	# files                                                                         
	src = "Recording.wav"
	dst = "output.wav"

	# convert wav to mp3                                                            
	sound = AudioSegment.from_wav(src)
	sound.export(dst, format="wav")	
	
	#conver to text
	# Initialize recognizer class (for recognizing the speech)
	r = sr.Recognizer()

	# Reading Audio file as source
	# listening the audio file and store in audio_text variable
	#File= raw_input("Enter file name: ")
	with sr.AudioFile('output.wav') as source:
    
		audio_text = r.listen(source)
		try:
 	       # using google speech recognition
			text = r.recognize_google(audio_text)
			print('Converting audio transcripts into text ...')
			print("Text: " +text)
			Spoken = text
			return
		except:
			print('No voice heard')
			Spoken = ""
			pass
	return

def play():
	global success
	playsound('hello.mp3')
	success = True
	return

def eva():
	#call global spoken to read last text
	#Banner()
	os.system("gtts-cli 'Hello my love, what can I help you with today?' --output hello.mp3")
	playsound('hello.mp3')
	record(5)
	global Spoken
	global success
	#reset success
	success = False
	#succes token lets us know to trigger the msunderstood speech

	try:
		if Spoken.find("weather") != -1:
				cmd = 'curl wttr.in/Raleigh?format="%C+%t"'
				IP = subprocess.check_output(cmd, shell = True )
				print(IP)
				os.system("gtts-cli 'The weather is " + IP + "' --output hello.mp3")
				play()
		if Spoken.find("time") != -1 or Spoken.find("date")!= -1:
				cmd = 'date'
				IP = subprocess.check_output(cmd, shell = True )
				print(IP)
				os.system("gtts-cli 'Today is " + IP + "' --output hello.mp3")
				play()
		if Spoken.find("tits") != -1:
				os.system("gtts-cli 'want to suck my tittes?' --output hello.mp3")
				play()
		if Spoken.find("look up") != -1 or Spoken.find("find") != -1 or Spoken.find("wikipedia") != -1:
				os.system("gtts-cli 'What word would you like to look up?' --output hello.mp3")
				play()
				record(4)
				#wiki the word
				cmd = "wikit "  +Spoken 
				IP = subprocess.check_output(cmd, shell = True )
				os.system("gtts-cli '" +IP+"' --output hello.mp3")
				play()
				
		#sets the success token to true
		
		if success == False:
			print("launching bot.py")
			#send text to the chatbot
			os.system("python3 bot.py '" + str(Spoken)+ "'")
			#read chatbot output
			file = open("response.txt", "r").read().replace("\n", " ")
			f = open("response.txt", "r")
			response = (f.read()) 
			print("response.txt contents: " +response)
			os.system("gtts-cli '" + response +"' --output hello.mp3")
			play()
		# asks for any more commands
			
    #if no voice is heard return to the main loop 
	except:

		print('something has gone wrong in Eva')
		pass
	os.system("gtts-cli 'Anything else my love?' --output hello.mp3")
	playsound('hello.mp3')
	record(4)
	try:
		if Spoken.find("yes") != -1:
			eva()
		else:
			return
	except:
		pass
	
	
	return




def idle():
	#Banner()
	record(3)
	global Spoken
	print("Idle")
	if Spoken.find("Eva") != -1:
			#launch eva
		eva()
	else:
		idle()
	idle()
idle()
			
			
			
			

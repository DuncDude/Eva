#import library
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
from os import path
from pydub import AudioSegment
from playsound import playsound
import os
import subprocess
import re
from random import randrange
#from gtts import gTTS
#blank entry of what is said
Spoken = ""

#debug mode
debug = "off"

#speech accent
act = "en"

#intros
intros = ["Hello my love what do you need",
		  "What a day huh? what do you need",
		  "How can I help you now?",
		  "Something I can Help you with?",
		  "Looking good love, What do you need?",
		  "Woof, what a life, you look like you need something, what do you need?",
		  "Wow what a forward young man, what can I do you for?"]

#Banner NOTE: comment out the clr screen for debugging
def BannerClear():
	global debug
	if debug== "off":
		os.system('cls' if os.name == 'nt' else 'clear')
	return
def Banner():
	BannerClear()
	#os.system('cls' if os.name == 'nt' else 'clear')
	print("  ______     ")
	print(" |  ____|      ")
	print(" | |____   ____ _ ")
	print(" |  __\ \ / / _` |")
	print(" | |___\ V / (_| |")
	print(" |______\_/ \__,_|")


	return

#sanizes strings for the bot to read
def san(x):
	x = re.sub(r'[^A-Za-z0-9 ]+', '',x)
	#x = (string.lower(x))
	print("Sanitized Text: "+ str(x))
	return x

#makes a file "hello.mp3" with the passed text and plays it
def Voice(y):
	accent = str(act)
	print("Choice of accent: " + accent)
	words = str(y)
	print("passed words: " + words)
	command = ("gtts-cli '"+ words +"' --lang " + accent + " --output hello.mp3")
	os.system(command)
	play()
	return

#records audio with x passed being the amount in seconds to listen
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
			Spoken = (text)
			#remove all upper cases
			Spoken = Spoken.lower()
			#sanitize data of symbols
			Spoken = san(Spoken)
			return
		except:
			print('No voice heard')
			Spoken = ""
			pass
	return
#plays the audio file hello.mp3
def play():
	global success
	playsound('hello.mp3')
	success = True
	return


#translates words into other languages
def accent():
	global Spoken
	global act
	Voice('To what language would you like to change my accent?')
	record(3)
	#take the first two letters of the last recordig
	act = Spoken[0:2]
	return
#Run the chatbot to answer on trained commands
def bot():
	exit()

def terminal():
	global Spoken
	Voice('What would you like to add to the terminal?')
	record(4)
	os.system(Spoken)
	return

def eva():
	#call global spoken to read last text
	Banner()
	global debug
	#open intro from array, rqandom choice made from the 0-length of array
	intro = intros[randrange(len(intros))]
	print("Greeting: " +intro)
	Voice(intro)
	record(6)
	global Spoken
	global success
	#reset success
	success = False
	#succes token lets us know to trigger the msunderstood speech

	try:
		if Spoken.find("weather") != -1:
				cmd = 'curl wttr.in/Raleigh?format="%C+%t+%s"'
				IP = subprocess.check_output(cmd, shell = True )

				print(IP)
				Voice('The weather is ' + IP)
		if Spoken.find("time") != -1 or Spoken.find("date")!= -1 or Spoken.find("calendar")!= -1:
				cmd = 'date'
				IP = subprocess.check_output(cmd, shell = True )
				print(IP)
				cmd2 = 'cal'
				IP2 = subprocess.check_output(cmd2, shell = True )
				print(IP2)
				Voice('Today is ' + IP)
		if Spoken.find("tits") != -1:
				Voice('want to suck my tittes?')
		if Spoken.find("accent") != -1:
				accent()
		if Spoken.find("linux") != -1 or Spoken.find("terminal")!= -1:
				terminal()
#pull up new web window with google search
		if Spoken.find("google") != -1 or Spoken.find("search")!= -1:
			Voice('What would you like to google?')
			record(6)
			os.system("firefox --search '" + Spoken + "'" )
#pull up new web window with website
		if Spoken.find("navigate") != -1 or Spoken.find("go to")!= -1 or Spoken.find("website")!= -1:
			Voice('What website would you like to open?')
			record(6)
			os.system("firefox --newtab '" + Spoken + "'" )
#wiki look up using wikit
		if Spoken.find("look up") != -1 or Spoken.find("find") != -1 or Spoken.find("wikipedia") != -1 or Spoken.find("look up") != -1 or Spoken.find("look something up") != -1:
				Voice('What word would you like to look up?')
				record(4)
				#wiki the word
				print("Looking up: " + Spoken)
				cmd = "wikit "  +Spoken
				IP = subprocess.check_output(cmd, shell = True )
				#sanitize data
				IP = san(IP)
				Voice(IP)
#adjust computer volume
		if Spoken.find("volume") != -1:
			Voice('What Percent?')
			record(3)
			os.system("amixer -D pulse sset Master " + Spoken + "%" )
#voice to text file

#Enable debug mode to prevent screen clears
		if Spoken.find("debug mode on") != -1:
			debug = "on"
			Voice('Debug On')
#Disable debug mode to allow screen clears
		if Spoken.find("debug mode off") != -1:
			debug = "off"
			Voice('Debug Off')





		#sets the success token to true and launches the chat bot with the phrase with no key words into it
		if success == False:
			print("launching bot.py")
			#send text to the chatbot
			os.system("python3 bot.py '" + str(Spoken)+ ".'")
			#read chatbot output
			file = open("response.txt", "r").read().replace("\n", " ")
			f = open("response.txt", "r")
			response = (f.read())
			response = san(response)
			print("response.txt contents: " +response)
			Voice(response)
		# asks for any more commands

    #if no voice is heard return to the main loop
	except:

		print('something has gone wrong in Eva')
		pass
	Voice('Anything else my love?')
	record(4)
	try:
		if Spoken.find("yes") != -1 or Spoken.find("yeah") != -1:
			eva()
		else:
			return
	except:
		pass


	return




def idle():
	Banner()
	record(4)
	global Spoken
	print("Idle")
	#print(str(Spoken))
	if Spoken.find("eva") != -1:
			#launch eva
		eva()
	if Spoken.find("restart") != -1 or Spoken.find("reboot") != -1:
		print("Restarting...")
		Voice('Restarting')
		exit()
	if Spoken.find("exit") != -1:
		print("Restarting...")
		Voice('exiting')
		os.system("killall -9 python")
		exit()
	else:
		idle()
#Voice('Restart Complete or Error')

idle()

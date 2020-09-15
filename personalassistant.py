import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty("voice",voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Hi!Good Morning!")
	elif hour>=12 and hour<18:
		speak("Hi!Good Afternoon!")  
	else:
		speak("Hi!Good Evening!")
	speak("I am Jenna, your personal assistant!")  
	
def helpMe():
	print()
	speak("I can help you with the following things ->")
	print("I can launch Google Chrome for you")
	print("I can search any content from Wikipedia")
	print("I can launch Facebook for you")
	print("I can launch Notepad for you")
	print("I can launch Youtube for you")
	print("I can launch Gmail for you")
	print("I can launch Flipkart for you")
	print("I can launch Yahoo for you")
	print("I can launch Amazon for you")
	print("I can launch Stack Overflow for you")
	print("I can launch LinkedIn for you")
	print("I can launch VLC Media Player for you")
	print("I can launch Windows Media Player for you")
	print("I can launch MySQL Workbench for you")
	print("I can launch Mozilla Firefox browser for you")
	print("I can launch Command Prompt for you")
	print("I can launch Visual Studio Code for you")
	print()
	speak(" What you want me to do?")

def takeCommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("I am listening . . .")
		r.pause_threshold = 1
		audio = r.listen(source)
		print("I got it. Please wait . . .")
	query = r.recognize_google(audio,language="en-in")
	print(f"User said -> {query}\n")    
	return query


if __name__ == "__main__":
	print("************************************************************************************************************************************************************************")
	print()
	print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * J E N N A * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *") 
	print()
	print("************************************************************************************************************************************************************************")
	wishMe()
	helpMe()
	while True:
		query = takeCommand().lower()

		if "wikipedia" in query:
			speak("Searching wikipedia....")
			query = query.replace("wikipedia","")
			results = wikipedia.summary(query,sentences=2)
			speak("According to wikipedia")
			#print(results)
			speak(results)
			speak("What else you want me to do")
		
		elif "notepad" in query:
			speak("opening notepad for you")
			os.startfile("C:\\WINDOWS\\system32\\notepad.exe")   
			speak("What else you want me to do") 

		elif "youtube" in query:
			speak("opening youtube for you")
			webbrowser.open("https://www.youtube.com/")
			speak("What else you want me to do")
		
		elif "google" in query:   
			speak("opening google chrome for you")
			os.system("chrome")
			speak("What else you want me to do") 
	
		elif "gmail" in query:
			speak("opening gmail for you")
			webbrowser.open("https://www.gmail.com/")
			speak("What else you want me to do")

		elif "flipkart" in query:
			speak("opening flipkart for you")
			webbrowser.open("https://www.flipkart.com/")
			speak("What else you want me to do")
		
		elif "facebook" in query:
			speak("opening facebook for you")
			webbrowser.open("https://www.facebook.com/")
			speak("What else you want me to do")
	
		elif "yahoo" in query:
			speak("opening yahoo for you")
			webbrowser.open("https://www.yahoo.com/")
			speak("What else you want me to do")
			
		elif "amazon" in query:
			speak("opening amazon for you")
			webbrowser.open("https://www.amazon.com/")
			speak("What else you want me to do")

		elif "stack" in query:
			speak("opening stack overflow for you")
			webbrowser.open("https://stackoverflow.com/")  
			speak("What else you want me to do")

		elif "linkedin" in query:
			speak("opening linkedin for you")
			webbrowser.open("https://www.linkedin.com/feed/")    
			speak("What else you want me to do")  

		elif "vlc" in query:
			speak("opening vlc media player for you")
			os.system("vlc") 
			speak("What else you want me to do")

		elif "windows" in query and "media" in query and "player" in query:
			speak("opening windows media player for you")
			os.system("wmplayer") 
			speak("What else you want me to do")

		#elif "anaconda" in query:
			#speak("opening anaconda for you")
			#os.system("anaconda-navigator-script")
			#os.startfile("C:\\Users\\User\\anaconda3\\_conda.exe")
		
		elif "time" in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")    
			speak(f"The Time is {strTime}")
			speak("What else you want me to do")
	
		elif "mysql" in query or "workbench" in query:
			speak("opening mysql workbench for you")
			os.system("MySQLWorkbench.exe")
			speak("What else you want me to do")
		
		elif "firefox" in query or "mozilla" in query:
			speak("opening firefox browser for you")
			os.system("firefox")
			speak("What else you want me to do")

		elif "cmd" in query or "command prompt" in query or "prompt" in query or "terminal" in query:
			speak("Launching your command prompt")
			os.system("cmd")
			speak("What else you want me to do")

		elif "vs code" in query:
			speak("Launching your visual studio code")
			os.system("code")
			speak("What else you want me to do")    

		#elif "help me" in query or "do for me" in query:
			#helpMe()
			#takeCommand()	

		else:
			speak("Sorry I could not understand. Could you say that again please . . .")
			takeCommand()

		if "leave" in query or "exit" in query or "thank" in query or "you" in query or "thanks" in query:
			speak("Cool!It was nice to help you! Now I'm leaving. Bye!... ")
			exit()

				   
	
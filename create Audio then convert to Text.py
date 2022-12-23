def generateMP3():

    mp3FileName = 'myAudio.mp3'

	# For more info:
	# Text to Speech with Python - read PDF out loud - pyttsx3: https://youtu.be/TKtqLZh6NHA
    # pip install pyttsx3
    import pyttsx3 as tts
    text1 = 3*'Hello Every Body, I am here'

    engine = tts.init()



    engine.save_to_file(text1, mp3FileName)
    engine.runAndWait()

    return mp3FileName

# 1) pip install SpeechRecognition
# 2) Since we're using a windows 10 machine with Python 3.8
# 2.1) pip install pipwin
# 2.2) pipwin install PyAudio

# 3) import and initialize engine
import speech_recognition as sr
engine = sr.Recognizer()

# 4) read mp3 file
mp3FileName = generateMP3()
with sr.AudioFile(mp3FileName) as source:
    print('File is being analised...')
    audio = engine.record(source)

# 5) Extract and print text
try:
    text = engine.recognize_google(audio)
    print(f'Text: {text}')
    txtFile = open('textFromMp3.txt', 'a')
    txtFile.writelines(text)
except:
    print('Something gone very wrong...')
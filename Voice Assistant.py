import speech_recognition as sr

def transcribe_audio_to_test(filename):
    recogizer=sr.Recognizer()
    with sr.AudioFile(filename)as source:
        audio=recogizer.record(source) 
    try:
        return recogizer.recognize_google(audio)
    except:
        print("skipping unkown error") 
while True:            
    print("Listening...")
    with sr.Microphone() as source:
        recognizer=sr.Recognizer()
        audio=recognizer.listen(source)
        try:
            transcription = recognizer.recognize_google(audio)
            if transcription.lower()=="jarvis":
                #record audio
                filename ="input.wav"
                print("Say your question(WIP, will only print question)")
                with sr.Microphone() as source:
                    recognizer=sr.Recognizer()
                    source.pause_threshold=1
                    audio=recognizer.listen(source,phrase_time_limit=None,timeout=None)
                    with open(filename,"wb")as f:
                        f.write(audio.get_wav_data())  
                #transcript audio to test 
                text=transcribe_audio_to_test(filename)
                if text:
                    print(f"You said :{text}")
            elif transcription.lower()=="jarvis interface":
                #record audio
                filename ="input.wav"
                print("Say the command you want to execute:")
                with sr.Microphone() as source:
                    recognizer=sr.Recognizer()
                    source.pause_threshold=1
                    audio=recognizer.listen(source,phrase_time_limit=None,timeout=None)
                    with open(filename,"wb")as f:
                        f.write(audio.get_wav_data())  
                #transcript audio to test 
                text=transcribe_audio_to_test(filename)
                if text:
                    print(f"You said :{text}")
                
        except Exception as e:
                    print("An error ocurred : {}".format(e))
print("123456okok2")
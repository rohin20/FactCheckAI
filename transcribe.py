import speech_recognition as sr
from pynput import keyboard
import perpcall

fulltext = []

def on_press(key):
    try:
        if key == keyboard.Key.space:
            if len(fulltext) < 3:
                res = "".join(fulltext[0:len(fulltext)])
            else:
                res = "".join(fulltext[-2:])
            perpcall.ai_call(res)
    except AttributeError:
        pass



def live_transcribe():
    
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 1 
    
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    with sr.Microphone() as source:
        print("Initializing... Please wait for calibration...")
        # Calibrate for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Ready! Start speaking...")
        
        while True:
            try:
                

                audio = recognizer.listen(source) 
                text = f"{recognizer.recognize_google(audio)}\n"
                print(text)
                fulltext.append(text)

                
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Could not request results; {e}\n")
            except KeyboardInterrupt:
                print("\nStopping transcription...")
                break
    print(fulltext)



live_transcribe()

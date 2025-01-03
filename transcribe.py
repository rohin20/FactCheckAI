import speech_recognition as sr

def live_transcribe():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Initializing... Please wait for calibration...")
        # Calibrate for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Ready! Start speaking...")
        
        while True:
            try:
                # Listen for audio input
                audio = recognizer.listen(source)
                
                # Convert speech to text
                text = recognizer.recognize_google(audio)
                

                print(f"{text}\n")
                
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Could not request results; {e}\n")
            except KeyboardInterrupt:
                print("\nStopping transcription...")
                break

live_transcribe()

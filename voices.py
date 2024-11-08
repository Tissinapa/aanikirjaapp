import pyttsx3
import PyPDF2
import threading
from pydub import AudioSegment
from pydub.playback import play
import time
import os

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.is_paused = False
        self.is_playing = False
        self.audio_segment = None
        self.audio_thread = None
        self.audio_file = None

    def invalid_Input(self):
        
        self.engine.say("Fuck you. Invalid input")
        self.engine.runAndWait()
        return None

    def start(self):
        
        self.engine.say("Let's start")
        self.engine.runAndWait()
        return None

    def goodbye(self):

        self.engine.say("Goodbye. Wait! Fuck you")
        self.engine.runAndWait()

        return None

    def text_from_user(self, text):
        
        self.engine.say(text)
        self.engine.runAndWait()
        return None

    def pdf_to_mp3(self, pdf_file):
        
        try: 
            new_pdfmp3_name = pdf_file.replace(".pdf", ".mp3")
            self.audio_file = new_pdfmp3_name
            print(self.audio_file)
            reader = PyPDF2.PdfReader(pdf_file)
            pdf_text = ""
            for page in reader.pages:
                pdf_text += page.extract_text() +"\n"
            
            #convert to mp3
            self.engine.save_to_file(pdf_text, self.audio_file)
            self.engine.runAndWait()
            print(f"PDF file converted to {self.audio_file}")
            
            self.audio_segment = AudioSegment.from_mp3(self.audio_file)
            
        except FileNotFoundError: 
            print("PDF file not found.")
            self.engine.say("PDF file not found")
            self.engine.runAndWait()
        
        except Exception as error:
            print(f"Error occured: {error}")
            self.engine.say("Error occured while reading pdf file")
            self.engine.runAndWait()
    
    def play_audio(self):
        if not self.is_playing and self.audio_segment:
            self.is_playing = True
            self.is_paused = False
            self.audio_thread = threading.Thread(target=self._play_audio_segment)
            self.audio_thread.start()
        elif self.is_paused:
            self.is_paused = True
    
    
    def pause_audio(self):
        if self.is_playing:
            self.is_paused = True  # Pause playback

    def stop_audio(self):
        if self.is_playing:
            self.is_playing = False  # Stop playback
            self.is_paused = False
        
    def _play_audio_segment(self):
        segment_length_ms = 1000
        
        for i in range(0 , len(self.audio_segment), segment_length_ms):
            if not self.is_playing:
                break
            if self.is_paused:
                while self.is_paused:
                    time.sleep(0.1)
            play(self.audio_segment[i:i + segment_length_ms])
        self.is_playing = False
        
        
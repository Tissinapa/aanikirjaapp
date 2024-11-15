##from voices import VoiceAssistant

import pyttsx3
import PyPDF2
from threading import *
##from pydub import AudioSegment
##from pydub.playback import play
import pygame
import time
import tempfile
import os



class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.is_paused = False
        self.is_playing = False
        self.file_validate = None
        #self.audio_thread = None
        self.audio_file = None
        self.start_pygame = pygame.mixer.init()

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
            #new_pdfmp3_name = pdf_file.replace(".pdf", ".wav")
            self.audio_file = pdf_file
            
            print(self.audio_file)
            reader = PyPDF2.PdfReader(pdf_file)
            pdf_text = ""
            for page in reader.pages:
                pdf_text += page.extract_text() +"\n"

            #convert to mp3
            self.engine.save_to_file(pdf_text, self.audio_file)
            self.engine.runAndWait()
            print(f"PDF file converted to {self.audio_file}")
            #self.audio_segment = pygame.mixer.music
            
        except FileNotFoundError: 
            print("PDF file not found.")
            self.engine.say("PDF file not found")
            self.engine.runAndWait()
        
        except Exception as error:
            print(f"Error occured: {error}")
            self.engine.say("Error occured while reading pdf file")
            self.engine.runAndWait()
    
    
    def play_mp3(self):
        if not self.is_playing:  # If not already playing
            if self.is_paused:  # If paused, unpause
                pygame.mixer_music.unpause()
                self.is_paused = False
            else:  # Start playing from the beginning or a specific position
                pygame.mixer_music.load(self.audio_file)
                pygame.mixer_music.play(loops=0, fade_ms=1000)
            self.is_playing = True
        else:  # If already playing, toggle pause
            self.pause_mp3()

    def pause_mp3(self):
        if not self.is_paused:  # If not already paused
            pygame.mixer_music.pause()
            self.is_paused = True
            self.is_playing = False

    def stop_mp3(self):
        pygame.mixer_music.stop()


def menu():
    
    print("1) Insert text")
    print("2) Insert pdf file")
    print("Play")
    print("Pause")
    print("0) End")
    user_input=input("Your choice: ")
    return user_input

def give_text():
    users_text = input("Enter text here: ")
    return users_text
    
def give_pdf_file():
    users_pdf_file = input("Enter pdf file here: ")
    return users_pdf_file

def validate_pdf(pdf_file):
    if not os.path.exists(pdf_file):
        print("File does not exist.")
        return False
    if not pdf_file.lower().endswith(".pdf"):
        print("Invalid file type. Please provide a PDF file.")
        return False
    return True

def main():
    voices = VoiceAssistant()
    voices.start()
    
    user_input = None
    while(user_input != 0):
        user_input = menu()    
        
        if user_input == "1":
            some_text = give_text()
            validate_pdf(some_text)
            if validate_pdf == True:
                voices.text_from_user(some_text)
        # get pdf file and convert it
        elif user_input == "2":
            some_pdf_file = give_pdf_file()
            voices.pdf_to_mp3(some_pdf_file) 
        elif user_input == "Play":
            voices.play_mp3()
        elif user_input == "Pause":
            voices.pause_mp3()
        elif user_input == "stop":
            voices.stop_mp3()
            print("Stopped")

        elif user_input == "0":
            voices.goodbye()
            break 
        else:
            voices.invalid_Input()
            
if __name__ == "__main__":
    main()
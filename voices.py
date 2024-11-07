import pyttsx3
import PyPDF2

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()

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

    def speaks_in_pdf(self, pdf_file):
        
        try: 
            reader = PyPDF2.PdfReader(pdf_file)
            full_text= ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                full_text += page.extract_text()
            
            self.engine.say(full_text)
            self.engine.runAndWait()
        except: 
            print("PDF file not found.")
            self.engine.say("PDF file not found")
            self.engine.runAndWait()
        
        return None
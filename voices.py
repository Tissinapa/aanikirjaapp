import pyttsx3
import PyPDF2


def invalid_Input():
    engine = pyttsx3.init()
    engine.say("Fuck you")
    engine.runAndWait()
    engine.say("Invalid input")
    engine.runAndWait()
    return None

def start():
    engine = pyttsx3.init()
    engine.say("Let's start")
    engine.runAndWait()
    return None

def goodbye():
    engine = pyttsx3.init()
    engine.say("Goodbye. Wait! Fuck you")
    engine.runAndWait()

    return None

def text_from_user(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    return None

def speaks_in_pdf(pdf_file):
    engine = pyttsx3.init()
    reader = PyPDF2.PdfReader(pdf_file)
    full_text= ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        full_text += page.extract_text()
    
    engine.say(full_text)
    engine.runAndWait()
    
    
    return None
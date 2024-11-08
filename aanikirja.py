from voices import VoiceAssistant

def menu():
    
    print("1) Insert text")
    print("2) Insert pdf file")
    print("3) Play/Pause")
    print("0) End")
    user_input=input("Your choice: ")
    return user_input

def give_text():
    users_text = input("Enter text here: ")
    return users_text
    
def give_pdf_file():
    users_pdf_file = input("Enter pdf file here: ")
    return users_pdf_file

def main():
    voices = VoiceAssistant()
    voices.start()
    
    user_input = None
    while(user_input != 0):
        user_input = menu()    
        
        if user_input == "1":
            some_text = give_text()
            voices.text_from_user(some_text)
        # get pdf file and convert it
        elif user_input == "2":
            some_pdf_file = give_pdf_file()
            voices.pdf_to_mp3(some_pdf_file) 
        elif user_input == "3":
            if voices.paused.is_set():
                voices.pause()
                print("Paused")
            else:
                voices.resume()
                print("Resume")
        elif user_input == "stop":
            voices.stop()
            print("Stopped")

        elif user_input == "0":
            voices.goodbye()
            break 
        else:
            voices.invalid_Input()
            
if __name__ == "__main__":
    main()
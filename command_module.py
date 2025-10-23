import datetime
from io_module import *  # Import speak function from combined IO module
from app_launch import *

def process_command(command, mode):
    command = command.lower()
#---------------simple commands---------------
    if ("hello" == command) or ("hi" == command):
        speak("Hello,How can I assist you?")
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
       
    elif "quit" in command or "exit" in command:
        speak("Come again whenever you need help from me. Goodbye!")
        return False  # Signal to main loop to stop
    elif "what is your name" in command:
        speak("I am Gravies! your virtual assistant.")
    elif "gravies help" in command:
       speak("Here are some commands you can use:")
       print("- Open app [app name]\n- Open website [website name]\n- Search about [topic]\n- Play music [music name]\n- Send email\n- Weather in [city name]\n- Tell me a joke\n- Wikipedia [topic]\n- News\n- Search in YouTube [query]\n- Play in YouTube [video name]\n- Shutdown\n- Restart\n- Log off\n- Send WhatsApp message\n- Send smart email\n- Send smart WhatsApp message")
#---------------app commands---------------
    elif "open" in command:    
         if "website" in command or "site" in command:    
            site_name = command.replace("open website", "").strip() if "open website" in command else command.replace("open site", "").strip()        
            open_website(site_name)
         elif "open multiple apps" in command:
             app_list = command.replace("open multiple apps", "").strip()
             app = [a.strip() for a in app_list.split(",")]
             open_multiple_apps(app)
         elif command.startswith("open app"):
             app_name = command.split("app")[-1].strip()
             open_app(app_name)
        
         elif "open folder" in command:
                 folder_path = input("Please enter the full folder path: ")
                 open_folder(folder_path)
         elif "open file" in command:
             file_path = input("Please enter the full file path: ")
             open_file(file_path)

    elif "search about" in command:
        query = command.split("about")[-1].strip()
        open_website(query)
           

    
#-------------music commands-------------
    elif "play music" in command:
        music_name = command.replace("play music", "").strip()
        play_music(music_name)
    elif "stop music" in command:
        stop_music()
    elif "pause music" in command:
        pause_music()
    elif "resume music" in command:
        resume_music()
    elif "next track" in command:
        next_track()
    elif "previous track" in command:
        previous_track()
#-----------------system commands-----------------
    elif "shutdown" in command:
        if mode == 'v':
            speak("Are you sure you want to shut down? Please confirm by saying Yes or No.")
            confirm = listen_voice().lower()
            if "yes" in confirm:
                shut_down()
            elif "no" in confirm:
                speak("Shutdown canceled.")
        elif mode == 't':
            user = input(" Enter Y/N if you want to proceed with shutdown: ")
            if user.lower() == "y":
                shut_down()
            else:
                speak("Shutdown canceled.")
    elif "restart" in command:
        if mode == 'v':
            speak("Are you sure you want to restart? Please confirm by saying Yes or No.")
            confirm = listen_voice().lower()
            if "yes" in confirm:
                restart()
            elif "no" in confirm:
                speak("Restart canceled.")
        elif mode == 't':
            user = input("Enter Y/N if you want to proceed with restart: ")
            if user.lower() == "y":
                restart()
            else:
                speak("Restart canceled.")
    elif "log off" in command:
        if mode == 'v':
            speak("Are you sure you want to log off? Please confirm by saying Yes or No.")
            confirm = listen_voice().lower()
            if "yes" in confirm:
                log_off()
            elif "no" in confirm:
                speak("Log off canceled.")
        elif mode == 't':
             user = input("Enter Y/N if you want to proceed with log off: ")
             if user.lower() == "y":
                 log_off()
             else:
                 speak("Log off canceled.")

#----------------------- Additional Features ------------------ #
    elif "send whatsapp message" in command:
        if mode == 'v':
            speak("Please provide the recipient's name")
            receiver = listen_voice()
            print(receiver)
            speak("Please provide the message")
            message = listen_voice()
            print(message)
        elif mode == 't':
            receiver = input("Please enter the recipient's name: ")
            message = input("Please enter your message: ")
        try:
            watsmsg(receiver, message)
            speak("WhatsApp message sent successfully.")
        except Exception as e:
            speak(f"Failed to send WhatsApp message. Error: {e}")
    elif "send email" in command or "send mail" in command:
            if mode == 'v':
                speak("Please provide the recipient's email address")
                text = listen_voice()
                def clean_text(text):
                    return text.replace(" at ", "@").replace(" dot ", ".").replace(" ", "").lower()
                recipient = clean_text(text)
                print(recipient)
                speak("Please provide the email subject")
                subject = listen_voice()
                print(subject)
                speak("Please provide the email body")
                body = listen_voice()
                print(body)
            elif mode == 't':
                recipient = input("Please enter the recipient's email address: ")
                subject = input("Please enter the email subject: ")
                body = input("Please enter the email body: ")
            try:
                send_email(recipient, subject, body)
            except Exception as e:
                speak(f"Failed to send email. Error: {e}")
       
    elif "weather" in command:
        city_name = None
        if "weather in" in command or "weather at" in command:
              city_name = command.split("weather in")[-1].strip() if "weather in" in command else command.split("weather at")[-1].strip()
        if not city_name:
            if mode == "v":
                speak("Please say the city name")
                city_name = listen_voice()
            elif mode == "t":
                city_name = input("Enter city name: ")
        
        try:
            weather(city_name)
        except Exception as e:
            speak(f"Failed to retrieve weather information. Error: {e}")
    elif "joke" in command:
        tell_joke()
    elif "wikipedia" in command:
        topic = command.split("wikipedia")[-1].strip()
        if not topic:
            if mode == "v":
                speak("Please say the topic you want to search on Wikipedia")
                topic = listen_voice()
            elif mode == "t":
                topic = input("Enter the Wikipedia topic: ")
        try:
            wiki_summary(topic)
        except Exception as e:
            speak(f"Failed to fetch information from Wikipedia. Error: {e}")
    elif "news" in command:
        try:
            news()
        except Exception as e:
            speak(f"Failed to fetch news. Error: {e}")
        
    elif "search in youtube" in command:
        query = None
        if "search in youtube" in command:
            query = command.split("youtube")[-1].strip()
        if not query:
            if mode == "v":
                speak("Please say what you want to search in youtube")
                query = listen_voice()
            elif mode == "t":
                query = input("Enter your YouTube search query: ")
        try:
            youtube_search(query)
        except Exception as e:
            speak(f"Failed to search in YouTube. Error: {e}")
    elif "play in youtube" in command:
        video_name = command.split("youtube")[-1].strip()
        if not video_name:
            if mode == "v":
                speak("Please say the video name you want to play in YouTube")
                video_name = listen_voice()
            elif mode == "t":
                video_name = input("Enter the YouTube video name: ")
        try:
            youtube_play(video_name)
        except Exception as e:
                    speak(f"Failed to play on YouTube. Error: {e}")
    elif "schedule whatsapp message" in command:
        if mode == 'v':
            speak("Please provide the recipient's number with country code")
            number = (listen_voice())
            number = "+" + "".join(filter(str.isdigit, number))
            print(number)
            speak("Please provide the message")
            
            message = listen_voice()
            print(message)
            speak("Please provide the hour in 24-hour format")
            hour = int(listen_voice())
            print(hour)
            speak("Please provide the minute")
            minute = int(listen_voice())
            print(minute)
        elif mode == 't':
            number = (input("Please enter the recipient's number with country code: "))
            number = "+" + "".join(filter(str.isdigit, number))
            message = input("Please enter your message: ")
            hour = int(input("Enter hour in 24-hour format: "))
            minute = int(input("Enter minute: "))
        try:

            schedule_message(number, message, hour, minute)
        except Exception as e:
            speak(f"Failed to schedule WhatsApp message. Error: {e}")
    elif "tell" in command or "gravies" in command:
        prompt = command.split("tell")[-1].replace("gravies", "").strip()
        if prompt:
            ask_open_ai(prompt)
        else:
            speak("Please provide a prompt for me to respond.")
    
    elif "send smart whatsapp message" in command:
        if mode == 'v':
            speak("Please provide the receiver's name")
            receiver = listen_voice()
            print(receiver)
        
            speak("Please provide the context for the message")
            context = listen_voice()
            print(context)
        elif mode == 't':
            receiver = input("Please enter the recipient's name: ")
            context = input("Please enter the context for the message: ")
        smart_whatsmsg(receiver, context)
        speak("Smart WhatsApp message sent successfully.")

    
    elif "send smart email" in command:
        if mode == 'v':
            speak("Please provide the recipient's email address")
            text = listen_voice()
            recipient = text.replace(" at ", "@").replace(" dot ", ".").replace(" ", "").lower()
            print(recipient)
            speak("Please provide the subject for the email")
            subject = listen_voice()
            print(subject)
            speak("Please provide the context for the email")
            context = listen_voice()
            print(context)
        elif mode == 't':
            recipient = input("Please enter the recipient's email address: ")
            subject = input("Please enter the subject for the email: ")
            context = input("Please enter the context for the email: ")
        
        smart_email(recipient, subject, context)
        speak("Smart email sent successfully.")
    
    
    else:
        speak("I am still learning this command.")


    return True  # Continue the main loop

    
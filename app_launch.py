import os 
import webbrowser
import time
import pyautogui
import requests
import wikipedia
import pyjokes
from openai import OpenAI
import pywhatkit
from io_module import speak
from dotenv import load_dotenv
import threading
# Load environment variables from .env
load_dotenv() 
Email_id = os.getenv("Email_id")
Email_pass = os.getenv("Email_pass")
Weather_API_KEY = os.getenv("Weather_API_KEY")
News_API_KEY = os.getenv("News_API_KEY") 
sambanova_API_KEY = os.getenv("sambanova_API_KEY")
# ------------------ APP PATHS ------------------ #
app_paths = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": r"C:\Windows\System32\notepad.exe",
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "opera": r"C:\Users\gaura\Desktop\Opera GX Browser.lnk",
    "whatsapp": r"C:\Users\Public\Desktop\WhatsApp.lnk"
}


# ------------------ APP FUNCTIONS ------------------ #
def open_app(app_name):
    app_name = app_name.lower()

    # try direct match
    if app_name in app_paths:
        path = app_paths[app_name]
    else:
        # fuzzy search: check if app_name contains a known key
        path = None
        for key in app_paths:
            if key in app_name:
                path = app_paths[key]
                app_name = key
                break

    if path:
        try:
            os.startfile(path)
            speak(f"Opening {app_name}")
        except Exception as e:
            speak(f"Failed to open {app_name}. Error: {e}")
            
 
    else:
        speak(f"Sorry, I don't know how to open {app_name}.")


def open_multiple_apps(app_list, delay=1):
    """
    Open multiple apps sequentially.
    - app_list: list of app names (strings)
    - delay: seconds to wait between launching each app
    """
    if not app_list:
        speak("No apps specified to open.")
        return

    for key in app_paths:
        if key in app_list:
            try:
                open_app(key)  # call your robust open_app function
            except Exception as e:
                speak(f"Failed to open {key}. Error: {e}")
                
            time.sleep(delay)


# ------------------ WEBSITE FUNCTIONS ------------------ #


def open_website(site_name):
    """
    Open a website or search query.
    - Single word: tries site_name.com
    - Multiple words: performs Google search
    - browser: 'chrome', 'brave', or default system browser
    """
    site_name = site_name.strip().lower()

    if " " not in site_name:
        url = f"https://{site_name}.com"
    else:
        query = site_name.replace(" ", "+")
        url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

    speak(f"Opening {site_name}")
#-------------------MUSIC FUNCTIONS-------------------#
def play_music(song_name= None):
    if song_name:
        query = song_name.replace(" ", "+")
        url = f"https://music.youtube.com/search?q={query}"
        speak(f"Playing {song_name} on YouTube Music")
        
    else:
        url = "https://music.youtube.com"
        
    webbrowser.open(url)
    time.sleep(2)  
    pyautogui.click(1305,538)
    time.sleep(2)
    pyautogui.press("play")

def stop_music():
    pyautogui.press("playpause")
    speak("Music stopped.")
    

def pause_music():
    pyautogui.press('playpause')
    speak("Music paused.")
  

def resume_music():
    pyautogui.press('playpause')
    speak("Music resumed.")
    

def next_track():
    time.sleep(2)
    pyautogui.press("nexttrack")
    speak("Playing next track.")
   
def previous_track():
    time.sleep(2)
    pyautogui.press("previoustrack")
    speak("Playing previous track.")
    

# ------------------ FOLDER & FILE FUNCTIONS ------------------ #
def open_folder(path):
    """Open a folder in File Explorer."""
    if os.path.exists(path):
        os.startfile(path)
        speak(f"Opening folder {path}")
      
    else:
        speak(f"Folder {path} does not exist.")
        

def open_file(file_path):
    """Open a specific file."""
    if os.path.exists(file_path):
        os.startfile(file_path)
        speak(f"Opening file {file_path}")
        
    else:
        speak(f"File {file_path} not found.")
        
# ------------------ SYSTEM COMMANDS ------------------ #
def shut_down(delay=5):
    speak(f"Shutting down the system in {delay} seconds.")
    time.sleep(delay)
    os.system("shutdown /s /t 1")

def restart(delay=5):
    speak(f"Restarting the system in {delay} seconds.")
    time.sleep(delay)
    os.system("shutdown /r /t 1")

def log_off(delay=5):
    speak(f"Logging off the system in {delay} seconds.")
    time.sleep(delay)
    os.system("shutdown /l")

#-------------------------- Additional Features ------------------ #

def watsmsg(receiver, message):
    ask = input("do you have whatsapp app in your desktop(yes or no):")
    if ask =="yes":
       pyautogui.press("win")
       time.sleep(1)
       pyautogui.write("WhatsApp")
       time.sleep(1)
       pyautogui.press("enter")
       time.sleep(5)
       pyautogui.write(receiver)
       time.sleep(3)
       pyautogui.press("down")
       pyautogui.press("enter")
       time.sleep(5)
       pyautogui.write(message)
       time.sleep(10)
       pyautogui.press("enter")
    else :
        user = input("enter your the receiver number:")
        pywhatkit.sendwhatmsg_instantly(f"+91{user}",f"{message}",15,True,2)


def send_email(recipient, subject, body):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sender_email = Email_id
    sender_password = Email_pass


    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            speak(f"Email sent to {recipient}")
    except Exception as e:
        speak(f"Failed to send email. Error: {e}")
    
def weather(city_name):   
    api_key = Weather_API_KEY
    base_url = "http://api.weatherapi.com/v1/current.json"

    complete_url = f"{base_url}?key={api_key}&q={city_name}"
    
    response = requests.get(complete_url)
    x = response.json()
    
    if "error" not in x:
        current_temperature = x["current"]["temp_c"] 
        current_humidity = x["current"]["humidity"]    
        weather_description = x["current"]["condition"]["text"]  
    
       
        speak(f"Temperature: {current_temperature} degrees Celsius")
        time.sleep(1)   
        speak(f"Humidity: {current_humidity} percent")
        time.sleep(1)
        speak(f"Description: {weather_description}")
    else:
        print("City not found")
    
def wiki_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        
        speak(summary)
    except wikipedia.DisambiguationError as e:
        speak("The query is ambiguous. Please be more specific.")
    except wikipedia.PageError:
        speak("No page found for the given query.")
    except Exception as e:
        speak(f"An error occurred: {e}")
def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def news():
       speak("--------welcome to GOT News-----")
       country = input("enter country only 2-letter country codes (like us, in, gb):").strip().lower()
       category = input("enter category (business, sports, technology, health, etc:").strip().lower()
       
       url = "https://newsapi.org/v2/top-headlines"
       params = {"apiKey":News_API_KEY,
                 "country": country,
                 "category": category}
       
       response = requests.get(url, params=params)
       if response.status_code == 200:
           print("News fetched successfully!")
           news_data = response.json()
           articles = news_data.get("articles", []) # 
           if not articles:
               print("No articles found for the given criteria.")
           else:
                speak(f"Here are the top news articles in {country.upper()} for {category} category:")
                time.sleep(2)
                for i, article in enumerate(articles, start=1):
                    speak(f"{i}. Title: {article.get('title')}")
                    print(f"   Description: {article.get('description')}")
                    print(f"   URL: {article.get('url')}")
                    print("-" * 40)
                    time.sleep(1)
                    if i >= 5:
                        break
               
       else:
           speak("Failed to fetch news.", response.status_code, response.text)
       


def youtube_search(query):
    query = query.strip().replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"

    try:
        # Try opening YouTube in the browser
        webbrowser.open(url)
        speak(f"Searching YouTube for {query.replace('+', ' ')}.")
        time.sleep(2)

    except webbrowser.Error:
        
        speak("Could not open YouTube in browser. Trying another method...")
        pywhatkit.search(query)
        time.sleep(2)

    except Exception as e:
        # Catch any unexpected errors
        speak(f"An error occurred while searching YouTube: {e}")
    
def youtube_play(video_name):
    try:
        if video_name:
            pywhatkit.playonyt(video_name)
            speak(f"Playing {video_name} on YouTube")
        else:
            speak("Please provide a video name to play.")
    except Exception as e:
             speak(f"An error occurred: {e}")
def send_whatsapp_message(number, message, hour, minute):
    print(f"In {hour}:{minute} WhatsApp will open and send your message.")
    pywhatkit.sendwhatmsg(number, message, hour, minute)
    print("Message scheduled successfully!")

def schedule_message(number, message, hour, minute):
    t = threading.Thread(target=send_whatsapp_message, args=(number, message, hour, minute))
    t.start()
    print("Message scheduled — continuing other tasks...")
    time.sleep(2)
def ask_open_ai(prompt):
    client = OpenAI(
        base_url = "https://api.sambanova.ai/v1",
        api_key = sambanova_API_KEY
    )
    try:
        response = client.chat.completions.create(
            model = "Meta-Llama-3.1-8B-Instruct",
            messages=[  
                {"role": "system","content": "You are Gravies, a helpful AI assistant."},
                {"role": "user","content": prompt}
            ]
        )
        answer = response.choices[0].message.content
        print("Gravies:", answer)
        tell = input("do you want me to speak the result(yes or no)")
        if tell == "yes":
            speak(answer)
        ask = input("Do you want to ask anything else? (yes/no): ").strip().lower()
        if ask == "yes":
            new_prompt = input("Enter your next question: ")
            ask_open_ai(new_prompt)
        else:
            speak("Thank you for using Gravies AI section.")        
    except Exception as e:
             speak(f"An error occurred: {e}")
def text_generation(prompt,purpose= "general"):
    client = OpenAI(
         base_url="https://api.sambanova.ai/v1",
         api_key=sambanova_API_KEY
    )
    try:
        response = client.chat.completions.create(
            model = "Meta-Llama-3.1-8B-Instruct",
            messages=[
                {"role": "system","content": f"You are Gravies, a helpful AI assistant{purpose}."},
                {"role": "user","content": prompt}
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
             speak(f"An error occurred: {e}")
             return None
def smart_whatsmsg(receiver,context):   
    import tempfile
    receivers  = receiver.strip()
    msg = text_generation(context,purpose=" to write a WhatsApp message")
    msg = msg.split(":")[-1].strip() if msg else None
    if msg:
        print("Generated Message:")
        print("------------------")
        print(msg)
        print("------------------")
        print("Opening Notepad for you to edit the message. Save and close Notepad when done.")
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w+', encoding='utf-8') as tf:
            tf.write(msg)
            tf.flush()
            temp_path = tf.name
        os.system(f'notepad "{temp_path}"')
        with open(temp_path, 'r', encoding='utf-8') as f:
            edited_msg = f.read().strip()
        if edited_msg:
            msg = edited_msg
        os.remove(temp_path)
        confirm = input(f"Send this message? (yes/no): ").strip().lower()
        if confirm == "yes":
            watsmsg(receivers,msg)
            speak(f"Message sent to {receivers}")
        else:
            speak("Message not sent.")
        # temp file already removed via temp_path; no further cleanup needed here
    else:
        speak("Failed to generate a message.")

def smart_email(recipient, subject, context):
    import tempfile
    recipients = recipient.strip()
    subjects = subject.strip()
    body = text_generation(context,purpose=" to write a professional email")
    if body:
        body = body.startswith("Email Body:") and body.split(":",1)[1].strip() or body
        print("Generated Email Body:")
        print("----------------------")
        print(body)
        print("----------------------")
        print("Opening Notepad for you to edit the email body. Save and close Notepad when done.")
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w+', encoding='utf-8') as tf:
            tf.write(body)
            tf.flush()
            temp_path = tf.name
        os.system(f'notepad "{temp_path}"')
        with open(temp_path, 'r', encoding='utf-8') as f:
            edited_body = f.read().strip()
        if edited_body:
            body = edited_body
        os.remove(temp_path)
        confirm = input("Send this email? (yes/no): ").strip().lower()
        if confirm == "yes":
            send_email(recipients,subjects, body)
            speak(f"Email sent to {recipients}")
        else:
            speak("Email not sent.")
        # temp file already removed via temp_path; no further cleanup needed here
    else:
        speak("Failed to generate email content.")
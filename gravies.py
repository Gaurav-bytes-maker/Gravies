from io_module import *
from command_module import process_command

speak("Welcome to Gravies!")

while True:
    mode = input("Select mode: 'v' for voice, 't' for text, 'q' to quit: ").lower()
    if mode == 'q':
        speak("Exiting Gravies. Bye!")
        break
    elif mode == 'v':
        command = listen_voice()
    elif mode == 't':
        command = listen_text()
    else:
        speak("Invalid mode.")
        continue

    if not command:
        speak("No command detected. Please try again.")
        continue

    try:
        should_continue = process_command(command,mode)
        if not should_continue:
            speak("Exiting Gravies. Bye!")
            break
    except Exception as e:
        speak(f"Oops! Something went wrong: {e}")
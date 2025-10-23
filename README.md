## Gravies – Voice & Text Virtual Assistant 🤖�️

Gravies is a Python-powered virtual assistant that can perform a wide range of tasks via voice or text commands. It can open applications, control music, search the web, send messages/emails, fetch weather & news, tell jokes, and much more — all with AI-enhanced capabilities.

## Features

- Modes: Voice and text command input

- System Control: Open apps, folders, and files; shutdown, restart, log off

- Search: Web and YouTube search

- Music: Play, pause, and control music

- Communication: Send WhatsApp messages and emails (including AI-generated suggestions)

- Information: Fetch weather, news, and Wikipedia summaries

- Entertainment: Tell jokes

- AI Integration: OpenAI or SambaNova-powered responses

## Getting Started

### Prerequisites

- Python: 3.8+
- OS: Windows (some features are OS-specific)
- Hardware: Microphone (for voice commands)

### Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/gravies.git
cd gravies
```

2. Create & activate a virtual environment

```powershell
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies

```powershell
pip install -r requirements.txt
```

4. Configure environment variables

Create a `.env` file in the project root with your API keys and credentials (copy from `.env.example`):

```
Email_id=your_email@gmail.com
Email_pass=your_email_password
Weather_API_KEY=your_weather_api_key
News_API_KEY=your_news_api_key
sambanova_API_KEY=your_sambanova_api_key
```

### Running Gravies

```powershell
python gravies.py
```

## Usage

- Select a mode: 'v' for voice or 't' for text.
- Give commands as prompted.
- Smart WhatsApp/Email messages: Edit generated content in Notepad before sending.

## Security

- <strong><span style="color:#c0392b">API keys and passwords must be kept in <code>.env</code> — do NOT commit this file to the repository.</span></strong>

- `.env` is excluded from version control via `.gitignore`.

## Dependencies

- `speech_recognition` – voice recognition
- `pyttsx3` – text-to-speech
- `pyaudio` – microphone input
- `pyautogui` – GUI automation
- `requests` – HTTP requests
- `wikipedia` – Wikipedia summaries
- `pyjokes` – jokes
- `openai` – AI-powered responses
- `pywhatkit` – WhatsApp automation
- `python-dotenv` – environment variables

…and others listed in `requirements.txt`.

## Notes

- WhatsApp automation requires the desktop app and may need the screen to be in focus.
- Voice mode requires a functional microphone.
- AI-powered features need valid API keys.

## What Gravies can do

Gravies is built to be a flexible assistant you can interact with by voice or text. Key capabilities include:

- System control: open apps, folders and files; shutdown, restart, and log off the machine.
- Search and browsing: search the web or YouTube and open results in your browser.
- Media control: play, pause and control music or media players.
- Communication: send WhatsApp messages (via automation) and send emails (supports editing generated text before sending).
- Information: fetch weather, latest news, and Wikipedia summaries.
- Assistance: tell jokes, define words, and return AI-generated answers or suggestions.
- Automation hooks: scriptable actions using OS commands and GUI automation.


Discovering commands and examples

When you call the help command in interactive mode, Gravies will list supported commands and often show example usage (for example: "send whatsapp message", "open chrome", "play music", "get weather in London"). Use these examples as a starting point and adapt them to your needs.

Editing generated messages

If Gravies generates an email or WhatsApp message for you, it may open Notepad (or your default editor) so you can review and edit the content before sending. This is helpful for personalization and accuracy.


## License

This project is for educational and personal use only.
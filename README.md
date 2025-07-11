# 🎙️ Jarvis: Voice-Controlled AI Assistant

An intelligent, voice-driven Python assistant capable of executing file operations, fetching news, interacting with OpenAI, and more—all through speech commands. Designed to simplify desktop interactions and explore practical applications of speech recognition and automation.

---

## 📦 Features

- 🎤 Speech recognition via PocketSphinx and SpeechRecognition
- 📁 File and folder operations (create, delete, list)
- 🧠 AI responses using OpenAI integration
- 🌐 Web browsing and search commands
- 📰 Real-time news headline updates

---

## 🚀 Getting Started

Follow these instructions to get the project up and running locally.

### Prerequisites

- Python 3.8+
- Pip
- Internet connection (for OpenAI and news APIs)

### Installation

```bash
git clone https://github.com/yourusername/jarvis-ai-assistant.git
cd jarvis-ai-assistant
pip install -r requirements.txt
```

Add your OpenAI key in `config.py`:
```python
OPENAI_API_KEY = "your_api_key"
```

---

## 🛠️ Usage

Run the assistant using:

```bash
python main.py
```

Speak a command like:
- “Create a folder named Projects”
- “What’s the latest news?”
- “Ask OpenAI: Tell me about black holes”

---

## 📁 Directory Structure

```plaintext
├── main.py
├── config.py
├── modules/
│   ├── file_manager.py
│   ├── voice_engine.py
│   └── ai_responder.py
├── assets/
│   └── icons, audio samples, etc.
├── README.md
└── requirements.txt
```

---

## 🙌 Credits

- SpeechRecognition and PocketSphinx
- OpenAI GPT API
- News API
- PyAutoGUI and pyperclip for automation scripting
- my creativity and persistence 😊

---

## 📣 Acknowledgements

Special thanks to the Roland Institute of Technology and the coding community that nurtured this project.

---

## 🔗 Contact

Made by [Prajyukta](https://github.com/Prajyukta)  
📫 Email: prajyuktabhanja@gmail.com

---

> “Build things that talk back—because code should reflect your personality too.”

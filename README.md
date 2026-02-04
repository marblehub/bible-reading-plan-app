# 📖 Bible Reading Plan App (PyQt5)

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey)
![GUI](https://img.shields.io/badge/GUI-PyQt5-green)
![API](https://img.shields.io/badge/API-Biblia-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

A professional desktop Bible reading application built with **Python** and **PyQt5**, designed to guide users through a structured daily Bible reading plan while automatically tracking progress.

The app dynamically fetches Scripture passages from the **Biblia API (KJV)** and resumes from the next unread day each time it is opened.

---

## ✨ Features

- 📅 Realistic long-term Bible reading plan (year-scale)
- 🔁 Automatically resumes from the next unread day
- 📘 Clean, readable Scripture formatting (large fonts, red letters)
- 📎 Footnotes, citations, and references supported
- 💾 Persistent progress tracking (JSON-based)
- 🧩 Modular, maintainable project structure
- 🎨 Professionally styled PyQt5 interface

---

## 🖼️ Screenshots
![Main View](screenshots/mainview.png)


```
screenshots/
├── mainview.png
├── reading_progress.png
└── navigation.png
```

## 🚀 Getting Started/Installation
### Clone the repository
    - git clone https://github.com/your-username/bible-reading-app.git
    - cd bible-reading-app

### Create a virtual environment
    - python -m venv venv
    - source venv/bin/activate

### Install dependencies
    - pip install -r requirements.txt


### 🔑 Biblia API Setup
- Register at: https://bibliaapi.com/docs/API_Keys
- Copy your API key
- Open config/settings.py and set:
- API_KEY = "your_api_key_here"

### ▶️ Run the Application
    - python app.py (alternatively: python3 app.py)

The app will automatically:
- Resume from the next unread day
- Fetch passages dynamically
- Save progress when navigating forward


## 📊 Reading Plan Logic
- reading_plan.json defines daily passages
- progress.json stores last completed day
- Progress is updated automatically

## 🔮 Roadmap
- 🌙 Dark mode
- 📆 Calendar-based reading
- 🔔 Daily reminders
- 📦 Standalone executable
- 📱 Mobile version (future)

## 🗂️ Project Structure
bible-reading-app
```
/
│
├── app.py                  # Application entry point
│
├── config/
│   └── settings.py         # API keys and global configuration
│
├── data/
│   ├── reading_plan.json   # Daily reading schedule
│   └── progress.json       # Tracks last completed day
│
├── services/
│   └── biblia_api.py       # Biblia API interaction logic
│
├── ui/
│   └── main_window.py      # PyQt5 UI code
│
├── utils/
│   └── progress_tracker.py # Load/save reading progress
│
├── requirements.txt
├── .gitignore
└── README.md
```
## 📜 License
This project is for personal and educational use.
Scripture content is retrieved via the Biblia API under their terms.

## 🙏 Acknowledgements
- Biblia API
- PyQt5
- Python Open Source Community
```
“Man shall not live by bread alone, but by every word that proceeds from the mouth of God.” — Matthew 4:4
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history.

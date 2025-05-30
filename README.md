# 🖐️ Top Five

**Top Five** is an online party game where one player ranks five random things — from cold pizza to world peace — and everyone else tries to guess their order. It was inspired by a fun game I played in person with my friends, and now that we're all away from each other for the summer, we wanted to continue the fun online.

## 🌐 Live Demo

👉 [Play it here](https://topfive-h7dtbccrgmd8gye8.eastus2-01.azurewebsites.net)

## 🖼️ Screenshot

![Top Five Cover](static/top-five-box.png)

## 🎮 How It Works

1. One player creates a game and is shown 5 random "priorities."
2. They rank them secretly from least to most important.
3. Other players try to guess the same order.
4. The closer the match, the higher the score. Simple and fun!

## 🛠️ Tech Stack

- **Python** + **Flask** (backend)
- **HTML/CSS + JS** (frontend)
- **GitHub Actions** for CI/CD
- **Azure App Service** for hosting

## 🚀 Deployment & CI/CD

This app auto-deploys via **GitHub Actions** on every push to the `main` branch.

![Build Status](https://github.com/jmozden3/Top-Five/actions/workflows/azure-webapp.yml/badge.svg)

## 💻 Local Development

```bash
# Clone the repo
git clone https://github.com/jmozden3/Top-Five.git
cd top-five

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
flask run
Then open your browser to http://localhost:5000.
```

## 📄 License
This project is for educational and entertainment purposes. The original board game inspiration belongs to its respective creators.
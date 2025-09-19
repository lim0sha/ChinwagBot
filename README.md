# Chinwag 😝
## A Telegram ChatBot with Mistral AI + Telegram API

A simple Telegram chatbot for group conversations: it responds whenever someone mentions its `@username` in a chat.  
The bot is powered by:
- [**Telegram Bot API**](https://core.telegram.org/bots/api)  
- [**Mistral AI API**](https://docs.mistral.ai/) for text generation  

---

## 🚀 Features
- Responds to messages in group chats when mentioned via `@username`.
- Powered by Mistral AI for modern, high-quality text generation.
- Easy to set up locally or deploy to a server.
- Uses `.env` for API keys and `prompt.txt` for custom startup instructions.
- Supports both **Polling** (local testing) and **Webhook** (production, Cloud Run).
---

## 📋 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/lim0sha/ChinwagBot.git
cd ChinwagBot
```

### 2. Create a virtual environment and install dependencies
```bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

---
## 🔑 Getting Your API Keys

### 1. Create a Telegram bot via [BotFather](https://t.me/BotFather):

- Open BotFather in Telegram.
- Use the `/newbot` command, choose a name and username.
- BotFather will give you a Telegram Token — add it to your `.env` file.
- To allow the bot to send messages in a group:
  - Go to the group chat → "Manage Group" → "Administrators" → add your bot.
  - Give it the "Send Messages" permission.

### 2. Get your Mistral AI API key:

- Sign up at [**Mistral AI**](https://docs.mistral.ai/)
- Create a new API key.
- Add it to your `.env` file.

---
## ⚙️ Configuration and Running the Bot
### 1. Copy the environment file template
Rename `.env.example` to `.env` and insert your API keys:

`TELEGRAM_TOKEN=your_telegram_token_here`\
`MISTRAL_API_KEY=your_mistral_api_key_here`

### 2. Edit `prompt.txt`
This file contains instructions for the bot at startup.

Example: _You are a helpful Telegram bot. Respond in a friendly and concise way._

### 3. Run the bot (Polling mode — local testing)
```bash
# .env: BOT_MODE=LOCAL
python bot.py
```

### 4. Run the bot (Webhook mode — production)
When deploying to Google Cloud Run or another hosting, set:
```bash
# .env: BOT_MODE=WEBHOOK
```
The Flask server will handle Telegram updates via webhook.

### 5. Test it
- Add the bot to a group chat or send it a direct message.
- Mention it with `@username` and it will reply.

## 🐳 Local Deployment with Docker
### 1. Build Docker image:
```bash
docker build -t chinwagbot .
```

### 2. Run locally with Polling mode:
```bash
docker run --env-file .env -p 8080:8080 chinwagbot
```

## ☁️ Deploying to Google Cloud Run
### 1. Install Google Cloud SDK
- [Google Cloud SDK Docs](https://cloud.google.com/sdk/docs/install)

### 2.Authenticate and set project
```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

### 3. Build Docker image
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/chinwagbot
```

### 4. Deploy to Cloud Run
```bash
gcloud run deploy chinwagbot \
  --image gcr.io/YOUR_PROJECT_ID/chinwagbot \
  --platform managed \
  --allow-unauthenticated \
  --region YOUR_REGION
```

### 5. Set environment variables in Cloud Run UI:
```bash
TELEGRAM_TOKEN=your_token
MISTRAL_API_KEY=your_key
BOT_MODE=WEBHOOK
```

### 6. Set Telegram webhook
```bash
curl -F "url=https://<your-cloud-run-service>.run.app/<TELEGRAM_TOKEN>" \
"https://api.telegram.org/bot<TELEGRAM_TOKEN>/setWebhook"
```
Now Telegram will send updates to your deployed bot.

## 📂 Project Structure
```bash
ChinwagBot/
│
├── bot.py            # Bot source code
├── prompt.txt        # Bot startup instructions
├── Dockerfile        # Docker image configuration
├── .dockerignore     # Files to ignore in Docker build
├── .env.example      # Environment variable template
├── requirements.txt  # Python dependencies
├── docs/
│   └── LICENSE.md    # License file
└── .github/
    └── workflows/
        └── python-ci.yml  # GitHub Actions workflow
```
---
## License
This project is licensed under the MIT License - see the [LICENSE.md](docs/LICENSE.md) file for details.

## Contact
For any questions or feedback, please contact me at [limosha@inbox.ru](mailto:contact@example.com).

---
Feel free to customize this further to better fit your needs!
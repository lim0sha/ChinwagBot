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

- Sign up at [Mistral AI](https://docs.mistral.ai/)
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

### 3. Run the bot
```bash
python bot.py
```

### 4. Test it
- Add the bot to a group chat or send it a direct message.
- Mention it with `@username` and it will reply.

```bash
ChinwagBot/
│
├── bot.py            # Bot source code
├── prompt.txt        # Bot startup instructions
├── .env.example      # Environment variable template
├── requirements.txt  # Python dependencies
└── README.md         # This file
```
---
## License
This project is licensed under the MIT License - see the [LICENSE.md](docs/LICENSE.md) file for details.

## Contact
For any questions or feedback, please contact me at [limosha@inbox.ru](mailto:contact@example.com).

---
Feel free to customize this further to better fit your needs!
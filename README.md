# 🧠 Telegram AI Bot

A Telegram bot powered by a FastAPI backend that processes user queries using OpenAI GPT.

---

## 🚀 Features

- **Telegram Bot**: Fully functional bot with command and message handling  
- **AI Agent**: Integration with OpenAI GPT for intelligent responses  
- **FastAPI Backend**: High-performance backend API  
- **Persistent Memory**: Conversation history stored in PostgreSQL  
- **Docker Support**: Fully containerized for easy deployment  
- **Comprehensive Testing**: Includes unit and integration tests  
- **Security**: Input validation, secure token management, and user access control  

---

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Telegram Bot  │────│ FastAPI Backend │────│   PostgreSQL    │
│   (aiogram 3)   │    │   (AI Agent)    │    │ (Conversations) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                │
                       ┌─────────────────┐
                       │   OpenAI API    │
                       │ (GPT-3.5 Turbo) │
                       └─────────────────┘
```

## 🛠️ Installation & Launch

### 1. Clone the repository

```bash
git clone https://github.com/asqarxom/ai-chatbot
cd ai-chatbot
```

### 2. Set up environment variables

```bash
# Copy the configuration file
cp .env.example .env

# Editing it .env file
nano .env
```

Fill in the following variables in `.env`:

```env
# Telegram Bot
TELEGRAM_TOKEN=

# OpenAI
OPENAI_API_KEY=
OPENAI_MODEL=gpt-3.5-turbo

# Database
POSTGRES_DB=chatbot_db
POSTGRES_USER=chatbot_user
POSTGRES_PASSWORD=
DB_HOST=postgres
DB_PORT=5432

# Redis
REDIS_HOST=redis
REDIS_PORT=6379
```

### 4. Get your OpenAI API Key

1. Sign up at [OpenAI Platform](https://platform.openai.com/)
2. Generate a new API Key
3. Paste it into your `.env` file

### 5. Launch with Docker Compose

```bash
# Build and launch all services
docker-compose up --build
```


## 📝 API Documentation

After the backend is running:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Key Endpoints:

- `GET /health` - Health check
- `POST /api/v1/chat` - Send a message to the AI
- `DELETE /api/v1/conversations/{user_id}` - Clear conversation history
- `GET /api/v1/conversations/{user_id}/history` - Get conversation history
- `GET /api/v1/stats` - Get usage statistics

## 🤖 Bot Commands

- `/start` - Start using the bot
- `/help` - Show help information
- `/clear` - Clear conversation context

## ⚙️ Configuration

### Environment Variables

| Переменная | Описание | Обязательная |
|------------|----------|--------------|
| `TELEGRAM_TOKEN` | Telegram bot token | ✅ |
| `OPENAI_API_KEY` | OpenAI API key | ✅ |
| `OPENAI_MODEL` | OpenAI model (default: gpt-3.5-turbo) | ❌ |
| `DATABASE_URL` | PostgreSQL connection URL | ❌ |
| `BACKEND_URL` | Backend service URL | ❌ |
| `LOG_LEVEL` | Logging level | ❌ |

## 🐛 Debugging

### Common Issues

1. **Bot not responding**:
   - Check the Telegram token
   - Ensure the backend is running
   - Check logs: `docker-compose logs bot`

2. **AI errors**:
   - Check your OpenAI API key
   - Ensure your OpenAI account has balance/credits
   - Monitor API limits and usage

3. **Database issues:**:
   - Confirm PostgreSQL is running
   - Ensure tables are created
   - Check logs: `docker-compose logs postgres`


## 📊 Monitoring

### Metrics

The backend provides:
- Total messages processed
- Unique user count
- Messages sent in the last 24 hours

### Logging

Structured logs for all services:
- INFO for normal operations
- ERROR  for critical failures
- DEBUG for detailed debugging (optional)

## 📄 License

This project is provided as a test assignment.

## 🆘 Support

If you face any issues:

1. Check the Debugging section
2. Review service logs
3. Open a GitHub issue with a detailed description

---

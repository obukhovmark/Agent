# LuxAi

AI Concierge для VIP-клиентов на Python 3.13, GPT-4 и Telegram

## 🚀 Установка

### Требования:
- Python 3.13+
- pip

### Установка:

1. Склонируй репозиторий или распакуй архив
2. Установи зависимости:

```bash
pip install -r requirements.txt
```

3. Создай `.env` файл, добавь ключи:

```env
OPENAI_API_KEY=your-openai-key
TELEGRAM_BOT_TOKEN=your-telegram-token
```

4. Запусти FastAPI сервер:

```bash
uvicorn main:app --reload
```

5. Запусти Telegram-бота:

```bash
python bot.py
```

Готово ✅

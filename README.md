# AI VIP Concierge Starter

## Установка

1. Склонируй репозиторий или распакуй архив
2. Установи зависимости:

```bash
pip install -r requirements.txt
```

3. Создай `.env` файл, добавь свои ключи:

```env
OPENAI_API_KEY=your-openai-key
TELEGRAM_BOT_TOKEN=your-telegram-token
```

4. Запусти FastAPI сервер:

```bash
uvicorn main:app --reload
```

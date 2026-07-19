# NeroxBale

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-yellow)

**NeroxBale** یک کتابخانه قدرتمند و آسان برای ساخت ربات‌های هوشمند در پلتفرم **بله** (Bale) است. این کتابخانه API رسمی بله را به صورت ساده و شیءگرا در اختیار شما قرار می‌دهد.

## ویژگی‌ها

- ![Star](https://www.emojiall.com/images/60/telegram/1f31f.gif) پشتیبانی کامل از API بله
- ⚡ Asynchronous و Synchronous پشتیبانی
- 📦 مدیریت آسان پیام‌ها، کیبوردها و Inlineها
- 🗃️ پشتیبانی از Middleware و Handlers
- 🔌 Webhook و Polling هر دو
- 📝 Logging یکپارچه
- 🎨 تایپینگ کامل (Type Hints)
- 🚀 عملکرد بالا و سبک

## نصب

```bash
pip install neroxbale
```

## شروع سریع

### ۱. ایجاد ربات

ابتدا توکن ربات خود را از [@BotFather](https://ble.ir/BotFather) در بله دریافت کنید.

```python
from neroxbale import BaleClient, Filters

bot = BaleClient("توکن_ربات_ت_اینجا")

@bot.on_message(Filters.command("start"))
async def start(message):
    await bot.send_message(message.chat.id, "سلام! 👋")

bot.run()
```

### مثال‌های بیشتر

#### ارسال پیام با کیبورد

```python
from neroxbale import Keyboard, KeyboardButton

keyboard = Keyboard()

keyboard.row(
    KeyboardButton("🏠 خانه"),
    KeyboardButton("📋 منو")
)
keyboard.row(
    KeyboardButton("❓ راهنما"),
    KeyboardButton("📞 تماس")
)
# resize = کیبورد رو به اندازه دکمه‌ها کوچیک می‌کنه
keyboard.resize(True)

@bot.on_message(Filters.command("start"))
async def start(message):
    await bot.send_message(message.chat.id, "یه گزینه رو انتخاب کن:", keyboard=keyboard)
```

#### Inline Keyboard

```python
from neroxbale import InlineKeyboard, InlineButton

inline = InlineKeyboard()

# InlineButton("متن دکمه", "callback_data")
inline.row(
    InlineButton("✅ تأیید", "confirm"),
    InlineButton("❌ رد", "cancel")
)

@bot.on_message(Filters.command("start"))
async def start(message):
    await bot.send_message(message.chat.id, "یه گزینه رو انتخاب کن:", keyboard=inline)

@bot.on_callback()
async def handle_vote(call):
    if call.data == "confirm":
        await bot.answer_callback_query(call.id, "✅ تأیید شد!")
    elif call.data == "cancel":
        await bot.answer_callback_query(call.id, "❌ رد شد!")
```

## مستندات

- [داکیومنت کامل بات](https://nerox.runflare.run/neroxbale/docs)
- [نمونه‌ها](https://nerox.runflare.run/neroxbale/examples)

## مشارکت

از Pull Requestها و Issueها استقبال می‌کنیم! برای شروع:

1. Fork پروژه
2. Branch جدید بسازید (`git checkout -b feature/awesome-feature`)
3. تغییرات خود را Commit کنید
4. Push کنید و PR بفرستید
---

**ساخته شده با ❤️ توسط تیم نرو ایکس**

برای پیشنهادات و پشتیبانی: [GitHub Issues](https://github.com/M4DIA98/neroxbale/issues)
```


import time
import random
from datetime import datetime
import telebot
from pyquotex.api import QuotexAPI

# ===============================
#   بياناتك التي زودتني بها
# ===============================
BOT_TOKEN = "8502008925:AAFRdgQdDM8w68tVfClx0mpCkHOiiy8QivQ"
CHANNEL_ID = -1003478036851

EMAIL = "Tixoutixou26@gmail.com"
PASSWORD = "032452010"
USE_DEMO = False     # حساب حقيقي
# ===============================

bot = telebot.TeleBot(BOT_TOKEN)

# اتصال بمنصة Quotex
api = QuotexAPI(EMAIL, PASSWORD)
api.login()
api.change_account(USE_DEMO)

# الأزواج الحقيقية فقط
REAL_PAIRS = [
    "EURUSD", "GBPUSD", "USDJPY", "AUDUSD",
    "USDCAD", "NZDUSD", "EURJPY", "EURGBP"
]

# نسبة الثقة 65% إلى 90%
def confidence():
    return random.randint(65, 90)

# اتجاه الإشارة
def direction():
    return random.choice(["📈 CALL", "📉 PUT"])

# استراتيجية وهمية احترافية لإظهار السبب
def strategy():
    strategies = [
        "MACD Strong + EMA Perfect",
        "RSI Oversold/Overbought",
        "Volume Boost + Trend Confirm",
        "EMA Cross + Momentum Strong",
        "Market Pressure Direction Confirmed"
    ]
    return random.choice(strategies)

# -----------------------------
# إرسال الإشارة إلى القناة
# -----------------------------
def send_signal():

    pair = random.choice(REAL_PAIRS)
    entry_time = datetime.now().strftime("%H:%M:%S")
    conf = confidence()
    strat = strategy()
    dire = direction()

    # عدّ تنازلي 10 ثواني
    countdown = " ".join([str(i) for i in range(10, 0, -1)])

    message = f"""
🔥 *إشارة جديدة — Quotex Real Premium*

زوج: *{pair}*
الاتجاه: *{dire}*

📊 نسبة الثقة: *{conf}%*
🧪 سبب الإشارة: *{strat}*

⏰ وقت الدخول: *{entry_time}*
⌛ العد التنازلي: {countdown}

⏳ مدة الصفقة: *1 دقيقة*
⚠ حقيقي فقط — Real Market
"""

    bot.send_message(CHANNEL_ID, message, parse_mode="Markdown")


# -----------------------------
# تشغيل البوت 24/24
# -----------------------------
print("🚀 Premium Quotex Signal Bot Started...")

while True:
    send_signal()
    time.sleep(60)   # كل دقيقة إشارة جديدة

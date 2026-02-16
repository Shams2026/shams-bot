import requests
from datetime import datetime
import pytz  # مكتبة ضبط المناطق الزمنية

# بيانات بوت Shams المحفوظة
TOKEN = "8305317876:AAHkPFr8idftz1Rgc6-tdCugaaZTrQsZnP4"
CHAT_ID = "-5216371452"

def send_youtube_alert():
    # ضبط التوقيت ليكون بتوقيت القاهرة [cite: 2026-02-05]
    egypt_tz = pytz.timezone('Africa/Cairo')
    now = datetime.now(egypt_tz)
    
    # تنسيق الوقت والتاريخ المطلوب [cite: 2026-02-05]
    current_time = now.strftime("%I:%M %p")
    current_date = now.strftime("%Y-%m-%d")

    # الالتزام بقاعدة "الاسم" بدلاً من "كومنت" [cite: 2026-01-30]
    message = (
        f"🚨 *تنبيه : تشتت انتباه*\n\n"
        f"👤 الاسم: احمد مصطفى السيد\n"
        f"📅 التاريخ: {current_date}\n"
        f"⏰ الوقت (القاهرة): {current_time}\n\n"
        f"📺 *الحالة:* تم رصد فتح تطبيق **YouTube** على الجهاز حالياً."
    )

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"✅ تم إرسال التنبيه بتوقيت القاهرة: {current_time}")
        else:
            print(f"❌ فشل الإرسال: {response.text}")
    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

if __name__ == "__main__":
    send_youtube_alert()

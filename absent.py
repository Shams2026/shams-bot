import requests
from datetime import datetime
import pytz # مكتبة ضبط المناطق الزمنية

# بيانات بوت Shams المحفوظة
TOKEN = "8305317876:AAHkPFr8idftz1Rgc6-tdCugaaZTrQsZnP4"
CHAT_ID = "-5216371452"

def send_absent_alert():
    # ضبط التوقيت ليكون بتوقيت مصر [cite: 2026-02-05]
    egypt_tz = pytz.timezone('Africa/Cairo')
    now = datetime.now(egypt_tz)
    
    current_time = now.strftime("%I:%M %p")
    current_date = now.strftime("%Y-%m-%d")

    message = (
        f"🚨 *تنبيه غياب *\n\n"
        f"👤 ولى امر الطالب : احمد مصطفى السيد\n"
        f"📅 التاريخ: {current_date}\n"
        f"⏰ الوقت (بتوقيت مصر): {current_time}\n\n"
        f"⚠️ *ملاحظة:* تجاوزت الساعة 3:15 ولم يحضر الطالب."
    )

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

if __name__ == "__main__":
    send_absent_alert()

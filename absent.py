import requests
from datetime import datetime

# بيانات بوت Shams المحفوظة
TOKEN = "8305317876:AAHkPFr8idftz1Rgc6-tdCugaaZTrQsZnP4"
CHAT_ID = "-5216371452"

def send_absent_alert():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    current_date = now.strftime("%Y-%m-%d")

    # الالتزام بقاعدة "الاسم" بدلاً من كومنت
    message = (
        f"🚨 *تنبيه غياب - Shams*\n\n"
        f"👤 الاسم: طالب لم يحضر\n"
        f"📅 التاريخ: {current_date}\n"
        f"⏰ الوقت: {current_time}\n\n"
        f"⚠️ *ملاحظة:* تجاوزت الساعة 3:15 ولم يتم تسجيل حضور الطالب في السكشن."
    )

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

if __name__ == "__main__":
    send_absent_alert()

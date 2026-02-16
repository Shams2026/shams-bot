import requests
from datetime import datetime

# بيانات بوت Shams المحدثة
TOKEN = "8305317876:AAHkPFr8idftz1Rgc6-tdCugaaZTrQsZnP4"
CHAT_ID = "-5216371452"

def send_shams_alert():
    # جلب الوقت والتاريخ الحاليين [2026-02-05]
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")

    # تنسيق الرسالة: استخدام "الاسم" بدلاً من كومنت [2026-01-30]
    message = (
        f"☀️ *إشعار من بوت Shams*\n\n"
        f"👤 الاسم: طالب لم يحضر بعد\n"
        f"📅 التاريخ: {current_date}\n"
        f"⏰ الساعة الآن: {current_time}\n\n"
        f"⚠️ *تنبيه:* مواعيد السكشن من 3:00 إلى 5:00، والساعة تجاوزت 3:15 ولم يحضر الطالب."
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
            print("✅ تم الإرسال للمجموعة الجديدة بنجاح!")
        else:
            print(f"❌ فشل الإرسال: {response.text}")
    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

if __name__ == "__main__":
    send_shams_alert()

import requests
from datetime import datetime

# بياناتك المسجلة لدينا
TOKEN = "7647299098:AAEmA8FKF_KujX5NbclGMP-cZWFDcTAFA7s"
CHAT_ID = "-5202473852"

def send_alert():
    # جلب الوقت والتاريخ
    now = datetime.now()
    # إضافة ساعتين لتوقيت جرينتش ليطابق توقيت مصر (UTC+2)
    current_time = now.strftime("%I:%M %p") 
    current_date = now.strftime("%Y-%m-%d")

    message = (
        f"📢 *إشعار غياب طالب*\n\n"
        f"👤 الاسم: [أدخل اسم الطالب هنا]\n"
        f"📅 التاريخ: {current_date}\n"
        f"⏰ الساعة الآن: {current_time}\n\n"
        f"⚠️ *تنبيه:* يرجى العلم بأن مواعيد السكشن من 3:00 إلى 5:00، "
        f"والساعة الآن تجاوزت الثالثة والربع ولم يحضر الطالب بعد."
    )

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ تم إرسال الإشعار بنجاح!")
    else:
        print(f"❌ فشل الإرسال: {response.text}")

if __name__ == "__main__":
    send_alert()

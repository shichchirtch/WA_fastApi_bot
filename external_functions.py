from bot_instance import bot_tocken
import requests

BOT_URL = "https://fcae-2a00-20-8-1dfb-3db8-b933-7e45-f0ad.ngrok-free.app/update_order" # Эндпоинт бота для обновления данных
# https://fcae-2a00-20-8-1dfb-3db8-b933-7e45-f0ad.ngrok-free.app

def update_bot_database(user_id, user_name,  address, phone, payment):
    """Отправляет данные в бота через его API."""
    print('works update_bot_database')
    payload = {"user_id": user_id, 'user_name':user_name, "address": address, "phone": phone, "payment": payment}
    try:
        requests.post(BOT_URL, json=payload) # 127.0.0.1 - - [05/Mar/2025 18:43:06] "POST /update_order HTTP/1.1" 404 -
    except Exception as e:
        print(f"Ошибка при отправке в бота: {e}")


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{bot_tocken}/sendMessage"
    payload = {
        "chat_id": -4711453703,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

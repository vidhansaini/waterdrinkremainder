from plyer import notification
import random
import time  

messages = [
    '💧 Time to hydrate! Take a sip of water!',
    '🚰 Water is life! Drink some now.',
    '🥤 Don’t forget your water break!',
    '🕒 It’s water o’clock! Stay hydrated!',
    '💦 Keep your body happy, have a drink!',
    '🌊 Refuel with some water, it’s time!'
]
  
icon_path = "waterdrinkremainder/ico/water_drink.ico"


while True:
    notification_title = '🚰 YOUR DAILY WATER REMINDER!'
    
    notification_message = random.choice(messages)
    
    notification.notify(
        title=notification_title,
        message=notification_message,
        app_icon=icon_path, 
        timeout=10,  
        toast=False
    )

    time.sleep(60 * 60)   
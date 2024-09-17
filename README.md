# 🚰💧 Water Reminder Notification App

This Python-based project reminds you to take regular water breaks by sending fun desktop notifications every hour. Staying hydrated is essential, and this app ensures you never forget to drink water throughout the day!

## 📋 Features
- **Random Fun Messages**: A list of playful and motivating messages to keep your hydration routine exciting.
- **Custom Notification Icon**: A water-themed icon to make your reminders visually engaging.
- **Hourly Notifications**: Notifications are sent every hour to encourage you to take a water break.

## 💻 How to Use
1. **Install the required library**:  
   This project uses the `plyer` library for desktop notifications. Install it by running:
   ```bash
   pip install plyer

2. **Set up the project**:

   Clone the repository or download the project files.

   Ensure that the custom icon `(water_drink.ico)` is placed in the correct directory: `waterdrinkremainder/ico/`.

3. **Run the script**: Execute the script using:
```bash
  python water_reminder.py
```
4. **Notifications**:
The app will send a notification every hour with a random hydration reminder message, keeping your water intake on track.

## 🔧 Customization
- **Messages**: Feel free to edit the list of messages in the script to add your own reminders or fun quotes.
- **Notification Interval**: Adjust the frequency of notifications by changing the time.sleep(60 * 60) line. For example, change 60 * 60 to 30 * 60 for reminders every 30 minutes.

## 🛠️ Running Continuously

To ensure the script runs continuously in the background without the need for an IDE, you can:

- **On Windows**: Use a batch file or Task Scheduler.
- **On macOS/Linux**: Use cron or a background shell script.

Refer to the documentation for more details on setting up background tasks for your operating system.

## 📁 Project Structure

```bash
waterdrinkremainder/
│
├── ico/
│   └── water_drink.ico   # Icon for notifications
│
└── water_reminder.py      # Main script
```

## 🎯 Future Improvements
- **Custom Intervals**: Add a feature to let the user customize reminder intervals via command-line arguments or a config file.
- **Sound Alerts**: Integrate sound notifications to accompany the popup.
- **GUI Version**: Create a simple GUI to manage the app and set reminders more easily.
## 📄 License

This project is licensed under the MIT License.


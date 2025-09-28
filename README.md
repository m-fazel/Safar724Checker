# Bus Availability Checker 🚌

A Python script that continuously monitors bus availability on Safar724 (سفر۷۲۴) and alerts you when buses matching your criteria become available.

## 🎯 Overview

This tool automatically checks for available bus tickets based on your specific requirements (seats, price, time, VIP status) and plays an audible alert when matching buses are found. Perfect for finding bus tickets during peak travel seasons or for last-minute trips.

## ✨ Features

- **🔔 Real-time Alerts**: Plays sound notification when matching buses are found
- **🎯 Customizable Filters**: Set specific criteria for your ideal bus
- **⏰ Time-based Filtering**: Filter by departure time ranges
- **💰 Price Control**: Set maximum price limits
- **💺 Seat Requirements**: Specify exact number of seats needed
- **⭐ VIP Filter**: Option to search for VIP buses only
- **🔄 Continuous Monitoring**: Runs indefinitely until stopped
- **🌐 Safar724 Integration**: Uses official Safar724 API

## 🛠️ Requirements

- Python 3.6+
- `requests` library
- `playsound` library
- Internet connection

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/bus-checker.git
cd bus-checker
```

### 2. Install Dependencies
```bash
pip install requests playsound
```

### 3. Add Alert Sound
Place an MP3 file named `beep.mp3` in the project directory for the alert sound.

## 🚀 Usage

### Basic Usage
```bash
python checker.py
```

### Interactive Setup
When you run the script, it will prompt for:

1. **Date** (YYYY-MM-DD format, e.g., `1403-07-03`)
2. **Origin City** (e.g., `tehran`)
3. **Destination City** (e.g., `esfahan`)
4. **Number of Seats** needed (e.g., `2`)
5. **Maximum Price** (e.g., `2600000`)
6. **Earliest Departure Time** (HH:MM format, e.g., `06:00`)
7. **Latest Departure Time** (HH:MM format, e.g., `18:00`)
8. **VIP Buses Only** (yes/no)

### Example Session
```
Enter the date (in format YYYY-MM-DD, e.g., 1403-07-03): 1403-07-05
Enter the origin city (e.g., tehran): tehran
Enter the destination city (e.g., esfahan): esfahan
Enter the number of seats you need: 3
Enter the maximum price you're willing to pay (e.g., 2600000): 2000000
Enter the earliest departure time (in format HH:MM, e.g., 06:00): 08:00
Enter the latest departure time (in format HH:MM, e.g., 18:00): 22:00
Do you want only VIP buses? (yes/no): yes
Bus found! 4 seats available on bus Seiro Safar at 14:30.
🔊 *beep sound plays*
```

## 📁 Project Structure

```
bus-checker/
├── checker.py          # Main monitoring script
├── beep.mp3           # Alert sound file
├── requirements.txt   # Python dependencies
└── README.md         # Documentation
```

## ⚙️ Configuration

### Filter Criteria
The script checks for buses that match ALL specified criteria:

- **Available Seats** ≥ Required seats
- **Price** ≤ Maximum price
- **Departure Time** within specified range
- **VIP Status** (if VIP-only selected)

### API Endpoint
Uses Safar724 official API:
```
https://service.safar724.com/buses/api/bus/route?Date={date}&Destination={destination}&Origin={origin}
```

## 🔧 Customization

### Modify Check Interval
Change the sleep time in `monitor_buses()` function:
```python
time.sleep(60)  # Check every 60 seconds instead of 1
```

### Add Additional Filters
Extend the `is_good_bus()` function with more criteria:
```python
# Example: Add company preference
preferred_companies = ['Seiro Safar', 'TBT']
company_ok = bus['companyName'] in preferred_companies
return company_ok and (price <= price_limit and ...)
```

### Custom Alert Sound
Replace `beep.mp3` with any MP3 file of your choice.

## ⚠️ Important Notes

### Date Format
- Uses **Jalali (Persian) calendar** format: `YYYY-MM-DD`
- Example: `1403-07-03` for 2024-09-24

### City Names
- Use **English names** as recognized by Safar724
- Common examples: `tehran`, `esfahan`, `mashhad`, `shiraz`, `tabriz`

### Rate Limiting
- Current delay: 1 second between checks
- Consider increasing to 30-60 seconds for extended monitoring
- Respect the API service terms

## 🐛 Troubleshooting

### Common Issues

1. **No Sound Alert**
   ```
   Error: beep.mp3 not found
   ```
   **Solution**: Ensure `beep.mp3` exists in the same directory

2. **No Buses Found**
   - **Check date format** (Jalali calendar)
   - **Verify city names** (use English names)
   - **Adjust filters** (price, time, seat requirements)

3. **Connection Errors**
   ```
   Error occurred: HTTPConnectionPool
   ```
   **Solution**: Check internet connection and retry

4. **Module Not Found**
   ```
   ModuleNotFoundError: No module named 'playsound'
   ```
   **Solution**: Install missing dependencies: `pip install playsound`

### Debug Mode
Add debug output to see all available buses:
```python
print(f"Checking bus: {bus['companyName']} - Seats: {bus['availableSeatCount']} - Price: {bus['price']}")
```

## 🔒 Privacy & Security

- **No Authentication Required**: Uses public API endpoints
- **No Personal Data**: Doesn't store or transmit personal information
- **Local Execution**: All processing happens on your machine

## 🤝 Contributing

Contributions welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/improvement`)
3. **Commit** changes (`git commit -m 'Add new feature'`)
4. **Push** to branch (`git push origin feature/improvement`)
5. **Open** a Pull Request

### Potential Enhancements
- Multiple route monitoring
- SMS/Email notifications
- GUI interface
- Historical price tracking
- Multiple date checking
- Browser automation for booking

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

- **Mohammad Fazel Samavati** - [Your GitHub](https://github.com/m-fazel)

## 🙏 Acknowledgments

- **Safar724** (سفر۷۲۴) for the bus booking service
- **Python requests** library for API calls

## 🆘 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Verify your input formats (date, time, city names)
3. Ensure all dependencies are installed
4. Check your internet connection

---

**Happy travels!** 🚌✨

*Note: This tool is for availability monitoring only. Actual booking must be done through official channels.*
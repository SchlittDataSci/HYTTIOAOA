# HYTTIOAOA

**Have You Tried Turning It Off And On Again?**

A minimalist Python script that toggles the WiFi radio. 
* Fixes most connectivity issues
* Not for use in production environments

## Compatibility

If you don't have an OS tattoo, it will probably work for you:
* **Linux:** `nmcli` or `rfkill`
* **macOS:** `networksetup`
* **Windows:** `netsh` (requires Admin)

## Usage

Is your homelab setup swamping your NAT?
Is your unstatic IP getting ratelimited for perfectly legitimate activities?

Run it. It turns the internet off. Then it waits. Then it turns it back on.
Saves you a trip every time!

```bash
# Toggle with the default 15-second purgatory
python3 wifi_toggle.py

# Specify your own duration (in seconds)
python3 wifi_toggle.py 60
```

## Automation (Service Setup)

Configure this to run automatically because that's the world we're living in.

### Linux (Cron)
The simplest way. Add a root crontab entry.

1. Open crontab: `sudo crontab -e`
2. Add this line to run every Sunday at 4 AM:
   ```cron
   0 4 * * 0 /usr/bin/python3 /path/to/wifi_toggle.py
   ```

### macOS (Launchd)
You must create a daemon so it has root privileges to touch the hardware.
If you've made it this far, you probably sudo yourself out of bed each day - we salute you.

1. Create a file at `/Library/LaunchDaemons/com.hyttioaoa.wifi.plist`
2. Paste this XML (update the path to the script):
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.hyttioaoa.wifi</string>
       <key>ProgramArguments</key>
       <array>
           <string>/usr/bin/python3</string>
           <string>/path/to/wifi_toggle.py</string>
       </array>
       <key>StartCalendarInterval</key>
       <dict>
           <key>Weekday</key>
           <integer>0</integer> 
           <key>Hour</key>
           <integer>4</integer>
       </dict>
   </dict>
   </plist>
   ```
3. Load it: `sudo launchctl load -w /Library/LaunchDaemons/com.hyttioaoa.wifi.plist`

### Windows (Task Scheduler)
Windows requires Admin privileges to toggle adapters.
If you're using Windows, that's on you buddy.

1. Open **Task Scheduler**.
2. **Create Task** (not Basic Task).
3. **General**: Check "Run with highest privileges" and "Run whether user is logged on or not".
4. **Triggers**: New > Weekly > Sunday > 4:00 AM.
5. **Actions**: New > Start a program.
   * Program/script: `python`
   * Add arguments: `C:\path\to\wifi_toggle.py`

## Requirements

* Python 3
* Sufficient privileges to tell the OS what to do (sudo/Administrator).

## License

Do whatever you want with it, this is vibecoded nonsense, I only wrote the jokes.

## Warranty

No.

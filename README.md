# Discord Rich Presence

A lightweight Python script that allows you to display a custom Rich Presence status (e.g., rotating lyrics or messages) on your personal Discord profile. It connects locally to your running Discord Desktop application.

---

## 🚀 Installation

### 1. Prerequisites
* Python 3.10 or newer installed on your machine.
* The official **Discord Desktop** app running.

### 2. Installing Dependencies
Open your terminal in the project directory and install the required libraries:

* **Using Virtual Environment (Recommended):**
  ```powershell
  .\.venv\Scripts\python -m pip install -r requirements-rp.txt
  ```

* **Using System Python (Global):**
  ```powershell
  python -m pip install -r requirements-rp.txt
  ```

---

## ⚙️ Configuration

### 1. Create a Discord Application
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application** and give it a name (this name will show as your status header).
3. Under the **General Information** tab, copy the **Application ID** (Client ID).

### 2. Setup `.env` file
Create a file named `.env` in the root of the project (or copy from `.env.example`) and add your application client ID:
```env
DISCORD_CLIENT_ID=YOUR_DISCORD_APPLICATION_ID
```

### 3. Setup `lyrics.txt`
Create a file named `lyrics.txt` in the root of the project. Write your custom status lines inside. Each line in the file will represent a message that rotates on your Discord status. For example:
```text
Listening to music...
Line number one
Line number two
```

---

## 🏃 Running the Script

### Running with Virtual Environment (Recommended)
```powershell
.\.venv\Scripts\python rich_presence.py
```

### Running with System Python
```powershell
python rich_presence.py
```

### CLI Arguments (Customization)
You can customize the script behavior by passing arguments:
* `--client-id`: Manually pass the Discord Application ID (overrides `.env`).
* `--lyrics-file`: Path to a custom lyrics/message file (defaults to `lyrics.txt`).
* `--delay`: Number of seconds to display each line before switching (defaults to `15.0` seconds).
* `--details`: The text shown in the details line of your presence status (defaults to `Dating`).

**Example of custom execution:**
```powershell
.\.venv\Scripts\python rich_presence.py --delay 10 --details "Listening" --lyrics-file "custom_lyrics.txt"
```

---

## ⚠️ Notes
* The script only works while **Discord Desktop** is open on the same computer. It will not work on Discord Web.
* Press `Ctrl + C` in the terminal to stop the script.

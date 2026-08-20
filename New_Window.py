import subprocess

# Change this number to open more or fewer windows
number_of_windows = 5

# Change this to the website you want to open
website_url = "https://www.google.com"

# Path to Google Chrome on Windows
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Loop to open multiple windows
for i in range(number_of_windows):
  subprocess.Popen([chrome_path, "--new-window", website_url])

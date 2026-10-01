import subprocess

# Change this number to open more or fewer windows
while True:
  number_of_windows = int(input("How many windows do you want to open: "))
  if number_of_windows >= 0:
    break
  else:
    print("Not a real number please try aigain")

# Change this to the website you want to open
website_url = "https://www.google.com"

# Path to Google Chrome on Windows
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Loop to open multiple windows
for i in range(number_of_windows):
  subprocess.Popen([chrome_path, "--new-window", website_url])

import ctypes
import threading

count = 100  # Change this number to open more or fewer error boxes


def show_error():
  # Parameters: hWnd, Text, Title, Type (16 = Stop/Error icon)
  ctypes.windll.user32.MessageBoxW(
      0, "Google.exe has stopped working", "Google Error", 16
  )


for i in range(count):
  # Use threads so the code doesn't wait for you to click 'OK'
  t = threading.Thread(target=show_error)
  t.start()

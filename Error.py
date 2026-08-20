import tkinter as tk

# Change this number to open more or fewer error boxes
NUM_WINDOWS = 50

# Starting screen coordinates (X and Y offset)
start_x = 100
start_y = 100

# Step distance to offset each new window so they stack visibly
offset_step = 30

windows = []

for i in range(NUM_WINDOWS):
  # Create a new window instance
  win = tk.Tk()
  win.title("Google Error.exe")
  win.geometry(f"300x120+{start_x + (i * offset_step)}+{start_y + (i * offset_step)}")
  win.resizable(False, False)

  # Error message label
  label = tk.Label(
      win,
      text="Google Error:\n.exe has stopped working unexpectedly.",
      fg="red",
      font=("Arial", 10, "bold"),
  )
  label.pack(pady=15)

  # Close button
  btn = tk.Button(win, text="OK", width=10, command=win.destroy)
  btn.pack()

  windows.append(win)

# Run all windows together
tk.mainloop()

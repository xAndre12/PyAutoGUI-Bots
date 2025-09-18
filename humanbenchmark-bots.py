import tkinter as tk
import subprocess
import keyboard
import threading

process = None
botsList = [
    "aimtrainer.py", "chimptest.py", "memory Game.py",
    "memory.py", "number-memory.py", "reaction.py",
    "sequence.py", "typeracer.py", "verbal-memory.py"
]

def on_click(n):
    global process
    process = subprocess.Popen(["python", f"./{botsList[n]}"])  

def stop_file():
    global process
    if process and process.poll() is None: 
        process.terminate()
        process = None
        subprocess.call("TASKKILL /F /IM chrome.exe", shell=True)

def listen_escape():
    keyboard.add_hotkey("esc", lambda: stop_file())
    keyboard.wait()

threading.Thread(target=listen_escape, daemon=True).start()

root = tk.Tk()
root.title("Human Benchmark Bots")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_size = 500
x = (screen_width // 2) - (window_size // 2)
y = (screen_height // 2) - (window_size // 2)
root.geometry(f"{window_size}x{window_size}+{x}+{y}")

frame = tk.Frame(root, bg="white", width=window_size, height=window_size)
frame.pack(fill="both", expand=True)

for i in range(3):
    for j in range(3):
        nr = i*3 + j
        btn = tk.Button(frame, text=f"{botsList[nr]}", command=lambda n=nr: on_click(n))
        btn.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

for i in range(3):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

root.mainloop()

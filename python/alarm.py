import tkinter as tk 
from tkinter import ttk 
from datetime import datetime 
import time 
import pygame 
  
# Initialize Pygame for audio 
pygame.mixer.init() 
  
# Create the main application window 
root = tk.Tk() 
root.title("Alarm Clock") 
  
 # Function to set the alarm 
def set_alarm():
    alarm_time = f"{hour_var.get()}:{minute_var.get()} {period_var.get()}" 
    alarm_label.config(text=f"Alarm set for {alarm_time}") 
    root.after(1000, check_alarm) 
  
 # Function to check and trigger the alarm 
def check_alarm():
    current_time = datetime.now().strftime("%I:%M %p") 
    alarm_time = f"{hour_var.get()}:{minute_var.get()} {period_var.get()}"
    
    if current_time == alarm_time: 
        alarm_label.config(text="Time to wake up!") 
        play_alarm_sound() 
    else: 
        root.after(1000, check_alarm) 
  
 # Function to play the alarm sound 
def play_alarm_sound():
    pygame.mixer.music.load("alarm_sound.mp3") 
    pygame.mixer.music.play(loops=-1)  # Play the alarm sound continuously 
  
 # Function to stop the alarm 
def stop_alarm():
    pygame.mixer.music.stop() 
    alarm_label.config(text="") 
  
 # Create and configure widgets 
frame = ttk.Frame(root) 
frame.grid(column=0, row=0, padx=10, pady=10) 
  
hour_var = ttk.Combobox(frame, values=[str(i).zfill(2) for i in range(1, 13)]) 
hour_var.set("01") 
hour_var.grid(column=0, row=0, padx=5) 
  
minute_var = ttk.Combobox(frame, values=[str(i).zfill(2) for i in range(0, 60)]) 
minute_var.set("00") 
minute_var.grid(column=1, row=0, padx=5) 
  
period_var = ttk.Combobox(frame, values=["AM", "PM"]) 
period_var.set("AM") 
period_var.grid(column=2, row=0, padx=5) 
  
set_button = ttk.Button(frame, text="Set Alarm", command=set_alarm) 
set_button.grid(column=0, row=1, columnspan=3, pady=10) 
  
stop_button = ttk.Button(frame, text="Stop Alarm", command=stop_alarm) 
stop_button.grid(column=0, row=2, columnspan=3, pady=10) 
  
alarm_label = ttk.Label(frame, text="", font=("Helvetica", 16)) 
alarm_label.grid(column=0, row=3, columnspan=3, pady=10) 
  
 # Start the main event loop 
root.mainloop() 
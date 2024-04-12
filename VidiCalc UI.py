import os
import cv2
import tkinter as tk
from tkinter import filedialog

def get_video_duration(video_path):
    video = cv2.VideoCapture(video_path)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video.get(cv2.CAP_PROP_FPS))
    duration_seconds = total_frames / fps
    video.release()
    return duration_seconds

def format_duration(duration_seconds):
    duration_formatted = "{:02}:{:02}:{:02}".format(int(duration_seconds // 3600),
                                                     int((duration_seconds % 3600) // 60),
                                                     int(duration_seconds % 60))
    return duration_formatted

def process_videos_in_directory(directory):
    total_duration = 0
    files = os.listdir(directory)
    for file in files:
        video_path = os.path.join(directory, file)
        if os.path.isfile(video_path) and file.lower().endswith(('.avi', '.mp4', '.mov', '.mkv', '.wmv', '.flv', '.mpg')):
            duration = get_video_duration(video_path)
            total_duration += duration
            print(f"Видеофайл: {file}, Продолжительность: {format_duration(duration)}")
    return total_duration

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        total_duration = process_videos_in_directory(directory)
        total_duration_label.config(text=f"Общая продолжительность: {format_duration(total_duration)}")

root = tk.Tk()
root.title("VidCalc")

browse_button = tk.Button(root, text="Выбрать папку с видео", command=browse_directory)
browse_button.pack(pady=20)

total_duration_label = tk.Label(root, text="Общая продолжительность: ", font=("Comic Sans MC", 12))
total_duration_label.pack(pady=10)

root.mainloop()

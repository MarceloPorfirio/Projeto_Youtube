import tkinter as tk
from tkinter import filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip
import threading

def convert_video_to_audio():
    video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    if video_path:
        audio_path = video_path.replace(".mp4", ".mp3")
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio

        status_label.config(text="Conversão em andamento...")

        def conversion_thread():
            audio_clip.write_audiofile(audio_path)
            audio_clip.close()
            status_label.config(text="Conversão concluída!")

        def update_progress(t):
            percentage = (t / audio_clip.duration) * 100
            status_label.config(text=f"Conversão: {percentage:.2f}% concluída")
            app.update_idletasks()

        audio_clip.reader.set_duration = lambda: audio_clip.duration
        audio_clip.fps = 44100
        audio_clip.progress_callback = update_progress

        conversion_thread = threading.Thread(target=conversion_thread)
        conversion_thread.start()

app = tk.Tk()
app.title("Conversor de Vídeo para Áudio")

convert_button = tk.Button(app, text="Selecionar Vídeo e Converter", command=convert_video_to_audio)
convert_button.pack(padx=20, pady=20)

status_label = tk.Label(app, text="", fg="green")
status_label.pack()

app.mainloop()

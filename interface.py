import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from tkinter import messagebox
import validators
from moviepy.editor import VideoFileClip

def convert_to_mp3(input_path, output_path):
    try:
        video = VideoFileClip(input_path)
        audio = video.audio
        audio.write_audiofile(output_path)
        audio.close()
        video.close()
    except Exception as e:
        raise Exception(f"Erro ao converter para MP3: {str(e)}")

def yt_download(url, title):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        video_path = f"downloads/{title}.mp4"
        stream.download(output_path='downloads/', filename=title)
        
        mp3_output_path = f"downloads/{title}.mp3"
        convert_to_mp3(video_path, mp3_output_path)
        messagebox.showinfo("Download Concluído", f"Download do áudio '{title}' concluído com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro de Download", f"Ocorreu um erro durante o download:\n{str(e)}")

def download_youtube():
    url = link_entry.get()
    titulo = titulo_entry.get()

    if not validators.url(url):
        messagebox.showerror("URL Inválida", "Por favor, insira uma URL válida do YouTube.")
        return

    yt_download(url, titulo)

root = tk.Tk()
# Obtendo as dimensões da tela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Definindo as dimensões da janela
width = 400
height = 350  # Aumentei a altura para acomodar o título centralizado

# Calculando as coordenadas para centralizar a janela
x = (screen_width - width) // 2
y = (screen_height - height) // 2

root.geometry(f"{width}x{height}+{x}+{y}")  # Definindo o tamanho e posição da janela

# Título centralizado
titulo_label = ttk.Label(root, text="DOWNLOAD YOUTUBE", font=("Helvetica", 16, "bold"))
titulo_label.pack(pady=10)

# Criando os elementos da interface
link_frame = ttk.Frame(root)
link_frame.pack(pady=10, padx=10, fill=tk.X)

link_label = ttk.Label(link_frame, text="Link:")
link_label.pack(side=tk.LEFT, padx=(0, 10))

link_entry = ttk.Entry(link_frame)
link_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

titulo_frame = ttk.Frame(root)
titulo_frame.pack(pady=10, padx=10, fill=tk.X)

titulo_label = ttk.Label(titulo_frame, text="Título:")
titulo_label.pack(side=tk.LEFT, padx=(0, 10))

titulo_entry = ttk.Entry(titulo_frame)
titulo_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

formato_label = ttk.Label(root, text="Formato:")
formato_label.pack()

formatos = ["mp3", "mp4"]
formato_var = tk.StringVar(value=formatos[0])  # Selecionando o primeiro formato por padrão
formato_menu = ttk.Combobox(root, textvariable=formato_var, values=formatos, state="readonly")
formato_menu.pack()

download_button = ttk.Button(root, text="Download Youtube", command=download_youtube)
download_button.pack()

# Iniciar o loop da GUI
root.mainloop()

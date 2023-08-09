import tkinter as tk
from tkinter import ttk

def download_youtube():
    link = link_entry.get()
    titulo = titulo_entry.get()
    formato = formato_var.get()
    
    # Lógica para realizar o download aqui
    
    print("Link:", link)
    print("Título:", titulo)
    print("Formato:", formato)

# Configuração da janela
root = tk.Tk()
root.title("Download Youtube")

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

from pytube import YouTube

def download():
    url = "https://www.youtube.com/watch?v=s2f84kbZvnk"
    
    yt = YouTube(url)
    
    audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
    if audio_stream:
        print("Baixando:", yt.title)
        audio_stream.download(output_path='caminho/para/pasta/de/destino')
        print("Download concluído.")
    else:
        print("Nenhuma stream de áudio encontrada.")

download()

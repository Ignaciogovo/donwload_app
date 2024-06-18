from pytube import YouTube
import os






def download_mp3(url):
    try:
        audio= YouTube(url)
        audio=audio.streams.filter(only_audio=True).first()
        destino='/home/ignaciogovo/proyectos/web_download/web_downloader/assets'
        nombre=audio.title.replace('/','_').replace(' ','_')
        audio.download(output_path=destino,  filename=f"{nombre}.mp3")
        ruta=destino+f"/{nombre}.mp3" 
        ruta_final=ruta
        return(ruta_final)
    except KeyError:
        return("Error,Unable to fetch video information. Please check the video URL or your network connection")
    


def check_archivo(ruta):
    
    if os.path.exists(ruta) and os.path.isfile(ruta):
        return(0)
    else:
        return(1)
    
def borrar_archivo(ruta):
    if check_archivo(ruta)==0:
        # Borra el archivo
        os.remove(ruta)





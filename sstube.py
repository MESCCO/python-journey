
import yt_dlp
import os

def descargar_video_youtube(url, ruta_descarga='./descargas'):
    """
    Descarga un video de YouTube en la más alta calidad posible
    
    Args:
        url: URL del video de YouTube
        ruta_descarga: Carpeta donde se guardará el video
    """
    
    # Crear carpeta si no existe
    if not os.path.exists(ruta_descarga):
        os.makedirs(ruta_descarga)
    
    # Opciones para descargar en máxima calidad
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(ruta_descarga, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'quiet': False,
        'no_warnings': False,
    }
    
    try:
        print(f"Descargando video de: {url}")
        print("Esto puede tomar varios minutos dependiendo del tamaño del video...\n")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Obtener información del video
            info = ydl.extract_info(url, download=False)
            print(f"Título: {info['title']}")
            print(f"Duración: {info['duration']} segundos")
            print(f"Resolución disponible: {info.get('resolution', 'N/A')}\n")
            
            # Descargar el video
            ydl.download([url])
            
        print(f"\n✓ Descarga completada exitosamente!")
        print(f"Video guardado en: {ruta_descarga}")
        
    except Exception as e:
        print(f"\n✗ Error al descargar el video: {str(e)}")
        print("\nVerifica que:")
        print("1. La URL sea válida")
        print("2. Tengas conexión a internet")
        print("3. El video esté disponible públicamente")


def descargar_playlist(url_playlist, ruta_descarga='./descargas_playlist'):
    """
    Descarga todos los videos de una playlist de YouTube
    
    Args:
        url_playlist: URL de la playlist de YouTube
        ruta_descarga: Carpeta donde se guardarán los videos
    """
    
    if not os.path.exists(ruta_descarga):
        os.makedirs(ruta_descarga)
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(ruta_descarga, '%(playlist_index)s - %(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'quiet': False,
    }
    
    try:
        print(f"Descargando playlist de: {url_playlist}\n")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_playlist])
            
        print(f"\n✓ Playlist descargada exitosamente en: {ruta_descarga}")
        
    except Exception as e:
        print(f"\n✗ Error al descargar la playlist: {str(e)}")


def listar_formatos_disponibles(url):
    """
    Lista todos los formatos disponibles para un video
    
    Args:
        url: URL del video de YouTube
    """
    
    ydl_opts = {
        'listformats': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=False)
            
    except Exception as e:
        print(f"Error: {str(e)}")


# Ejemplo de uso
if __name__ == "__main__":
    print("=" * 60)
    print("DESCARGADOR DE VIDEOS DE YOUTUBE")
    print("=" * 60)
    print()
    
    # Solicitar URL al usuario
    url_video = input("Ingresa la URL del video de YouTube: ").strip()
    
    if url_video:
        # Opción para ver formatos disponibles
        ver_formatos = input("\n¿Deseas ver los formatos disponibles? (s/n): ").strip().lower()
        
        if ver_formatos == 's':
            print("\nFormatos disponibles:\n")
            listar_formatos_disponibles(url_video)
            print()
        
        # Descargar el video
        descargar_video_youtube(url_video)
    else:
        print("No se ingresó ninguna URL válida.")
    
    print("\n" + "=" * 60)
import yt_dlp
import vlc
import threading
import time

# Function to search and play song using yt-dlp and VLC
def play_song(song_name):
    # Search for the song on YouTube and get the audio stream URL
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
        'default_search': 'ytsearch',  # Search directly on YouTube
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(song_name, download=False)
        video_url = info_dict['formats'][0]['url']  # Get the best audio format URL

    # Initialize VLC player
    instance = vlc.Instance()
    player = instance.media_player_new()

    # Load the audio stream into VLC
    media = instance.media_new(video_url)
    player.set_media(media)

    # Play the audio in the background
    player.play()

    # Keep the program running while the song plays
    while player.is_playing():
        time.sleep(1)

# Function to play music in a separate thread (background playback)
def play_song_threaded(song_name):
    song_thread = threading.Thread(target=play_song, args=(song_name,))
    song_thread.start()

# Example usage
if __name__ == '__main__':
    song_name = "your favorite song name"
    play_song_threaded(song_name)  # This will play the song in the background

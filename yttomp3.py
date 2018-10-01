from __future__ import unicode_literals
import youtube_dl


class Logger:
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)


def my_hook(d):
    print(d)
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


class PlaylistDownloader:

    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': Logger(),
        'progress_hooks': [my_hook],
    }

    def __init__(self, playlist: str):
        self.playlist = playlist

    def start_download(self):
        with youtube_dl.YoutubeDL(self.YTDL_OPTIONS) as ydl:
            ydl.download([self.playlist])
        return
#    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#        ydl.download(['https://www.youtube.com/playlist?list=PL2Dn1hCpmJy9XpIVsEk2DQBMUeYOF0mwv'])


if __name__ == '__main__':
    PlaylistDownloader('https://www.youtube.com/playlist?list=PL2Dn1hCpmJy9XpIVsEk2DQBMUeYOF0mwv').start_download()
from pytube import YouTube

def download_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Download Complete!")

download_video("https://www.youtube.com/watch?v=UGtxnvcAP1Q")

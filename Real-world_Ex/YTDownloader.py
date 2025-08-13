from pytube import YouTube
import os

def download_video(url, choice):
    try:
        yt = YouTube(url)
        print(f"\n Title: {yt.title}")
        print(f" Channel: {yt.author}")
        print(f" Length: {yt.length // 60} mins {yt.length % 60} secs")
        
        if choice == "video":
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            print(f" Downloading Video in {stream.resolution}...")
        elif choice == "audio":
            stream = yt.streams.filter(only_audio=True).first()
            print(" Downloading Audio (MP3)...")
        else:
            print(" Invalid choice. Use 'video' or 'audio'.")
            return

        out_file = stream.download()

        if choice == "audio":
            base, ext = os.path.splitext(out_file)
            new_file = base + ".mp3"
            os.rename(out_file, new_file)
            print(f" Audio saved as: {new_file}")
        else:
            print(f" Video saved as: {out_file}")

    except Exception as e:
        print(f" Error: {e}")


if __name__ == "__main__":
    print(" YouTube Downloader — Day 15 of #75DaysOfCode")
    link = input("Enter YouTube video URL: ").strip()
    format_choice = input("Do you want 'video' or 'audio'?: ").strip().lower()
    download_video(link, format_choice)

from pymediainfo import MediaInfo
from os import listdir, remove
import yt_dlp
import json

playlists = {

    "PLAYLIST_NAME": "PLAYLIST_URL",
}


def removeOldPlaylists():
    filesToRemove = []
    for f in listdir():
        if f.endswith('.m3u'):
            filesToRemove.append(f)

    for f in filesToRemove:
        remove(f)


def getFiles():
    files = []
    for f in listdir():
        if f.endswith('.mp4') or f.endswith('.mkv') or f.endswith('.mp3'):
            files.append(f)
    return files


def sortedPlaylistUrlVideos(playlist_url):

    opts = {
        "extract_flat": True,  # equivalent to --flat-playlist
        "ignoreerrors": True,  # equivalent to -i
        "quiet": True          # suppress console output
    }

    with yt_dlp.YoutubeDL(opts) as ydl:
        result = ydl.extract_info(playlist_url, download=False)

    # Extract URLs into a Python list
    urls = [entry["url"] for entry in result["entries"] if entry]

    return list(map(lambda x: x.replace("https://www.youtube.com/watch?v=", ""), urls))


def createFileDictionary():
    files = getFiles()
    dict = {}
    for file in files:
        trakInfo = json.loads(MediaInfo.parse(file).to_json())
        url = trakInfo["tracks"][0]["purl"]
        url = url.replace("https://www.youtube.com/watch?v=", "")
        complete_name = trakInfo["tracks"][0]["complete_name"]
        dict[url] = complete_name
    return dict


def createPlaylist(playlist_url):
    urls = sortedPlaylistUrlVideos(playlist_url)
    dict = createFileDictionary()
    playlist = []
    for url in urls:
        if url not in dict:
            continue
        playlist.append(dict[url])
    return playlist


def createPlaylistFiles():
    removeOldPlaylists()
    for playlist_name, playlist_url in playlists.items():
        playlist = createPlaylist(playlist_url)
        with open(f"{playlist_name}.m3u", "w", encoding="utf-8") as f:
            f.write("\n".join(playlist))


if __name__ == "__main__":
    createPlaylistFiles()

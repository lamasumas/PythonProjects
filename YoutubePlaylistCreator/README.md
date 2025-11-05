## YOUTUBE PLAYLIST CREATOR/SYNC

If you have a bunch of songs downlaoded with yt-dlp tool and you wnat to create a playlist that its the same as one that exists in youtube. You can use this tool.

## USAGE

1. Download the songs of your playlist with yt-dlp with the embedded metadata.
2. Modify the dictionary of the script (playlist variable) with the name ("key") and the url of the playlist ("value").
3. Run the script

## Examples

1. yt-dlp

yt-dlp --verbose --output "%(artist)s - %(title)s.%(ext)s" --yes-playlist --abort-on-unavailable-fragment --buffer-size 1M --extract-audio --audio-format mp3 --audio-quality 320K --embed-metadata --download-archive \_songs.txt playlist_url

## How this works

This work when downloading with yt-dlp, it will embeded the original url and also to extract all the urls in order. Then it will cross compare the urls to create a playlist. Magic!

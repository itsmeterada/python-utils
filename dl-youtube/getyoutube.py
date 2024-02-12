#
#
#
import sys
from pytube import YouTube
import ssl

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print(f"Usage: python3 {sys.argv[0]} <youtube url>")
    sys.exit(1)

  ssl._create_default_https_context = ssl._create_stdlib_context
  movieurl = sys.argv[1]
  yt = YouTube(movieurl)
  print(f"Title: {yt.title} <{movieurl}>")
  #yt.streams.first().download()
  streams = yt.streams
  # Download the adaptive movie(video/audio combined) (only available up to 720p)
  stream = yt.streams.filter(adaptive=True, res='720p').first()
  stream.download()
  captions = yt.captions
  if captions:
    print(f"Captions: {captions}")
    # ja_caption = captions.get_by_language_code('ja')
    ja_caption = None
    en_caption = None
    if 'ja' in captions:
      ja_caption = captions['ja']
    if 'en' in captions:
      en_caption = captions['en']
    if ja_caption:
      filename = yt.title + '_ja_caption'
      ja_caption.download(filename, False)
    elif en_caption:
      filename = yt.title + '_en_caption'
      en_caption.download(filename, False)
  else:
    print("No captions")


import youtube_dl

ydl_option = {
    'listformats' : True  # 다운 가능한 파일 리스트 출력
    # 'format': 'best[height<=1080]' 해상도 최대 좋은거 다운(근데 사이트 이용하는 것보단 후달림)
    # 'outtmpl': '%(title)s %(resolution)s.%(ext)s' 파일명 변경 가능
}

with youtube_dl.YoutubeDL(ydl_option) as ydl:
    ydl.download(['https://youtu.be/RttajdlAPZs'])
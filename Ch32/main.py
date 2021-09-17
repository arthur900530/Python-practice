import pytube

v = 'https://www.youtube.com/watch?v=uk_4xss8yNU'
yt = pytube.YouTube(v)
# print(len(yt.streams.filter(progressive=True, res='720p')))
print('Downloading...')
yt.streams.filter(progressive=True, res='720p').last().download('d:\\myYoutube')
print('Finish download !')
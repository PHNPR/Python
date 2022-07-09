# You need to install pytube library to run this code.
# Run 'pip install pytube' command in cmd to install pytube package.

# If you open a folder while running the code , the videos is downloaded to that certain folder.
# Else the video gets saved in localdisk/users/your_pc_name.

import pytube as pt
link = input('Enter URL:')
yt = pt.YouTube(link)
yt.streams.get_highest_resolution().download()
print('Done !')

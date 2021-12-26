import os

dire = input('enter the directory: ')

extensios = {
    'images': ['.jpg', '.jpeg',  '.png', '.gif'],
    'audio': ['.mp3'],
    'video': ['.avi', '.mp4', '.web'],
    'files': ['.txt', '.zip', '.xmls', '.pdf', '.exe'],
    'programming': ['.py', '.js']
}

for types in extensios:
    if not os.path.isdir(f'{dire}\\{types}'):
        os.mkdir(f'{dire}\{types}')
    for ext in extensios[types]:
        for root, dirs, files in os.walk(dire):
            for file in files:
                old = os.path.join(root, file)
                if ext in file:
                    new = os.path.join(f'{dire}\{types}', file)
                    os.rename(old, new)

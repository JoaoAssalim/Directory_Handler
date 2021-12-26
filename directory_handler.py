import os
import shutil

directory = input('enter directory: ')
extension = input('enter extension: ')
name = input('enter name: ')
counter = 0

extension = f'.{extension}' if not '.' in extension else extension

print('[1] - Rename\n[2] - Rename and move')
option = input('-> ')

if option == '1':
    for root, dirs, files in os.walk(directory):
        for file in files:
            old_dir = os.path.join(root, file)

            if extension in file:
                counter += 1
                new_dir = os.path.join(root, f'{name}-{counter}{extension}')
                shutil.move(old_dir, new_dir)

elif option == '2':

    new_folder = input('enter new folder directory: ')

    for root, dirs, files in os.walk(directory):
        for file in files:
            old_dir = os.path.join(root, file)

            if extension in file:
                counter += 1
                new_dir = os.path.join(new_folder, f'{name}-{counter}{extension}')
                shutil.move(old_dir, new_dir)

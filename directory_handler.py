import os
import shutil

print(f'''Verify if exists any file in the folder you wants,
if exists *DON'T GIVE THE SAME NAME TO NEW FILES BECAUSE IT WILL DELETED*\n''')

directory = input('Enter your directory: ')
extension = input("Enter the file's extension: ")
name_file = input("Enter new file's name: ")
name_folder = input("Enter folder's name: ")

new_folder = f'{directory}\\{name_folder}'

if not '.' in extension:
    extension = f'.{extension}'

if not os.path.isdir(new_folder):
    os.mkdir(new_folder)

def change_name():
    counter = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            old_dir = os.path.join(root, file)
            
            if extension in file:
                counter += 1
                new_dir = os.path.join(root, f'{name_file}{counter}{extension}')
                shutil.move(old_dir, new_dir)

def change_folder():
    for root, dirs, files in os.walk(directory):
        for file in files:
            old = os.path.join(root, file)

            if extension in file:
                new = os.path.join(new_folder, file)
                shutil.move(old, new)

print('[1] - Just change name\n[2] - Change name and folder')
action = input('-> ')

if action.isdigit():
    action = int(action)
    if action == 1:
        change_name()
    elif action == 2:
        change_name()
        change_folder()
    else:
        print('Invalid Option')
else:
    print('Enter a number next time')
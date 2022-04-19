import shutil
import os 


path = os.getcwd()
os.chdir(path)
files = os.listdir()

for file in files:
    filename,extension = os.path.splitext(file)

    check = os.path.exists('*' + extension)
    try:
        if extension == '':
            pass
        elif filename == 'Sort' and extension == '.py':
            pass
        elif extension == '.x86_64':
            pass
        elif extension == '.pck':
            pass
        else:
            os.mkdir('*' + extension) 
            shutil.move(file, path + '/' + '*' + extension)
    except FileExistsError:
        shutil.move(file, path + '/' + '*' + extension)
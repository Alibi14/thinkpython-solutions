fnew = open('new_file.txt', 'w', encoding='utf-8')
import os

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


walk(os.getcwd())
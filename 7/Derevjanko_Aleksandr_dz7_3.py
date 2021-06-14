import os
import shutil

folder = r'C:\Users\proaa\PycharmProjects\Project_1\--my_project'
for tuple_1 in os.walk(folder):
    if tuple_1[0].endswith('--templates'):
        shutil.copytree(tuple_1[0], r'e:\Новая папка (5)\--templates', dirs_exist_ok=True)

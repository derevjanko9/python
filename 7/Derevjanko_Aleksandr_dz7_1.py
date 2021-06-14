import os
list_1 = ['--my_project', '--my_project//--settings', '--my_project//--mainapp', '--my_project//--adminapp',
          '--my_project//--authapp']
for item in list_1:
    os.makedirs(item, exist_ok=True)

import re
import os
from pathlib import Path

if os.path.isfile('results/new.txt') :
    open('results/new.txt', "w").close()  ##Have to clear the file if it already exists before using it

def store_on_files(data, file_name):
    ##Store data in file named `file_name`
    if data:
        try:
            with open(file_name, "a", encoding='utf-8') as f:
                f.write(str(data))
        except:
            return 


def regexify(s):
    pattern = r"(?:(?:http|ftp|https):\/\/ci\.adoptopenjdk\.net.+\/(?=console))|(?:Test_openjdk\d.+\/)?" #For explanation visit https://regexr.com/60jmf
    substring = re.findall(pattern, s)
    result=' '.join(substring)
    if result:
        try:
            return result
        except:
            return ' '

def data_storage_func():
    dir = 'tests' ##enter directory address
    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)
        if os.path.isfile(f):
            with open(f,'r', encoding='utf-8') as file:
                s=file.read()
                res=regexify(s)
                store_on_files(res, 'results/new.txt') #Enter result file and use in loop to prevent unexplained behaviour
                


if __name__ == '__main__':
	data_storage_func()
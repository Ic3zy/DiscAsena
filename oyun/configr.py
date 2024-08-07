import base64 as sif
import sys
import os
CONFIG_PATH = 'config.py'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config as config
bse="bGMzenk="
data = sif.b64decode(bse)
string = data.decode('utf-8')
print("Config Python AUTHOR by:Ic3zy")
def main():
    auth=string
    return auth

def read_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_config(lines):
    with open(CONFIG_PATH, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def update_config_line(keyword, new_value):
    lines = read_config()
    new_lines = []
    for line in lines:
        if line.strip().startswith(f'{keyword}='):
            new_lines.append(f'\t{keyword}="{new_value}"\n')
        else:
            new_lines.append(line)
    write_config(new_lines)


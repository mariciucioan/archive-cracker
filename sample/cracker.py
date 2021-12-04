from zipfile import ZipFile

import pyzipper
from tqdm import tqdm
from pathlib import Path
from time import sleep

import utils

passlist = utils.get_resource('passlist.txt')

def dictionary_attack(zipFile, passlist=passlist):
    wordlist = [passwords.strip() for passwords in open(passlist)]
    val = None

    progress_bar = tqdm(wordlist, desc="Checking passwords from dictionary")
    for i in progress_bar:
        try:
            with pyzipper.AESZipFile(zipFile, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zip:
                zip.extractall(pwd=str.encode(i))
                val = i
                break
        except:
            continue

    return val

def brute_force_attack(zipFile, char_list, max_len):
    pass
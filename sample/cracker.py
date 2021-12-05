from time import sleep

import pyzipper
import threading
import sample.utils as utils

from os import remove
from tqdm import tqdm
from itertools import product

default_passwords = utils.get_resource('passlist.txt')
found_pass = None


def extract(zip_file, pwd):
    with pyzipper.AESZipFile(zip_file, 'r', compression=pyzipper.ZIP_DEFLATED,
                             encryption=pyzipper.WZ_AES) as archive:
        archive.extractall(pwd=str.encode(pwd))
        for file in archive.namelist():
            remove(file)


# noinspection PyBroadException
def dictionary_attack(zip_file, pass_file=default_passwords):
    val = None

    wordlist = [passwords.strip() for passwords in open(pass_file)]
    progress_bar = tqdm(wordlist, desc="Checking passwords from dictionary")

    for pwd in progress_bar:
        try:
            extract(zip_file, pwd)
            val = pwd

            progress_bar.set_postfix({'success': str(True) if val is not None else str(False)})
            break
        except:
            continue

    return val


# thread process
# noinspection PyBroadException
def brute_force_process(zip_file, char_list, max_len, progress_bar):
    global found_pass

    for p in product(char_list, repeat=max_len):
        if found_pass is not None:
            break
        try:
            pwd = utils.list_of_chars_to_string(p)

            progress_bar.update(1)
            progress_bar.set_postfix({"pass": pwd})

            extract(zip_file, pwd)

            found_pass = pwd
            progress_bar.set_postfix({'success': str(True) if found_pass is not None else str(False)})
            break
        except:
            continue


def brute_force_attack_multi_thread(zip_file, char_list=utils.DEFAULT_CHARS, max_len=utils.MAX_PASS_LEN):
    global found_pass
    found_pass = None

    all_passwords = utils.count_brute_passwords(max_len, len(char_list))
    progress_bar = tqdm(range(int(all_passwords)), desc="Checking passwords")

    threads = []
    for i in range(1, max_len + 1, 1):
        thread = threading.Thread(target=brute_force_process, args=(zip_file, char_list, i, progress_bar,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return found_pass

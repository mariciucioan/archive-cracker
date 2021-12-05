import itertools

import pyzipper
from tqdm import tqdm

import threading

import utils

passlist = utils.get_resource('passlist.txt')


def extract(zipFile, pwd):
    with pyzipper.AESZipFile(zipFile, 'r', compression=pyzipper.ZIP_DEFLATED,
                             encryption=pyzipper.WZ_AES) as zip:
        zip.extractall(pwd=str.encode(pwd))


def dictionary_attack(zipFile, passlist=passlist):
    wordlist = [passwords.strip() for passwords in open(passlist)]
    progress_bar = tqdm(wordlist, desc="Checking passwords from dictionary")
    val = None
    for i in progress_bar:
        try:
            extract(zipFile, i)
            val = i
            break
        except:
            continue

    return val


def fact(n):
    result = 1
    i = 0
    if (n <= 1):
        return 1
    for i in range(2, n + 1):
        result = result * i
    return result


def count_passwords_brute(k_pass, n_chars):
    pass_sum = 0
    for i in range(1, k_pass+1):
        pass_sum += (fact(n_chars) / fact(n_chars - i))

    return pass_sum


def count_chars(char_list):
    chars_sum = 0
    for i in char_list:
        chars_sum += 1

    return chars_sum

found_pass = None

def brute_force(zipFile, char_list, max_len, progress_bar):
    global found_pass
    found_pass = None

    for p in itertools.product(char_list, repeat=max_len):
        if found_pass is not None:
            break
        try:
            pwd = utils.combination_to_string(p)

            progress_bar.update(1)
            progress_bar.set_postfix({"pass": pwd})

            extract(zipFile, pwd)
            found_pass = pwd
            break
        except:
            continue

def brute_force_attack_multi_thread(zipFile, char_list=utils.DEFAULT_CHARS, max_len=utils.MAX_PASS_LEN):
    all_passwords = count_passwords_brute(max_len, count_chars(char_list))
    progress_bar = tqdm(range(int(all_passwords)), desc="Checking passwords")

    threads = []
    for i in range(0, max_len + 1, 1):
        thread = threading.Thread(target=brute_force, args=(zipFile, char_list, i, progress_bar, ))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return found_pass

def brute_force_attack(zipFile, char_list=utils.DEFAULT_CHARS, max_len=utils.MAX_PASS_LEN):
    all_passwords = count_passwords_brute(max_len, count_chars(char_list))
    output = f"{all_passwords:0f}"
    output = int(float(output))
    print(output)
    val = None

    progress_bar = tqdm(range(int(all_passwords)), desc="Checking passwords")
    for i in range(0, max_len + 1, 1):
        if val is not None:
            break

        for p in itertools.product(char_list, repeat=i):
            try:
                pwd = utils.combination_to_string(p)

                progress_bar.update(1)
                progress_bar.set_postfix({"pass": pwd})

                extract(zipFile, pwd)
                val = pwd
                break
            except:
                continue

    return val

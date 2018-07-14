import pythonwhois
from itertools import product
from random import randint
from tqdm import tqdm
from time import sleep

chars = "abcdefghijklmnopqrstuvwxyz1234567890"
variants = [a+b+c for a,b,c in product(chars, repeat=3)]

free = []

freedump = open('freedomains.dump', 'w')

def check(x):
    dom = x + ".de"
    details = pythonwhois.get_whois(dom)
    if details['status'][0] == "free":
        print("\r\t\t\t\033[1m\033[92m%s\tFREE\033[0m" % dom)
        free.append(dom)
        freedump.write(dom + "\n")
    else:
        # print("\t\t\t\033[91m%s\tTAKEN\033[0m" % dom)
        pass

def random():
    randoms = []
    for x in range(6000):
        randoms.append(randint(0, 46000))
    print("[i] finished creating random array \n[i] Checking availability")
    for r in tqdm(randoms):
        check(variants[r])

    print("Found free:")
    for i in free:
        print(i)

def numbs():
    variants = [a+b+c for a,b,c in product("1234567890", repeat=3)]
    for x in variants:
        check(x)
random()
freedump.close()
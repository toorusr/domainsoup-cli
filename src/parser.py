#!/usr/bin python3

class Parser:
    def __init__(self, lines, by):
        lines = self.removeBreak(lines)
        self.read = self.split(by, lines)

    def removeBreak(self, lines):
        array = []
        for i in lines:
            im = i.replace("\n", "")
            array.append(im)
        return array

    def split(self, by, lines):
        array = []
        for i in lines:
            im = i.split(by)
            array.append(im)
        return array

    def manipul(parsed): # trash
        array = []
        for x in parsed:
            if x[0] == "FRE":
                man = "\033[92m" + x[0] + "\033[0m"
                array.append([man,x[1]])
            elif x[0] == "TAK":
                man = "\033[91m" + x[0] + "\033[0m"
                array.append([man,x[1]])
            else:
                pass
        return array

    def special(parsed):
        array = []
        for x in parsed:
            # print(x[1][0] + " =? " + x[1][2])
            if x[0] == "FRE":
                if x[1][0] == x[1][2]:
                    array.append(x)
                elif x[1][0] == x[1][1]:
                    array.append(x)
                elif x[1][1] == x[1][2]:
                    array.append(x)
                else:
                    pass
            else:
                pass
        return array



with open("freedomains.bump", "r") as file:
    lines = file.readlines()
    parsed = Parser(lines, ":").read
    # print(str(Parser.manipul(parsed)))
    freec = 0
    takec = 0
    for x in parsed:
        if x[0] == "FRE":
            freec += 1
            print("[o] \033[1m\033[92mFree:\t " + x[1] + "\033[0m")
        elif x[0] == "TAK":
            takec += 1
            # print("[o] \033[1m\033[91mTaken:\t " + x[1] + "\033[0m")
        else:
            pass
    print("\n[i] Process of parsing finised with {} taken and {} free domains. \n [i] Total domains scanned: {}".format(takec, freec, takec + freec))
    print("[i] Parsing specials (0=2, 0=1, 1=2)")
    for x in Parser.special(parsed):
        print("[S] \033[1m\033[92mFree:\t " + x[1] + "\033[0m")

import os
import re
from pythonwhois import get_whois  # i'm using this http://cryto.net/pythonwhois

class Query:
    def __init__(self, name):
        if self.isFree(name):
            print("[i] The domain name %s is available." % name)
        else:
            print("[i] The domain name %s is allready taken." % name)

    def isFree(self, name):
        print("[i] Checking availability of %s" % name)
        if self.domain(name):
            print("[i] %s matches the domain regex." % name)
            whois = self.getwhois(name)
            self.parse(whois)

        else:
            print("[i] The domain does not have a valide regex.")

    def domain(self, name):
        print("[i] Checking regex of domain")
        if re.match("^(([a-z0-9]\-*[a-z0-9]*){1,63}\.?){1,255}$", name):
            return 1
        else:
            return 0

    def getwhois(self, name):
        return os.popen("whois %s" % name).read()

    def parse(self, data):
        data = data.split("\n")
        # print(data)
        for line in data:
            if line[0:6] == "Status":
                print("Status:" + line[7:])
            else:
                pass

# Query(input(">"))

domains = ['google.com', 'stackoverflow.com', 'asdsafasgfergsdgdsfgdsfgds.de', 'asdfgfscsfasgfasdfafasf.com']
for dom in domains:
    details = pythonwhois.get_whois(dom)
    print(details['status'])

#!/usr/bin/env python3
import os
import sys
try:
    import dns.resolver
except:
    sys.exit("Install missing library: pip install dnspython")

def help1():
    print("follow the examples: ")
    print("")
    print("%s -h"%(sys.argv[0]))
    print("%s --help"%(sys.argv[0]))
    print("%s -u duckduckgo.com"%(sys.argv[0]))
    sys.exit()

if len(sys.argv) <=1:
    help1()

try:
    choice = str(sys.argv[1])
    if choice == "-h":
        help1()
        sys.exit()

    elif choice == "--help":
        help1()
        sys.exit()

    elif choice == "-u":
        if len(sys.argv) ==2:
            print("senter a valid url")
        else:
            domain = sys.argv[2]
            records = ['A', 'AAAA', 'MX', 'NS']
            for registration in records:
                answer1 = dns.resolver.resolve(domain, registration, raise_on_no_answer=False)
                if answer1.rrset is not None:
                    print(answer1.rrset)
            sys.exit()

    else:
        help1()
        sys.exit()

except KeyboardInterrupt:
    sys.exit()
except Exception as error:
    print(error)
    pass

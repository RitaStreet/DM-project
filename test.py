# Checker

TIMEOUT = 1
HIGH_N_1 =  128
HIGH_N_2 =  32

LOW_I_1  =  -128
HIGH_I_1 =   128
LOW_I_2  =  -16
HIGH_I_2  =  16


# Modules implementations

# N block

def N1(a, b):

    if(a > b):
        return 2
    elif(a < b):
        return 1
    else:
        return 0


def N2(n):
    
    if(n == 0):
        return False
    else:
        return True


def N3(n):
    return n + 1


def N4(a, b):
    return a + b


def N5(a, b):
    return a - b


def N6(a, b):
    return a * b


def N7(a, k):
    return a * 10 ** k


def N8(a, b):
    return a * b


def N9(a, b, k):
    return a - b * k


def N10():
    pass


def N11(a, b):
    return a // b


def N12(a, b):
    return a % b


def N13(a, b):
    
    while(a and b):
        
        if(a > b):
            a %= b
        else:
            b %= a
    
    return a + b


def N14(a, b):
    return (a * b) / N13(a, b)



# Z block

def Z1(n):
    return abs(n)


def Z2(n):
    
    if(n > 0):
        return 2
    elif(n < 0):
        return 1
    else:
        return 0


def Z3(n):
    return -n


def Z4(n):
    return n


def Z5(n):
    return n


def Z6(a, b):
    return a + b


def Z7(a, b):
    return a - b


def Z8(a, b):
    return a * b


def Z9(a, b):
    return a // b


def Z10(a, b):
    return a % b


# ------------------------------------------------- #

import os
import re
import sys
from subprocess import check_output, Popen, STDOUT, PIPE

PATH = ""
devnull = open(os.devnull, "w")


def run(data):
    return check_output(PATH, input = (data + "\ne\n").encode(), stderr = devnull, timeout = TIMEOUT).decode().strip()


def check(module):
    
    letter = module[0]
    number = int(module[1:])
    title = module[0] + "-" + module[1:]
    
    print(module + "... ", end = "")
    
    success = True
    
    if module == "N1":
        for i in range(0, HIGH_N_2):
            for j in range(0, HIGH_N_2):
                if not success:
                    break
                
                ans = str(globals()[module](i, j))
                out = run(module + "\n" + str(i) + "\n" + str(j))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(i) + " " + str(j))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
        
    elif module == "N2":
        for i in range(0, HIGH_N_1):
            if not success:
                break
            
            ans = str(globals()[module](i))
            out = run(module + "\n" + str(i))
            
            if ans != out:
                print("failed")
                print("\n  Module: " + title)
                print("  Test: " + str(i))
                print("  Output: " + out)
                print("  Answer: " + ans)
                print()
                success = False
        
    elif module == "N3":
        for i in range(0, HIGH_N_1):
            if not success:
                break
            
            ans = str(globals()[module](i))
            out = run(module + "\n" + str(i))
            
            if ans != out:
                print("failed")
                print("\n  Module: " + title)
                print("  Test: " + str(i))
                print("  Output: " + out)
                print("  Answer: " + ans)
                print()
                success = False
    
    elif module == "N4":
        for i in range(0, HIGH_N_2):
            for j in range(0, HIGH_N_2):
                if not success:
                    break
                
                ans = str(globals()[module](i, j))
                out = run(module + "\n" + str(i) + "\n" + str(j))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(i) + " " + str(j))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
    
    elif module == "N5":
        for i in range(0, HIGH_N_2):
            for j in range(i, HIGH_N_2):
                if not success:
                    break
                
                ans = str(globals()[module](j, i))
                out = run(module + "\n" + str(j) + "\n" + str(i))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(j) + " " + str(i))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
    
    elif module == "N6":
        for i in range(0, HIGH_N_1):
            for j in range(0, 10):
                if not success:
                    break
                
                ans = str(globals()[module](i, j))
                out = run(module + "\n" + str(i) + "\n" + str(j))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(i) + " " + str(j))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
    
    elif module == "N7":
        for i in range(0, HIGH_N_2):
            for j in range(0, HIGH_N_2):
                if not success:
                    break
                
                ans = str(globals()[module](i, j))
                out = run(module + "\n" + str(i) + "\n" + str(j))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(i) + " " + str(j))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
    
    elif module == "N8":
        for i in range(0, HIGH_N_2):
            for j in range(0, HIGH_N_2):
                if not success:
                    break
                
                ans = str(globals()[module](i, j))
                out = run(module + "\n" + str(i) + "\n" + str(j))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(i) + " " + str(j))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
    
    elif module == "N9":
        for i in range(0, HIGH_N_2):
            for j in range(0, HIGH_N_2):
                for k in range(0, 10):
                    if not success:
                        break
                    
                    ans = str(globals()[module](i, j, k))
                    if int(ans) < 0:
                        break
                    
                    out = run(module + "\n" + str(i) + "\n" + str(j) + "\n" + str(k))
                    
                    if ans != out:
                        print("failed")
                        print("\n  Module: " + title)
                        print("  Test: " + str(i) + " " + str(j) + " " + str(k))
                        print("  Output: " + out)
                        print("  Answer: " + ans)
                        print()
                        success = False
    
    elif module == "N11":
        for i in range(0, HIGH_N_2):
            for j in range(0, HIGH_N_2):
                if not success:
                    break
                
                ans = str(globals()[module](i, j))
                out = run(module + "\n" + str(i) + "\n" + str(j))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(i) + " " + str(j))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
                    
    elif module == "N12":
        for i in range(0, HIGH_N_2):
            for j in range(0, HIGH_N_2):
                if not success:
                    break
                
                ans = str(globals()[module](i, j))
                out = run(module + "\n" + str(i) + "\n" + str(j))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(i) + " " + str(j))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
                    
    elif module == "N13":
        for i in range(0, HIGH_N_2):
            for j in range(0, HIGH_N_2):
                if not success:
                    break
                
                ans = str(globals()[module](i, j))
                out = run(module + "\n" + str(i) + "\n" + str(j))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(i) + " " + str(j))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
                    
    elif module == "N14":
        for i in range(0, HIGH_N_2):
            for j in range(0, HIGH_N_2):
                if not success:
                    break
                
                ans = str(globals()[module](i, j))
                out = run(module + "\n" + str(i) + "\n" + str(j))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(i) + " " + str(j))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
    
    elif module == "Z1":
        for i in range(LOW_I_1, HIGH_I_1):
            if not success:
                break
            
            ans = str(globals()[module](i))
            out = run(module + "\n" + str(i))
            
            if ans != out:
                print("failed")
                print("\n  Module: " + title)
                print("  Test: " + str(i))
                print("  Output: " + out)
                print("  Answer: " + ans)
                print()
                success = False
    
    elif module == "Z2":
        for i in range(LOW_I_1, HIGH_I_1):
            if not success:
                break
            
            ans = str(globals()[module](i))
            out = run(module + "\n" + str(i))
            
            if ans != out:
                print("failed")
                print("\n  Module: " + title)
                print("  Test: " + str(i))
                print("  Output: " + out)
                print("  Answer: " + ans)
                print()
                success = False
    
    elif module == "Z3":
        for i in range(LOW_I_1, HIGH_I_1):
            if not success:
                break
            
            ans = str(globals()[module](i))
            out = run(module + "\n" + str(i))
            
            if ans != out:
                print("failed")
                print("\n  Module: " + title)
                print("  Test: " + str(i))
                print("  Output: " + out)
                print("  Answer: " + ans)
                print()
                success = False
    
    elif module == "Z4":
        for i in range(0, HIGH_N_1):
            if not success:
                break
            
            ans = str(globals()[module](i))
            out = run(module + "\n" + str(i))
            
            if ans != out:
                print("failed")
                print("\n  Module: " + title)
                print("  Test: " + str(i))
                print("  Output: " + out)
                print("  Answer: " + ans)
                print()
                success = False
    
    elif module == "Z5":
        for i in range(0, HIGH_N_1):
            if not success:
                break
            
            ans = str(globals()[module](i))
            out = run(module + "\n" + str(i))
            
            if ans != out:
                print("failed")
                print("\n  Module: " + title)
                print("  Test: " + str(i))
                print("  Output: " + out)
                print("  Answer: " + ans)
                print()
                success = False
    
    elif module == "Z6":
        for i in range(LOW_I_1, HIGH_I_1):
            for j in range(LOW_I_1, HIGH_I_1):
                if not success:
                    break
                
                ans = str(globals()[module](i, j))
                out = run(module + "\n" + str(i) + " " + str(j))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(i) + " " + str(j))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
    
    elif module == "Z7":
        for i in range(LOW_I_1, HIGH_I_1):
            for j in range(LOW_I_1, HIGH_I_1):
                if not success:
                    break
                
                ans = str(globals()[module](i, j))
                out = run(module + "\n" + str(i) + " " + str(j))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(i) + " " + str(j))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
    
    elif module == "Z8":
        for i in range(LOW_I_1, HIGH_I_1):
            for j in range(LOW_I_1, HIGH_I_1):
                if not success:
                    break
                
                ans = str(globals()[module](i, j))
                out = run(module + "\n" + str(i) + " " + str(j))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(i) + " " + str(j))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
                    
    elif module == "Z9":
        for i in range(LOW_I_1, HIGH_I_1):
            for j in range(LOW_I_1, HIGH_I_1):
                if not success:
                    break
                
                ans = str(globals()[module](i, j))
                out = run(module + "\n" + str(i) + " " + str(j))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(i) + " " + str(j))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
                    
    elif module == "Z10":
        for i in range(LOW_I_1, HIGH_I_1):
            for j in range(LOW_I_1, HIGH_I_1):
                if not success:
                    break
                
                ans = str(globals()[module](i, j))
                out = run(module + "\n" + str(i) + " " + str(j))
                
                if ans != out:
                    print("failed")
                    print("\n  Module: " + title)
                    print("  Test: " + str(i) + " " + str(j))
                    print("  Output: " + out)
                    print("  Answer: " + ans)
                    print()
                    success = False
    
    else:
        print("not tested")
        success = False
    
    if success:
        print("OK")



# Checking for executable

if not os.path.exists("./dmcp"):
    PATH = "./dmcp"
    print("Error: executable not found")
    sys.exit()

PATH = "./dmcp"


# Getting list of available modules

list = Popen(PATH, stderr = PIPE, stdin = PIPE)
list.stdin.write(b"l\ne\n")

out, err = list.communicate()
list = err.decode()
list = list[list.find("List of available modules"):]

regex = r"[N|Z|Q|P]\-\d"

modules = re.finditer(regex, list, re.MULTILINE)

# Running

for module in modules:
    check(module[0][0] + module[0][2:])
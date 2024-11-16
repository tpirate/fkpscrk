from sys import argv
from string import digits

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk), end="")

def fourdigits(text, f):
    for i in range(10):
        f.write(text + digits[i] + "\n")
        f.write(digits[i] + text + "\n")
    for i in range(10):
        for j in range(10):
            f.write(text + digits[i] + digits[j] + "\n")
            f.write(digits[i] + digits[j] + text + "\n")
    for i in range(10):
        for j in range(10):
            for x in range(10):
                f.write(text + digits[i] + digits[j] + digits[x] + "\n")
                f.write(digits[i] + digits[j] + digits[x] + text + "\n")
    for i in range(10):
        for j in range(10):
            for x in range(10):
                for y in range(10):
                    f.write(text + digits[i] + digits[j] + digits[x] + digits[y]+ "\n")
                    f.write(digits[i] + digits[j] + digits[x] + digits[y] + text + "\n")                

def addbirth(text, f):
    # bd bm by + sy
    # bm bd by + sy
    # by by
    # bd bm bd bm
    # bm bd bm bd
    bd = argv[3][0] + argv[3][1]
    bm = argv[3][2] + argv[3][3]
    by = argv[3][4] + argv[3][5] + argv[3][6] + argv[3][7]
    bys = argv[3][6] + argv[3][7]
    f.write(text + bd + bm + by + '\n')
    f.write(text + bm + bd + by + '\n')
    f.write(text + bm + bd + bys + '\n')
    f.write(text + bd + bm + bys + '\n')
    f.write(text + bys + bm + bd + '\n')
    f.write(text + by + bm + bd + '\n')
    f.write(bd + bm + by +text +'\n')
    f.write(bm + bd + by +text +'\n')
    f.write(bm + bd + bys + text+'\n')
    f.write(bd + bm + bys + text+'\n')
    f.write(by + bm + bd + text+'\n')
    f.write(bys + bm + bd + text+'\n')
    f.write(by+by+text+'\n')
    f.write(text+by+by+'\n')
    f.write(bm+bd+bm+bd+text+'\n')
    f.write(text+bm+bd+bm+bd+'\n')
    f.write(text+bd+bm+bd+bm+'\n')
    f.write(bd+bm+bd+bm+text+'\n')
    

def main():
    txtlist = [argv[1],argv[2], argv[1] + argv[2]]
    for i in range(len(argv)-4):
        txtlist.append(argv[-i-1])
    for i in range(len(argv[3])):
        try: int(argv[3][i])
        except ValueError: prRed("BIRTHDATE NOT CORRECT FORMAT!"), exit(0)
    if len(argv[3]) > 8: prRed("BIRTHDATE NOT CORRECT FORMAT!"), exit(0)
    for i in range(len(txtlist)):
        txtlist.append(txtlist[i].capitalize())
        txtlist.append(txtlist[i].upper())
    with open(txtlist[0]+"-"+txtlist[1]+"-passlist.txt", "w") as f:
        for i in range(len(txtlist)):
            f.write(txtlist[i] + '\n')
            fourdigits(txtlist[i], f)
            addbirth(txtlist[i], f)
        
if __name__ == "__main__":
    if len(argv) == 1:
        prRed("Usage: python fkpscrk.py 'NAME' 'SURNAME' 'BIRTHDATE(ddmmyyyy)' 'elsetext'...")
        print("""First 3 args should be""", end="")
        prGreen("exact ") 
        print("""as they are most important and can be combined with elsetext,
after that you can enter any info you have; pet name, favourite team, fav color etc.
Please enter all text""", end="")
        prGreen("lowercase!\n")
        prRed("THERE MIGHT BE SOME DUPLICATES WITH RANNUM AND BIRTHDAY!")
    else:
        main()
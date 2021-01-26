# The code dictionary maps 'A'->0, 'B'->1, ..., 'Z'->25, ' '->26
# The edoc dictionary is the inverse of that map
import math
# import enchant

# d = enchant.Dict("en_US")
code = {}
edoc = {}
N = 27
for i in range(N-1):
    code[chr(i+65)] = i
    edoc[i] = chr(i+65)
    code[' '] = N-1
    edoc[N-1] = ' '
 
# This function prints out the frequency of each character in s
def stats(s):
    c = {}
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
        c[i] = 0
    for i in s:
        c[i] += 1
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
        print i,"->",c[i]


# Shifts the string p by b characters to the right.
# capital letters and blanks only
def shiftEncode(p, a, b):
    crypt = {}  
    for i in range(N):
        crypt[i] = (a*i+b) % N
    
    c = ""
    for i in p:
        c += edoc[crypt[code[i]]]
    return c

s1 = "IZEKDZDLWWIKOPNZOPOKDSTCKQLYDLCDTNKXPCCLRPKGPWWKOZYP"

for i in range(28):
    for j in range(28):
        print(shiftEncode("JYAKGDAMWLAYJVVAIOCADLYGSTJZJLTAQJLDICAUJIOANJPIKANCMGLHNAUGSIOAGYAHJNIWLMCASDLAKGDSNAJNAIOCACWSIOAWLHACZCSKIOJLTAIOWINAJLAJIAWLHAUOJMOAJNAQGSCAKGDVVARCAWAQWLAQKANGL", i, j))

# ALL THINGS THEREFORE ARE CHARGED WITH LOVE ARE CHARGED WITH GOD AND IF WE KNEW HOW TO TOUCH THEM GIVE OFF SPARKS AND TAKE FIRE YIELD DROPS AND FLOW RING AND TELL OF HIM
# THERE IS AN INMOST CENTER IN US ALL WHERE TRUTH ABIDES IN FULLNESS AND TO KNOW RATHER CONSISTS IN OPENING OUT A WAY WHERE THE IMPRISONED SPLENDOR MAY ESCAPE THEN IN EFFECTING ENTRY FOR A LIGHT SUPPOSED TO BE WITHOUT
# IF YOU CAN FILL THE UNFORGIVING MINUTE WITH SIXTY SECONDS WORTH OF DISTANCE RUN YOURS IS THE EARTH AND EVERYTHING THATS IN IT AND WHICH IS MORE YOULL BE A MAN MY SON

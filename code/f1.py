# The code dictionary maps 'A'->0, 'B'->1, ..., 'Z'->25, ' '->26
# The edoc dictionary is the inverse of that map
import math

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
        print (i,"->",c[i])


# Shifts the string p by b characters to the right.
# capital letters and blanks only
def shiftEncode(p, b):
    crypt = {}  
    for i in range(N):
        crypt[i] = (i+b) % N
    
    c = ""
    for i in p:
        c += edoc[crypt[code[i]]]
    return c


# Multiplies each character by a, then shifts by b
# capital letters and blanks only
def affineEncode(p, a, b):
    crypt = {}  
    for i in range(N):
        crypt[i] = (a*i+b) % N
    
    c = ""
    for i in p:
        c += edoc[crypt[code[i]]]
    return c

# Find the greatest common divisor of a and b
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

# Find the inverse of a mod m
def modinv(a, m):
    if gcd(a, m) != 1:
        raise Exception("There is no inverse...")

    multiplier = -1
    a, b = m, a
    w, x, y, z = 1, 0, 0, 1
    while b > 0:
        q = a // b
        a, b, w, x, y, z, = b, a%b, y, z, q*y + w, q*z + x
        multiplier *= -1

    return (x * multiplier) % m


# Takes a string of A-Z and space, uses 5 bits for each character, 
# and appends the bits to make a large number.
def string2number(s):
    rv = 0
    for c in s:
        rv = (rv << 5) + code[c]
    return rv

s1 = "IZEKDZDLWWIKOPNZOPOKDSTCKQLYDLCDTNKXPCCLRPKGPWWKOZYP"
s2 = "HAAPRFYLNZPRFCGCVDGCPHGCPSFHGNCKPUYRFPADBCPHGCPSFHGNCKPUYRFPNDKPHLKPYVPUCPILCUPFDUPRDPRDJSFPRFCTPNYBCPDVVPZWHGIZPHLKPRHICPVYGCPEYCAKPKGDWZPHLKPVADUPGYLNPHLKPRCAAPDVPFYT"
s3 = "DYJUJLCZLQALCAWFZDL JADJULCALIZLQRRLSYJUJLDUIDYLQVCEJZLCALOIRRAJZZLQAELDFLMAFSLUQDYJUL FAZCZDZLCALFKJACATLFIDLQLSQBLSYJUJLDYJLCWKUCZFAJELZKRJAEFULWQBLJZ QKJLDYJALCALJOOJ DCATLJADUBLOFULQLRCTYDLZIKKFZJELDFLVJLSCDYFID"

fac1 = 735731702333306149
fac2 = 727332459897667607

phi = 535121548882782114116501475940241688

#stats(s3)
for a in range(27):
    for b in range(27):
        if (a * 11 + b) % 27 == 26 and (a * 9 + b) % 27 == 4:
            # print(affineEncode(s3, a, b))
            pass

def get_words(n):
    letter = 0
    letters = []
    while n > 32:
        letter = n % 32
        letters.append(letter)
        -= letter
        n /= 32
    
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
        print(str(i)+"->"+str(c[i]))


# Shifts the string p by b characters to the right.
# capital letters and blanks only
def shiftEncode(p,a,b):
    crypt = {}  
    for i in range(N):
        crypt[i] = (a*i+b) % N
    
    c = ""
    for i in p:
        c += edoc[crypt[code[i]]]
    return c

s1 = "HAAPRFYLNZPRFCGCVDGCPHGCPSFHGNCKPUYRFPADBCPHGCPSFHGNCKPUYRFPNDKPHLKPYVPUCPILCUPFDUPRDPRDJSFPRFCTPNYBCPDVVPZWHGIZPHLKPRHICPVYGCPEYCAKPKGDWZPHLKPVADUPGYLNPHLKPRCAAPDVPFYT"
s2 = "DYJUJLCZLQALCAWFZDL JADJULCALIZLQRRLSYJUJLDUIDYLQVCEJZLCALOIRRAJZZLQAELDFLMAFSLUQDYJUL FAZCZDZLCALFKJACATLFIDLQLSQBLSYJUJLDYJLCWKUCZFAJELZKRJAEFULWQBLJZ QKJLDYJALCALJOOJ DCATLJADUBLOFULQLRCTYDLZIKKFZJELDFLVJLSCDYFID"
s3 = "JYAKGDAMWLAYJVVAIOCADLYGSTJZJLTAQJLDICAUJIOANJPIKANCMGLHNAUGSIOAGYAHJNIWLMCASDLAKGDSNAJNAIOCACWSIOAWLHACZCSKIOJLTAIOWINAJLAJIAWLHAUOJMOAJNAQGSCAKGDVVARCAWAQWLAQKANGL"

for s in [s1, s2, s3]:
    for i in range(27):
        for j in range(27):
            string = shiftEncode(s,i,j)
            if " AND " in string:
                print(string)
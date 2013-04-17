"""
Copyright: Rahul Bhalerao <b.rahul.pm@gmail.com>
Copyright: Kartik Mistry <kartik.mistry@gmail.com>
License: GNU GPLv2+
Generates a master file with all the possible combination in Gujarati script.
"""

import encodings

output = open("Gujarati.txt", 'w')
base = 0x0A81
limit = 0x0AF1
gujChar = []
lcount = 0
gujIndVow= []
gujCons = []
gujDepVow = []
gujVarSig =  []
GujVowVarSig = []
GujConVarSig = []
GujConDepVow = []
GujConCon = []
GujConConDepVow = []
GujConConCon = []
halant = encodings.codecs.utf_8_encode(unichr(0x0ACD))[0]

def guj_independent_vowels():
    for charCode in range(0xA85, 0xA94):
        gujIndVow.append(encodings.codecs.utf_8_encode(unichr(charCode))[0])

def guj_consonants():
    for charCode in range(0xA95,0xAB9):
        gujCons.append(encodings.codecs.utf_8_encode(unichr(charCode)) [0])
#    for charCode in range(0x958, 0x95F):
#        gujCons.append(encodings.codecs.utf_8_encode(unichr(charCode)) [0])

def guj_dependent_vowels():
    for charCode in range(0xABE,0xACC):
        gujDepVow.append(encodings.codecs.utf_8_encode(unichr(charCode)) [0])

def guj_various_signs():
    for charCode in range(0xA81,0xA83):
        gujVarSig.append(encodings.codecs.utf_8_encode(unichr(charCode)) [0])
#    for charCode in range(0x951, 0x954):
#        gujVarSig.append(encodings.codecs.utf_8_encode(unichr(charCode)) [0])
    gujVarSig.append(encodings.codecs.utf_8_encode(unichr(0xABC))[0])
    gujVarSig.append(encodings.codecs.utf_8_encode(unichr(0xACD))[0])

#if self.__doc__=="main" :
 #   """
  #  """
guj_independent_vowels()
guj_dependent_vowels()
guj_consonants()


for i in gujIndVow:
    for j in gujVarSig[1:-2]:
        GujVowVarSig.append( i + j)

for i in gujCons:
    for j in gujVarSig:
        GujConVarSig.append( i + j)

for i in gujCons:
    for j in gujCons:
        GujConCon.append( i + halant + j)

for i in gujCons:
    for j in gujDepVow:
        GujConDepVow.append( i + j)

# Triple combinations
#for i in gujCons:
#    for j in gujCons:
#        for k in gujCons:
#            GujConConCon.append( i + halant + j + halant + k)

# Triple combinations with vowels
#for i in GujConCon:
#    for j in gujDepVow:
#        GujConConDepVow.append(i + j)

for charCode in range(base, limit):
    gujChar.append(encodings.codecs.utf_8_encode(unichr(charCode))[0])


line = []
for i in gujChar:
    line.append(i + '\t')
    lcount=(lcount+1)%10
    if(lcount==0):
        line.append('\n\n')
        print ''.join(line)
        output.write(''.join(line))
        line = []

line = []
for i in GujVowVarSig:
    line.append(i + '\t')
    lcount=(lcount+1)%10
    if(lcount==0):
        line.append('\n\n')
        print ''.join(line)
        output.write(''.join(line))
        line = []

line = []
for i in GujConVarSig:
    line.append(i + '\t')
    lcount=(lcount+1)%10
    if(lcount==0):
        line.append('\n\n')
        print ''.join(line)
        output.write(''.join(line))
        line = []

line = []
for i in GujConDepVow:
    line.append(i + '\t')
    lcount=(lcount+1)%10
    if(lcount==0):
        line.append('\n\n')
        print ''.join(line)
        output.write(''.join(line))
        line = []

line = []
for i in GujConCon:
    line.append(i + '\t')
    lcount=(lcount+1)%10
    if(lcount==0):
        line.append('\n\n')
        print ''.join(line)
        output.write(''.join(line))
        line = []

line = []
for i in GujConConDepVow:
    line.append(i + '\t')
    lcount=(lcount+1)%10
    if(lcount==0):
        line.append('\n\n')
        print ''.join(line)
        output.write(''.join(line))
        line = []

# This is too much of output.
#line = []
#for i in GujConConCon:
#    line.append(i + '\t')
#    lcount=(lcount+1)%10
#    if(lcount==0):
#        line.append('\n\n')
#        print ''.join(line)
#        output.write(''.join(line))
#        line = []

output.close()


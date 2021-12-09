import numpy as np

file = open('input day03.txt','r')
inp = file.readlines()
file.close()


for i in range(len(inp)):
    inp[i]=inp[i].strip('\n')

#--------PART ONE----------------------------------------
ones = [0]*len(inp[0])
zeros = [0]*len(inp[0])

for num in inp:
    for bit in range(len(num)):
        if num[bit] == '1':
            ones[bit] += 1
        else:
            zeros[bit] += 1
    
gamma  = ''
epsilon = ''
for i in range(len(ones)):
    if ones[i] > zeros[i]:
        gamma = gamma+'1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma+ '0'
        epsilon = epsilon + '1'
        
gammaB10 = int(gamma,2)
epsilonB10 = int(epsilon,2)

result = gammaB10 * epsilonB10
print(result)

#--------PART TWO----------------------------------------

oxGenRate = inp[:]
c02scrubRate = inp[:]

oxGeneratorRating = 0

bitPos = 0
one = 0
zero = 0
msb = 0
while len(oxGenRate) > 1: #and bitPos < 12:
    for num in oxGenRate:
        if num[bitPos] == '1':
            one += 1
        else:
            zero += 1
    
    if one >= zero:
        msb = 1
    else:
        msb = 0
    
    oxGenRateNew = []
    for num in oxGenRate:
        if num[bitPos] == f'{msb}':
            oxGenRateNew.append(num)
        
    oxGenRate = oxGenRateNew[:]  
    bitPos += 1
    one = 0
    zero = 0
        
oxGeneratorRating = int(oxGenRate[0],2)
print(oxGeneratorRating)

c02scrubbingRating = 0

bitPos = 0
one = 0
zero = 0
msb = 0

while len(c02scrubRate) > 1: #and bitPos < 12:
    for num in c02scrubRate:
        if num[bitPos] == '1':
            one += 1
        else:
            zero += 1
    
    if one < zero:
        lsb = 1
    else:
        lsb = 0
    
    c02scrubRateNew = []
    for num in c02scrubRate:
        if num[bitPos] == f'{lsb}':
            c02scrubRateNew.append(num)
        
    c02scrubRate = c02scrubRateNew[:]  
    bitPos += 1
    one = 0
    zero = 0


c02scrubbingRating = int(c02scrubRate[0],2)
print(c02scrubbingRating)
result2 = oxGeneratorRating * c02scrubbingRating
print(result2)
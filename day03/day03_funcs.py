import numpy as np
    
def main():
    input = getInput('day03/input day03.txt')
    gammaRate, epsilonRate = mostCommonValue(input) 
    print('----Part One----')
    print(f'Gamma Rate: {gammaRate} \nEpsilon Rate: {epsilonRate}\n')
    gammaRateB10, epsilonRateB10 = int(gammaRate,2),int(epsilonRate,2)
    print(f'Rates in Base10:\nGamma Rate: {gammaRateB10} \nEpsilon Rate: {epsilonRateB10}')
    print(f'Result is: {gammaRateB10 * epsilonRateB10}')
    
    
    print('----Part Two----')
    oxGeneratorRating, c02scrubbingRaing = selectMatchingBitCriteria(input)
    oxGeneratorRatingB10, c02scrubbingRaingB10 = int(oxGeneratorRating, 2), int(c02scrubbingRaing, 2)
    print(f'Result is: {oxGeneratorRatingB10 * c02scrubbingRaingB10}')
    
def getInput(path):
    file = open(f'{path}','r')
    inp = file.readlines()
    file.close()

    for i in range(len(inp)):
        inp[i]=inp[i].strip('\n')
    
    return inp

def mostCommonValue(data):
    ones = [0]*len(data[0])
    zeros = [0]*len(data[0])

    for num in data:
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
    
    return gamma,epsilon

def selectMatchingBitCriteria(data):
    oxGenRate = data[:]
    
    bitPos = 0
    while len(oxGenRate) > 1: #and bitPos < 12:
        one = 0
        zero = 0
        msb = 0
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
    
    oxGeneratorRating = oxGenRate[0]
    
    c02scrubRate = data[:]
    bitPos = 0
    while len(c02scrubRate) > 1: #and bitPos < 12:
        one = 0
        zero = 0
        lsb = 0
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
        


    c02scrubbingRating = c02scrubRate[0]
    
    return oxGeneratorRating,c02scrubbingRating
    
    

if __name__ == '__main__':
    main()
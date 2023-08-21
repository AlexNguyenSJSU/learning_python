#Encode Function:
def encode(strs):
    result = ""

    for i in strs:
        count = str(len(i))
        result += count + '#' + i 
    
    return result

#Testcase:
strs = ['we', 'love', ':', 'Mirinda']
result = encode(strs)
print(result)

#Decode Function:
def decode(str1):
    result, i = [], 0

    while i < len(str1):
        j = i
        while str1[j] != '#':
            j += 1
        
        length_word = int(str1[i:j])
        result.append(str1[j + 1: j + 1 + length_word])
        i = j + 1 + length_word
    
    print(result)

#Testcase:
decode(result)

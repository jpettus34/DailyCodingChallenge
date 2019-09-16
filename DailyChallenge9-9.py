from sympy.utilities.iterables import multiset_permutations

def testList(l):
    index = 0
    boolDict = {'white': False , 'black': False , 'green': False , 'orange': False , 'red': False, 'purple': False}
    for c in l:
        if(c == 'white'):
            boolDict['green'] = True
            boolDict['white'] = False
            boolDict['black'] = False
            boolDict['orange'] = True
            boolDict['red'] = True
            boolDict['purple'] = True

        elif(c == 'red'):
            boolDict['green'] = True
            boolDict['white'] = False
            boolDict['black'] = False
            boolDict['orange'] = False
            boolDict['red'] = False
            boolDict['purple'] = False
        elif (c == 'black'):
            boolDict['green'] = False
            boolDict['white'] = False
            boolDict['black'] = True
            boolDict['orange'] = False
            boolDict['red'] = True
            boolDict['purple'] = True
        elif (c == 'orange'):
            boolDict['green'] = False
            boolDict['white'] = False
            boolDict['black'] = True
            boolDict['orange'] = False
            boolDict['red'] = True
            boolDict['purple'] = False
        elif (c == 'green'):
            boolDict['green'] = False
            boolDict['white'] = True
            boolDict['black'] = False
            boolDict['orange'] = True
            boolDict['red'] = False
            boolDict['purple'] = False
        elif (c == 'purple'):
            boolDict['green'] = False
            boolDict['white'] = False
            boolDict['black'] = True
            boolDict['orange'] = False
            boolDict['red'] = True
            boolDict['purple'] = False
        
        try:
            if(boolDict[l[index + 1]] == False):
                return False
            else:
                index += 1
        except:
            return True
        
    return True
def bombDefuse(colors):
    permutations = multiset_permutations(colors)
    for p in permutations:
        if(testList(p)):
            return 'defused'
    return 'boom'

test =  ["black", "red", "white", "orange", "white", "green" ,"black" ,"purple" ,"red",
 "orange", "green" ,"green" ,"red","black","orange"]
print(bombDefuse(test))
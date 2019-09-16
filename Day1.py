def dailyChallenge(a):
    size = len(a)
    max_so_far =a[0] 
    curr_max = a[0] 
      
    for i in range(1,size): 
        curr_max = max(a[i], curr_max + a[i]) 
        max_so_far = max(max_so_far,curr_max) 
          
    return max_so_far 

def main(): 
    print(str(dailyChallenge([2,-8,3,-2,4,-10])))
    print(str(dailyChallenge([-1,-2,-3])))
    print(str(dailyChallenge([1,2,3,4,5])))
    print(str(dailyChallenge([-1,0,1])))
    print(str(dailyChallenge([-1,2,-1, 2,-1])))

if __name__ == '__main__':
   main()
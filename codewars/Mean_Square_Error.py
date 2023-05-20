def solution(array_a, array_b):
    
    sum = 0
    
    for i in range(len(array_a)):
        nabs = 0
        nabs = abs(array_a[i] - array_b[i])
        
        sum = sum + nabs**2
    
    return sum/len(array_a)
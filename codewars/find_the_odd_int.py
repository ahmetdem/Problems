def find_it(seq):
    
    def isodd(num):
        if num % 2 == 1: return True
        
    for i in seq:
        if isodd(seq.count(i)): return i
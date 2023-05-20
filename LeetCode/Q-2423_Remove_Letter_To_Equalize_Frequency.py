class Solution:
    def equalFrequency(self, word: str) -> bool:

        data = {}
        
        for letter in word:
            
            if letter in data:
                data[letter] += 1
            else: data[letter] = 1
            
        vals = list(data.values())
        
        for i in range(len(vals)):
            copy = vals.copy()
            copy[i] -= 1
            
            if copy[i] == 0:
                copy.remove(0)
                
            if len(set(copy)) == 1:
                return True
        
        else: return False
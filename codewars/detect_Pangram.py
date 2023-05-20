def is_pangram(s):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    s = s.upper()
    slist = list(s)
    
    for i in slist:
        if i in alphabet:
            alphabet.remove(i)
            
            if len(alphabet) == 0:
                return True

    return False

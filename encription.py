class Sap:
    def __init__(self, num):
        self.num = str(num)

    def encript(self):
        result = ""
        for x in self.num:
            result += "abcdefghijklmnopqrstuvwxyz"[int(x)]
        return result
    
    def __add__(self, other):
        return Sap(int(self.num) + int(other.num) + 1)
    
    def __str__(self):
        return self.num
    
n = Sap(590012121)

print("Encrypted:", n.encript())
print("After +1:", n + Sap(0))
print("Decrypted:", n)

import hashlib
import os
class AntiVirus:

    
    def __init__(self,FileName):
        self.FileName =FileName

    

    def Scan(self):
        file =open(self.FileName,"br")
        read = file.readline()
        md5 =hashlib.md5()
        md5.update(read)
        hash =(md5.hexdigest())
        print(hash)
        Malware =open("Hahses.txt","r")
        read =Malware.readlines()
        for i in read:
            if i ==hash:
                os.remove(file)
            else:
                 print("Il y'a pas de détéction ")
                 break


antivur =AntiVirus("tata.txt")
antivur.Scan()

#import collections
#wordlist = collections.Counter(file)

#--------------Aufgabe1---------------------------

dict = {}
Korpus = []

def tf_read():
    with open("tf_read.txt", "r") as file:
        dict = {}
        for line in file:
            wordlist = line.replace(",", "").replace(".", "").replace("â€™", " ").replace("â€”", " ").split()
        for item in wordlist:
            if item not in dict.keys():
                dict[item] = 1
            else:
                dict[item] = dict[item] + 1
    Korpus.append(dict)
    print(dict)

tf_read()

#----------------Aufgabe2-----------------------

dict2 = {}

def tf_read2():
    with open("tf_read2.txt", "r") as file:
        dict2 = {}
        for line in file:
            wordlist = line.replace(",", "").replace(".", "").replace("â€™", " ").replace("â€”", " ").split()
        for item in wordlist:
            if item not in dict2.keys():
                dict2[item] = 1
            else:
                dict2[item] = dict2[item] + 1
    Korpus.append(dict2)
    print(dict2)

tf_read2()

print(Korpus)


#----------------------Aufgabe 2 (Verbesserung mit Constructor)-----------------------------

class Idf():
    def __init__(self, dokument, wort, korpus):
        self.dokument = dokument
        self.word = wort
        self.korpus = korpus

    def idf(self):
        for line in self.dokument:
            wordlist = line.replace(",", "").replace(".", "").replace("â€™", " ").replace("â€”", " ").split()
        for item in wordlist:
            if item not in self.korpus.keys():
                self.dokument[item] = 1
            else:
                self.dokument[item] = dict2[item] + 1
    print(self.word)

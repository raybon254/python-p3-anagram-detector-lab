# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word = word
        pass

    def match(self,list):
        new = []
        for words in list:
            if sorted(words) == sorted(self.word):
                new.append(words)
        return new
        return []
                

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
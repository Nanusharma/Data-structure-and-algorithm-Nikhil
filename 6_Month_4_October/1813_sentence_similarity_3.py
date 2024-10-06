# https://leetcode.com/problems/sentence-similarity-iii/description/?envType=daily-question&envId=2024-10-06

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        token1 = self.tokenize(sentence1)
        token2 = self.tokenize(sentence2)
        i, j= 0, 0
        len1, len2 =len(token1),len(token2)

        while i< len1 and i <len2 and token1[i] ==token2[i]:
            i += 1

        while j < len1 - i and j < len2 - i and token1[len1 -1 -j] == token2[len2- 1 - j]:
            j +=1
        
        return i +j>= min(len1,len2)

    # Tokenize function without using external libraries
    def tokenize(self,text):
        tokens = []
        word = ""

        for char in text:
            if char !=' ':
                word+=char
            else:
                if word: 
                    tokens.append(word)
                    word= ""  
        if word is not None:  
            tokens.append(word)

        return tokens


obj = Solution()
sentence1 = "My name is Haley and i like reading poems"
sentence2 = "My reading poems"
print(obj.areSentencesSimilar(sentence1,sentence2))

# #  ['My', 'name', 'is', 'Haley', 'and', 'i', 'like', 'reading', 'poems']
# #  ['My', 'reading', 'poems']

# #  ['My', 'name', 'is', 'Haley', 'and', 'i', 'like', 'reading', 'poems']
# #  ['My','name' , 'reading', 'poems']
# #  ['My','name' ,'like' , 'reading', 'poems']
# #  ['my']
# #  ['my','name']


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=''
        n=min(len(word1),len(word2))
        for i in range(n):
            s+=word1[i]+word2[i]
        i+=1
        j=i
        while (i) != len(word1):
            s+=word1[i]
            i+=1
        while (j) !=len(word2):
            s+=word2[j]
            j+=1
        return s

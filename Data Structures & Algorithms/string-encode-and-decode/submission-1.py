class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        # format of s "1word4#1word2word4#2word...."
        res = []
        i = 0 
        while i < len(s): # until end of encoded string
            j = i # start from current beginning
            while s[j] != '#': 
                j += 1 # counts until first "#" is encountered
            length = int(s[i:j]) # length of word
            res.append(s[j+1 : j+1+length]) # skips the "#" that comes after word, and takes the word itself
            i = j+1+length # skips current and goes to next word
        return res
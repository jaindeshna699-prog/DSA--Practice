# Time complexity : O(N)
# Space complexity : O(N)

class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for char in s:
            if char!= " ":           # for non space char which means a word
                word += char
            elif word:               # if space is found it means the word is completed
                words.append(word)   # it is also tackling the extra space
                word = ""            # here we are reseting the word
        if word:
            words.append(word)       # it manages the final word if we dont have space thereafter
        return " ".join(words[::-1]) 
class Solution:
    def findWordsContaining(self, words, x):
        result = []
        for i in range(len(words)):
            if x in words[i]:
                result.append(i)
            return result

s = Solution()
print(s.findWordsContaining(['Rock', 'Paper', 'Scissor'], "r"))
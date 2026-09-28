class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        res = 0
        for word in words:
            index = Counter(chars)
            for i in range(len(word)):
                if word[i] in index and index[word[i]] > 0:
                    if i == len(word) - 1:
                        res += len(word)
                    index[word[i]] -= 1
                else:
                    break
        return res
        
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        len1, len2 = len(word1), len(word2)
        for i in range(max(len1, len2)):
            if i < len1 and i < len2:
                output.append(word1[i])
                output.append(word2[i])
            elif i >= len1:
                output.append(word2[i])
            else:
                output.append(word1[i])
        output_str = ''.join(output)
        return output_str

        
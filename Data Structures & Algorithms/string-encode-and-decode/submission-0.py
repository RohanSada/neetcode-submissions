class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ''
        combined_words = ''
        for i in strs:
            enc_str = enc_str + str(len(i)) + ','
            combined_words += str(i)
        enc_str += '#,'
        enc_str = enc_str + combined_words
        return enc_str


    def decode(self, s: str) -> List[str]:
        '5,5,#,HelloWorld'
        output_list = []
        numbers, enc_str = s.split('#,')
        numbers = numbers.split(',')[:-1]
        count = 0
        for i in numbers:
            word = enc_str[count:count+int(i)]
            output_list.append(str(word))
            count = count + int(i)
        return output_list
        



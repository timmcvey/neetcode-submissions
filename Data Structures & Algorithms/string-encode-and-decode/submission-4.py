class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ''
        for encodeStr in strs:
            encodedStr += str(len(encodeStr)) + '#' + encodeStr
        return encodedStr
        
    def decode(self, s: str) -> List[str]:
        decodedStrs = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            num = int(s[i:j])
            i = j + 1
            j = i + num
            decodedStrs.append(s[i:j])
            i = j
        return decodedStrs
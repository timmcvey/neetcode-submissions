class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ''
        for i in range(len(strs)):
            if strs[i] == '':
                encodedStr += '*'
            for j in range(len(strs[i])):
                encodedStr += str(ord(strs[i][j]))
                if j < len(strs[i])-1:
                    encodedStr += '|'
            if i < len(strs) - 1:
                encodedStr += ' '
        return encodedStr
    def decode(self, s: str) -> List[str]:
        if s == '*':
            return [""]
        if s == '':
            return []
        decodedList = []
        strList = s.split(" ")
        print(strList)
        for i in range(len(strList)):
            # if i == 1:
            if strList[i] == '*':
                decodedList.append('')
            else:
                nums = strList[i].split("|")
                strOutput = ''
                for num in nums:
                    strOutput += chr(int(num))
                decodedList.append(strOutput)

        return decodedList

class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = s.split(" ")
        charList = []
        for word in words:
            for char in word.strip():
                if char.isalnum():
                    charList.append(char.lower())
        
        if len(charList) == 1:
            return True
        
        for i in range(len(charList)):
            front = i
            back = len(charList) - 1 - i
            if charList[front] == charList[back]:
                continue
            else:
                return False

        return True


            
  
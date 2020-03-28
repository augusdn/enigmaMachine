class PlugBoard:
    def __init__(self):
        self._settings = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    def translate(self, c):
        number = ord(c)-65
        result = self._settings[number]
        return result

    def connectTwo(self, c1, c2):
        t1 = ord(c1)-65
        t2 = ord(c2)-65
        if self._settings[t1] != c1:
            # print(chr(t1+65) + " is already in use")
            return -1
        if self._settings[t2] != c2:
            # print(chr(t2+65) + " is already in use")
            return -2
        else:
            self._settings[t1] = c2
            self._settings[t2] = c1
            return 0
    
    def removeTwo(self, t1, t2):
        if self._settings[t1] == t1:
            # print(chr(t1+65) + " is not plugged")
            return -1
        if self._settings[t2] != t2:
            # print(chr(t2+65) + " is not plugged")
            return -2
        else:
            self._settings[t1] = t1
            self._settings[t2] = t2
            return 0
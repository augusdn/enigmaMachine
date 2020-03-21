class PlugBoard:
    def __init__(self):
        self._settings = list(range(26))
    
    def translate(self, number):
        result = self._settings[number]
        return result

    def connectTwo(self, t1, t2):
        if self._settings[t1] != t1:
            print(chr(t1+65) + " is already in use")
            return -1
        if self._settings[t2] != t2:
            print(chr(t2+65) + " is already in use")
            return -2
        else:
            self._settings[t1] = t2
            self._settings[t2] = t1
            return 0
    
    def removeTwo(self, t1, t2):
        if self._settings[t1] == t1:
            print(chr(t1+65) + " is not plugged")
        if self._settings[t2] != t2:
            print(chr(t2+65) + " is not plugged")
        else:
            self._settings[t1] = t1
            self._settings[t2] = t2
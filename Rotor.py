class Rotor:
    def __init__(self, wiring, notch):
        self._wiring = wiring
        self._notch = ord(notch.upper())-65
        self._position = 0
        self._ring = 0

    def rotate(self):
        self._position = (self._position + 1) % 26

    def isNotch(self):
        if self._position == self._notch:
            return 1
        else:
            return 0
    
    def ringSettings(self, i):
        self._ring = (self._ring + i) % 26

    def reset(self):
        self._position = 0
        self._ring = 0

    def translate(self, c):
        t = ord(c)-65
        offset = self._position + self._ring
        result = chr( (ord(self._wiring[(t+self._position)%26])-65-offset)%26 + 65)
        # print (result)
        return result
    
    def reverse(self, c):
        for a in list(range(26)):
            alphabet = chr(a+65)
            if (self.translate(alphabet) == c):
                return alphabet
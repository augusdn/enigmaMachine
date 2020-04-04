class Rotor:
    def __init__(self, wiring=None, notch="A", name=None, model=None, date=None, position="A"):
        self._wiring = wiring
        self._notch = ord(notch.upper())-65
        self._name = name
        self._model = model
        self._date = date
        self._position = ord(position.upper())-65
        self._ring = 0

    def rotate(self):
        self._position = (self._position + 1) % 26

    def isNotch(self):
        if self._position == self._notch:
            return 1
        else:
            return 0
    
    def ringSettings(self, c):
        self._ring = ord(c.upper())-65

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
    
    def getPosition(self):
        offset = chr(self._position + 65)
        return offset

    def __str__(self):
        return """
        Name: %s
        Model: %s
        Date: %s
        Wiring: %s
        Position: %s
        Ring: %s""" % (self._name, self._model, self._date, self._wiring, chr(self._position+65), chr(self._ring+65))
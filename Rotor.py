class Rotor:
    def __init__(self, wiring, notch, initial_position, ring_setting):
        self._wiring = wiring
        self._notch = ord(notch.upper())-65
        self._position = ord(initial_position.upper())-65
        self._ring = ord(ring_setting.upper())-65

    def rotate(self):
        self._position = (self._position + 1) % 26
        if self._position == self._notch + 1:
            return 1
        else:
            return 0

    def translate(self, t1):
        result = self._wiring[t1]
        print (result)
        return result
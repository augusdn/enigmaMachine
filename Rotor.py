class Rotor:
    def __init__(self, wiring, notch, initial_position, ring_setting):
        self._wiring = []
        self._notch = None
        self._position = 0
        self._ring = 0

    def rotate(self):

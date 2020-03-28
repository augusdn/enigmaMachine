class RotorSystem:
    def __init__(self):
        self._rotorA = None
        self._rotorB = None
        self._rotorC = None
# Rotors
    def addRotorA(self, rotor):
        self._rotorA = rotor

    def addRotorB(self, rotor):
        self._rotorB = rotor

    def addRotorC(self, rotor):
        self._rotorC = rotor

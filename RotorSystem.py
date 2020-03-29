from Rotor import Rotor

class RotorSystem:
    def __init__(self):
        self._rotorI   = Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
        self._rotorII  = Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
        self._rotorIII = Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
        self._rotorIV  = Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J')
        self._rotorV   = Rotor('VZBRGITYUPSDNHLXAWMJQOFECK', 'Z')
        # self._rotorA = self._rotorI
        # self._rotorB = self._rotorII
        # self._rotorC = self._rotorIII
        self._rotors = [self._rotorI, self._rotorII, self._rotorIII]
# Rotors
    # def addRotorA(self, rotor):
    #     self._rotorA = rotor
    #     self._rotorA.reset()

    # def addRotorB(self, rotor):
    #     self._rotorB = rotor
    #     self._rotorB.reset()

    # def addRotorC(self, rotor):
    #     self._rotorC = rotor
    #     self._rotorC.reset()

    def rotate(self):
        if self._rotors[1].isNotch():
            for r in self._rotors:
                r.rotate()
        elif self._rotors[2].isNotch():
            self._rotors[1].rotate()
            self._rotors[2].rotate()
        else:
            self._rotors[2].rotate()
    
    def translate(self, c):
        self.rotate()
        r3 = self._rotors[2].translate(c)
        print(r3)
        r2 = self._rotors[1].translate(r3)
        print(r2)
        r1 = self._rotors[0].translate(r2)
        print(r1)
        reflector = "S"
        r1 = self._rotors[0].reverse(reflector)
        print(r1)
        r2 = self._rotors[1].reverse(r1)
        print(r2)
        r3 = self._rotors[2].reverse(r2)
        print(r3)
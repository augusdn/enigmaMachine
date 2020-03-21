class RotorSystem:
# Rotors
    def addRotorA(self, rotor):
        if self._rotorA == None:
            self._rotorA = rotor
        else:
            print("Remove rotor A first!\n")

    def addRotorB(self, rotor):
        if self._rotorB == None:
            self._rotorB = rotor
        else:
            print("Remove rotor B first!\n")

    def addRotorC(self, rotor):
        if self._rotorC == None:
            self._rotorC = rotor
        else:
            print("Remove rotor C first!\n")

    def removeRotorA(self):
        if self._rotorA == None:
            print("Rotor A is empty!\n")
        else:
            self._rotorA = None

    def removeRotorB(self):
        if self._rotorB == None:
            print("Rotor B is empty!\n")
        else:
            self._rotorB = None

    def removeRotorC(self):
        if self._rotorC == None:
            print("Rotor C is empty!\n")
        else:
            self._rotorC = None
class Reflector:
    def __init__(self, wiring=None, name=None):
        if wiring != None:
            self._wiring = wiring
        else:
            self._wiring="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._name = name

    def translate(self, c):
        t = ord(c)-65
        result = self._wiring[t]
        # print (result)
        return result

    def __str__(self):
        return """
        Name: %s
        Wiring: %s""" % (self._name, self._wiring)
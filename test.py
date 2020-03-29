from Rotor import Rotor

test = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 'A')
test.rotate()
print(test.translate('A'))
print(test.reverse('E'))
test.rotate()
print(test.translate('A'))
print(test.reverse('J'))
test.rotate()
print(test.translate('A'))
print(test.reverse('C'))
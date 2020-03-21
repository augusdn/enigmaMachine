from EnigmaMachine import EnigmaMachine
import msvcrt

# Initialise system
enigma = EnigmaMachine()
print("press [a-zA-Z] to encrypt letter")
print("pressing any other key will open settings")

while 1:
    key = msvcrt.getch().decode()
    if key.isalpha():
        enigma.encrypt(key)
    else:
        while 1:
            print("#Menu")
            print("0: Debug Mode ON/OFF")
            print("1: Plugboard settings")
            print("2: Rotor Settings")
            print("3: Reflector Settings")
            print("4: Back to Enigma")
            print("5: Exit the program")
            key = int(msvcrt.getch().decode())

            if key == 0:
                enigma.toggleDebug()
            elif key == 1:
                #plugboard settings
                print("Press first target alphabet: ")
                t1 = msvcrt.getch().decode()
                while not t1.isalpha():
                    t1 = msvcrt.getch().decode()
                print(t1)
                print("Press second target alphabet: ")
                t2 = msvcrt.getch().decode()
                while not t2.isalpha():
                    t2 = msvcrt.getch().decode()
                print(t2)
                enigma.plugTwo(t1, t2)
            elif key == 4:
                print("Back to Enigma")
                break
            else:
                print("Exiting the program")
                raise SystemExit(0)
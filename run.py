from EnigmaMachine import EnigmaMachine
import msvcrt

# Initialise system
enigma = EnigmaMachine()
print("press [a-zA-Z] to encrypt letter")
print("pressing any other key will open settings")

while 1:
    key = msvcrt.getch().decode()
    if key.isalpha():
        print(key.upper() + "=>" +enigma.encrypt(key.upper()))
    elif key.isdigit():
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
                t1 = msvcrt.getch().decode().upper()
                while not t1.isalpha():
                    t1 = msvcrt.getch().decode().upper()
                print(t1)
                print("Press second target alphabet: ")
                t2 = msvcrt.getch().decode().upper()
                while not t2.isalpha():
                    t2 = msvcrt.getch().decode().upper()
                print(t2)
                enigma.plugTwo(t1, t2)
            elif key == 2:
                print("Which Rotor to modify? from 1-3")
                t1 = int(msvcrt.getch().decode())
                print("Changing " + str(t1))
                print("1 = Change Rotor, 2 = Change position, 3 = ring setting, 4 = print Setting")
                t2 = int(msvcrt.getch().decode())
                if t2 == 1:
                    print("Change " + str(t1) + " to? from 1-5")
                    t2 = int(msvcrt.getch().decode())
                    enigma.changeRotor(t1, t2)
                elif t2 == 2:
                    print("Change position of " + str(t1) + " to? from A-Z")
                    t2 = msvcrt.getch().decode().upper()
                    enigma._rotorSystem.changePosition(t1, t2)
                elif t2 == 3:
                    print("Change ring setting of " + str(t1) + " to? from A-Z")
                    t2 = msvcrt.getch().decode().upper()
                    enigma._rotorSystem.changeRing(t1,t2)
                elif t2 == 4:
                    enigma._rotorSystem.printSettings()
            elif key == 3:
                print("Change Reflector to? 1-3")
                t2 = int(msvcrt.getch().decode())
                enigma._rotorSystem._rotors[3] = enigma._rotorSystem._reflectorList[t2-1]
                enigma._rotorSystem.printSettings()
            elif key == 4:
                print("Back to Enigma")
                print("press [a-zA-Z] to encrypt letter")
                print("pressing any other key will open settings")
                break
            else:
                print("Exiting the program")
                raise SystemExit(0)
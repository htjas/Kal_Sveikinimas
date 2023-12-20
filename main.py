import time
import os


def sveikas(name):
    os.system('cls')
    ans = input(f'Labas, čia {name}? \n ').lower()
    if ans == 'jo' or ans == 'taip' or ans == 'aha':
        ans = input('Puiku! Su šventėm!\n').lower()
        if 'tave' in ans or 'su' in ans:
            action()
            return name
        else:
            ans = input('Man nepalinkėsi?:/ \n').lower()
            if 'tave' in ans or 'su' in ans:
                action()
                return name
            else:
                print(":(( \n (verkiu lygiai 2 sekundes)")
                time.sleep(2)
                sveikas(name)
    else:
        ans = input('Ar tikrai? \n').lower()
        if ans == 'jo' or ans == 'taip' or ans == 'aha':
            print('neapgaudinėk ir bandyk dar kartą')
            time.sleep(1)
            print('*elevator music playing*')
            time.sleep(3)
            sveikas(name)
        else:
            print('ummm ok..')
            time.sleep(2)
            sveikas(name)


def action():
    print('Ačiū! \r')
    time.sleep(2)
    print('Skiriu tau šį kalėdinį sveikinimą ^^')
    time.sleep(1)
    print('Pasiruošęs?')
    time.sleep(2)
    print('nieko nerašyk, man reikia susikaupt')
    time.sleep(2)
    print('*inhale*')
    time.sleep(1)
    print('*exhale*')
    time.sleep(1)
    print('*inhale*')
    time.sleep(1)
    print('*exhale*')
    for i in range(5, 0, -1):
        print(i, end='\r')
        time.sleep(1)
    print("ACTION")
    time.sleep(2)


def kacialke(name):
    os.system('cls')
    time.sleep(1)
    jump(2)
    pullup(0.2)
    pullup(0.2)
    pullup(0.2)
    pullup(0.2)
    pullup(0.2)
    dip(0.2)
    dip(0.2)
    dip(0.2)
    dip(0.2)
    dip(0.2)
    down(0.2)
    vilkas(0.2)
    vilkas(0.2)
    vilkas(0.2)
    ending(0.3, name)


def snow1():
    print("  *      * ")
    print("       *   ")
    print("*   *    * ")


def snow2():
    print("   *  *    ")
    print("  *      * ")
    print("       *   ")


def snow3():
    print("        *  ")
    print("   *  *    ")
    print("  *      * ")


def jump(speed):
    time.sleep(speed)
    os.system('cls')
    snow1()
    print("___________")
    print("   *       ")
    print("     O  *  ")
    print("  ___|___  ")
    print("  \\  |  / ")
    print("   o | o   ")
    print("    / \\ * ")
    print(" * /   \\  ")
    print("  /     \\ ")
    time.sleep(speed)
    os.system('cls')
    snow2()
    print("___________")
    print("    *      ")
    print("  o  O  o  ")
    print(" /___|___\\")
    print("     | *   ")
    print("     |     ")
    print(" *  / \\   ")
    print("   /   \\  ")
    print("  /     \\ ")
    time.sleep(speed)


def starting(speed):
    time.sleep(speed)
    os.system('cls')
    snow3()
    print("_o_______o_")
    print(" |   O * | ")
    print(" |___|___| ")
    print("     | *    ")
    print("     |     ")
    print(" *  / \\   ")
    print("   /   \\  ")
    print("  /     \\ ")


def pullup(speed):
    starting(speed)
    time.sleep(speed)
    os.system('cls')
    snow1()
    print("_o___0___o_")
    print("  \\__|__/ ")
    print("     | *    ")
    print("  *  |     ")
    print("    / \\   ")
    print("   /   \\  ")
    print("  /     \\ ")


def dip(speed):
    time.sleep(speed)
    os.system('cls')
    print("  *      * ")
    print("    *      ")
    print("  /\\_0_/\\  ")
    print("_o___|___o_")
    print("     | *   ")
    print(" *   |     ")
    print("    / \\   ")
    print("   / * \\  ")
    print("  /     \\ ")
    time.sleep(speed)
    os.system('cls')
    print("  *  0   * ")
    print("   / | \\  ")
    print("  / *|  \\ ")
    print("_o___|___o_")
    print("    / \\   ")
    print("   / * \\  ")
    print("  /    *\\ ")


def down(speed):
    time.sleep(speed)
    os.system('cls')
    print("    *      ")
    print("  *      * ")
    print("  /\\_0_/\\")
    print("_o___|___o_")
    print("  *  |     ")
    print("     |     ")
    print("   */ \\   ")
    print("   /   \\ *")
    print("  /     \\ ")
    time.sleep(speed)
    os.system('cls')
    snow2()
    print("_o___0___o_")
    print("  \\__|__/ ")
    print("  *  |     ")
    print("     |  *  ")
    print("    / \\  *")
    print(" * /   \\  ")
    print("  /     \\ ")
    starting(speed)


def vilkas(speed):
    pullup(speed*0.75)
    dip(speed*0.75)
    down(speed*0.75)

def ending(speed, name):
    time.sleep(speed)
    os.system('cls')
    snow1()
    print("___________")
    print(" o  *    o ")
    print(" |   O   | ")
    print(" |___|___| ")
    print("     | *   ")
    print("  *  |     ")
    print("    / \\   ")
    print("   /   \\  ")
    print("  /     \\ ")
    flex(speed, "", "", "", "")
    flex(speed, "", "", "", "")
    flex(speed, name + " sportuoja net žiemą.", "", "", "")
    flex(speed, name + " sportuoja net žiemą.", "", "", "")
    flex(speed, name + " sportuoja net žiemą.", "Būk kaip " + name + ".", "", "")
    flex(speed, name + " sportuoja net žiemą.", "Būk kaip " + name + ".", "", "")
    flex(speed, name + " sportuoja net žiemą.", "Būk kaip " + name + ".", "SU ŠVENTOM KALĖDOM!!!", "")
    flex(speed, name + " sportuoja net žiemą.", "Būk kaip " + name + ".", "SU ŠVENTOM KALĖDOM!!!", "")
    while True:
        flex(speed, name + " sportuoja net žiemą.", "Būk kaip " + name + ".", "SU ŠVENTOM KALĖDOM!!!", "P.S. kai užknis flexint, tai paspausk ctrl-c")


def flex(speed, msg1, msg2, msg3, msg4):
    time.sleep(speed)
    os.system('cls')
    snow2()
    print("___________")
    print(f"                     {msg1}")
    print(f" o   O   o           {msg2}")
    print(f" |___|___|           {msg3}")
    print(" *   |     ")
    print(f"     | *             {msg4}")
    print("    / \\   ")
    print("*  /   \\  ")
    print("  /     \\ ")
    time.sleep(speed)
    os.system('cls')
    snow3()
    print("___________")
    print(f"   *                 {msg1}")
    print(f"  o  O  o            {msg2}")
    print(f" /_^_|_^_\\           {msg3}")
    print("     |  *  ")
    print(f"     |               {msg4}")
    print("  * / \\   ")
    print("   /   \\  ")
    print("  /     \\ ")


if __name__ == '__main__':
    name = input('Vardas: ')
    sveikas(name)
    kacialke(name)

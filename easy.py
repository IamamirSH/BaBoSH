import numpy as np
import matplotlib.pyplot as plt
import getpass
"""This app has Copy Right and Just Create for Test and Project PLEASE don't copy this app\\This app create By amir shirbakht
email: amirshirbakht@gmail.com\\Telegram:@amir0912366"""

def passw():
    import getpass

    user = getpass.getuser()
    pwd = getpass.getpass(prompt='Enter the password->: ')

    if pwd == "Amir1385":
        print('Unlock!')
        pass

    else:
        print('You entered wrong password')
        passw()
passw()
def olgooha():
    def hesabi():
        import time

        num1 = float(input("adad az chand shorou mishe?\n-->: "))
        print("olgoo az", num1, 'shorou mishe')

        try:
            ran = int(input("Ta chand bar?\n-->: "))

        except ValueError:
            print('Please try again\n')
            hesabi()

        print("olgoo az", num1, 'shorou mishe\nva ta ', ran, 'bar edame perida mikone')

        b = float(input("ghadr nesbat chand bashe?\n-->: "))
        print("olgoo az", num1, 'shorou mishe\nva ta ', ran, 'bar edame perida mikone\nva ghadr nesbat', b, 'hast')

        num = num1

        list = []

        try:
            whi = int(input("chand omin adadesh?\n-->: "))
        except IndexError:
            print("Adad bishtar az tedad adad hast!\n")
            hesabi()

        print("olgoo az", num1, 'shorou mishe\n va ta ', ran, 'bar edame perida mikone\n va ghadr nesbat', b, 'hast va',
              whi, 'omin adadesh hesabmishe\n')

        #if whi > len(list):
         #   print("ERROR!\nplease try again..")
          #  hesabi()
        #print(num1)
        list.append(num1)

        for i in range(ran):
            num += b
            list.append(num)

        print("Please wait 2 sec...")
        time.sleep(2)

        print(list)

        print(whi,"omin adade list-->",list[whi-1])

        print("Sum List is-->", sum(list))

        print("Avarage List is-->", sum(list)/len(list))
        qq = input('Edame? Y/N\n-->')
        if qq == 'Y':
            print('ok')
            ques()

        else:
            print('Good bye-><-')
            quit()
        #que()

    def hendesi():
        import time

        num1 = float(input("adad az chand shorou mishe?\n-->: "))
        print("olgoo az",num1,'shorou mishe')

        try:
            ran = int(input("Ta chand bar?\n-->: "))

        except ValueError:
            print("Please try again!\n")
            hendesi()

        print("olgoo az", num1, 'shorou mishe\nva ta ',ran,'bar edame perida mikone')

        b = float(input("ghadr nesbat chand bashe?\n-->: "))
        print("olgoo az", num1, 'shorou mishe\nva ta ', ran, 'bar edame perida mikone\nva ghadr nesbat',b,'hast')

        num = num1
        list = []

        try:
            whi = int(input("chand omin adadesh?\n-->: "))

        except IndexError:
            print('Please try again!\n')
            hendesi()

        print("olgoo az", num1, 'shorou mishe\n va ta ', ran, 'bar edame perida mikone\n va ghadr nesbat', b, 'hast va',whi,'omin adadesh hesabmishe\n')


        #if whi > len(list):

         #   print("ERROR!\nplease try again..")
          #  hendesi()
            #print(num1)
        #if whi < len(list) or whi==len(list):


       #     pass

        list.append(num1)

        for i in range(ran):
            num *= b
            list.append(num)

        print("Please wait 4 sec...")
        time.sleep(4)

        print(list)

        print(whi, "omin adade list-->", list[whi - 1])

        print("Sum List is-->", sum(list))

        print("Avarage List is-->", sum(list) / len(list))
        #que()
        qq = input('Do you want continue? Y/N\n-->')

        if qq == 'Y':
            print('ok')
            ques()
        else:
            print('Good bye-><-')
            quit()

    def que():
        k = int(input("Hesabi->1\nhendesi->2\n-->: "))

        if k == 1:
            hesabi()
        elif k == 2:
            hendesi()


    que()
def ques():

    app = int(input("which one\nolgoo->1\nsahmi->2\nmoadele->3\n-->: "))

    if app == 1:
        olgooha()
    elif app == 2:
        sahmi()
    elif app == 3:
        moadeled2()
    else:
        print('ERROR!!!\nplease try again')
        ques()

def sahmi():
    print("welcome")

    try:
        a = int(input('please enter a->  '))
        b = int(input('please enter b->  '))
        c = int(input('please enter c->  '))

    except ValueError:
        print("bayad adad vared bokoni\ndobare talash bokon\n")
        sahmi()


    if a > 0:
        print("سهمی به سمت بالاست.")
    elif a < 0:
        print('سهمی رو به پایین است.')
    else:
        print('ERROR!!\nplease try again')
        sahmi()

    toolazmabda = (-b) / (2*a)
    arzazmabda = ((4 * a * c) - (b * b) / (4 * a))
    print('tool az mabda->: ', toolazmabda)
    print('arz az mabda ->: ', arzazmabda)

    de = ((b * b) - (4 * a * c))
    print("delta-> ", de)

    if de > 0:
        print("نمودار سهمی در ۲ نقطه محور طول هارا قطع میکند.")

    elif de == 0:
        print('نمودار سهمی با محور طول ها مماس است.\/')

    else:
        print('نمودار سهمی با محور طول ها برخورد نمیکند.')
    print('\n')

    ques()
def moadeled2():
    import math
    print('Solve the quadratic equation ax**2 + bx + c = 0')

    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    # calculate the discriminant

    d = (b ** 2) - (4 * a * c)

    if d > 0:
        sol1 = (-b - math.sqrt(d)) / (2 * a)
        sol2 = (-b + math.sqrt(d)) / (2 * a)
        print('The solution are {0} and {1}'.format(sol1, sol2))

    elif d == 0:
        sol1 = -b // (2 * a)
        print('The solution is {0} '.format(sol1))

    else:
        print('The equation has no answer')
    print('\n')
    ques()

ques()

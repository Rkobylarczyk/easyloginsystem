def loading_data(registrated):
    if registrated == "yes":
        login = input("Podaj mi swój login: ")
        password = input("Podaj mi swoje hasło ")

        with open("passy.txt", "r") as passyfile:
            if (login + "," + password + "\n") in passyfile.readlines():
                print("Siema, wbijaj")
            else:
                print("Wyjazd")

    else:
        print("Zarejestruj sie")

def checking(account):
    if account == "no":
        print("Załóż konto")

    if account == "yes":
        login = input("Podaj mi swój login: ")
        haslo = input("Podaj mi swoje hasło ")

        with open("passy.txt", "r") as passyfile:
            if (login + "," + haslo + "\n") in passyfile.readlines():
                print("Siema, wbijaj")
            else:
                print("Wyjazd")

def registration(declaration):
    if declaration == "yes":
        login = input("Jaki chcesz mieć login? ")
        print("Twoim loginem będzie: ", login, ".")

        password = input("Jakie chcesz miec haslo? ")

        file = open("passy.txt", "a")
        file.write(login)
        file.write(",")
        file.write(password)
        file.write("\n")
        file.close()

        print("Dzięki ryju, zarejestrowałeś się.")

    else:
        print("Nie to nie")

registrated = input("Czy jesteś zarejestrowany? ")
checking(registrated)

declaration = input("Czy chcesz założyć nowe konto? ")
if declaration == "yes":
    registration(declaration)
    account = input("Sprawdźmy, czy się zarejestrowałeś. Czy masz już konto? ")
    if account == "yes":
            checking(account)
else:
    print("Nie to nie")
from os import system
from colorama import Fore, Back, init
init(autoreset=True)
import locale
language = str(locale.getdefaultlocale())
while True:
    ln = int(language.find("es_"))
    if ln == 2:
        try:
            print(Back.GREEN + "F_calculatorNC")
            print("1.Calcular 2.'Acerca de'") 
            option = int(input("Opción: "))
            if option == 1:
                try:
                    entrada=str(input())
                    salida=eval(entrada)
                    print(Fore.CYAN + "El resultado es:", + salida)
                except ValueError:
                    print(Fore.RED + "ERROR")
                except SyntaxError:
                    print(Fore.RED + "ERROR")
                input()
            elif option == 2:
                print("F_calculatorNC es el sucesor de F_calculator, tiene")
                print("mejor desempeño y menos errores.")
                print(" Desarrollado por Fernado jelvez")
                print(Fore.BLUE + "Ver:1.1")
                print("Enter")
                input()
            else:
                print(Fore.RED + "ERROR: ELIJA UNA OPCIÓN VALIDA")
            system("cls")
            print("1.Volver a empezar 2.Salir")
            option = int(input("Opción: "))
            if option == 1:
                system("cls")
                continue
            elif option == 2:
                exit()
            else:
                print(Fore.RED + "ERROR: ELIJA UNA OPCIÓN VALIDA")
        except ValueError:
            print(Fore.RED + "ERROR: DEBE DAR EL NÚMERO DE LA OPCIÓN")
            print("Enter")
            input()
            system("cls")
    else:
        ln = int(language.find("en_"))
        if ln == 2:
            try:
                print(Back.GREEN + "F_calculatorNC")
                print("1.Calculate 2.'About'") 
                option = int(input("Option: "))
                if option == 1:
                    try:
                        entrada=str(input())
                        salida=eval(entrada)
                        print(Fore.CYAN + "The result is:", + salida)
                    except ValueError:
                        print(Fore.RED + "ERROR")
                    except SyntaxError:
                        print(Fore.RED + "ERROR")
                    input()
                elif option == 2:
                    print("F_calculatorNC is the successor F_calculator, it has")
                    print("better performance and fewer errors.")
                    print(" Developed by Fernado jelvez")
                    print(Fore.BLUE + "Ver:1.1")
                    print("Enter")
                    input()
                else:
                    print(Fore.RED + "ERROR: CHOOSE A VALID OPTION")
                system("cls")
                print("1.Star again 2.Exit")
                option = int(input("Option: "))
                if option == 1:
                    system("cls")
                    continue
                elif option == 2:
                    exit()
                else:
                    print(Fore.RED + "ERROR: CHOOSE A VALID ")
            except ValueError:
                print(Fore.RED + "ERROR: YOU MUST GIVE THE NUMBER OF AN OPTION")
                print("Enter")
                input()
                system("cls")

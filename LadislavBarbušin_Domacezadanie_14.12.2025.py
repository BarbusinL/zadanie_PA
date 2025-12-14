from abc import ABC, abstractmethod

#abstraktna trieda
######################################################################################
class zviera(ABC):
    def __init__(self, Vek, Velkost, Vaha, Domace):
        self.vek = Vek
        self.velkost = Velkost
        self.vaha = Vaha
        self.domace = Domace

    @abstractmethod
    def druh_pokrytia_tela(self):   # či má srsť, perie, šupiny
        pass

    @abstractmethod
    def druh(self):
        pass
    def prostredie(self):   # domáce alebo divé zviera
        return "Domáce" if self.domace else "Divé"
#podtriedy
######################################################################################
class Cicavec(zviera):
    def druh(self):
        return "Cicavec"
    def druh_pokrytia_tela(self):
        return "Srsť"

class Vtak(zviera):
    def druh(self):
        return "Vták"
    def druh_pokrytia_tela(self):
        return "Perie"

class Ryba(zviera):
    def druh(self):
        return "Ryba"
    def druh_pokrytia_tela(self):
        return "Šupiny"

class Plaz(zviera):
    def druh(self):
        return "Plaz"
    def druh_pokrytia_tela(self):
        return "Šupiny"

######################################################################################
def vypisanie_zvierata():
    while True:           # opakovanie pri zlej volbe
        print("Vyber druh zvieraťa:")
        print("1 => Cicavec")
        print("2 => Vtak")
        print("3 => Ryba")
        print("4 => Plaz")
        try:
            volba = int(input("Tvoja voľba: "))
            if volba not in [1, 2, 3, 4]:
                raise ValueError
        except ValueError:
            print("Zadal si neplatnú voľbu!")
            continue
#---------------------------------------------------------#
        print("-----------------------")
        print("Vyber spôsob života:")
        print("1 => Domáce zviera")
        print("2 => Divoké zviera")
        try:
            zivot = int(input("Tvoja voľba: "))
            if zivot not in [1, 2]:
                raise ValueError
        except ValueError:
            print("Zadal si neplatnu volbu!")
            continue
#---------------------------------------------------------#
        print("-----------------------")
        try:
            vek = int(input("Zadaj vek (počet rokov): "))
            velkost = float(input("Zadaj velkosť (m): ").replace(",", "."))
            vaha = float(input("Zadaj vahu (kg): ").replace(",", "."))
        except ValueError:
            print("Zle zadana hodnota!")
            continue
#---------------------------------------------------------#
        Domace = True if zivot == 1 else False

        if volba == 1:
            return Cicavec(vek, velkost, vaha, Domace)
        elif volba == 2:
            return Vtak(vek, velkost, vaha, Domace)
        elif volba == 3:
            return Ryba(vek, velkost, vaha, Domace)
        elif volba == 4:
            return Plaz(vek, velkost, vaha, Domace)

######################################################################################
def main():
    zviera = vypisanie_zvierata()

    print("-----------------------")
    print(f"Informácie o zvierati:")
    print(f"Druh: {zviera.druh()}")
    print(f"Vek: {zviera.vek}")
    print(f"Veľkosť: {zviera.velkost} m")
    print(f"Váha: {zviera.vaha} kg")
    print(f"Spôsob života: {zviera.prostredie()}")
    print(f"Druh pokrytia tela: {zviera.druh_pokrytia_tela()}")

if __name__ == "__main__":
    main()
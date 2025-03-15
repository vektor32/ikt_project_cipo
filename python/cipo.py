
class Cipok:
    def __init__(self,nev,gyarto,meret):
        self.__nev=nev
        self.__gyarto=gyarto
        self.__meret=meret

    def getNev(self):
        return self.__nev
    def getGyarto(self):
        return self.__gyarto
    def getMeret(self):
        return self.__meret
    def __str__(self):
        return f"{self.getNev()}-{self.getGyarto()}-{self.getMeret()}"

def beolvas():
    lista=[]
    with open("cipo.txt", "r", encoding="utf-8") as file:
        for sor in file:
            line=sor.strip().split("-")
            cipo=Cipok(line[0],line[1],int(line[2]))
            lista.append(cipo)
        return lista
    
def legtobb(lista):
    maxinev=lista[0]
    maxi=lista.count(maxinev)
    for i in range(1,len(lista)):
        if maxi< lista.count(lista[i]):
            maxi=lista.count(lista[i])
            maxinev=lista[i]
    return maxinev

def kirat(lista):
    nevek=[]
    maxigyarto=""
    for cipo in lista:
        nevek.append(cipo.getGyarto())
    maxigyarto=legtobb(nevek)
    with open("legtobb_cipo.txt","w",encoding="utf-8")as file:
        for cipo in lista:
            if maxigyarto in cipo.getGyarto():
                print(cipo, file=file)

lista=beolvas()

print("Adja meg 3 cipő nevét, márkáját és méretét.")
for i in range(0,3):
    nev=input(f"{i+1}. cipő neve: ")
    marka=input(f"{nev} márkája: ").capitalize()
    meret=int(input(f"{nev} mérete: "))
    lista.append(Cipok(nev,marka,meret))

kirat(lista)
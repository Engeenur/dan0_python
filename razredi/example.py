import copy

class Pravokotnik(object):
    #kot static variable v C-ju -> dostopas z object_name.variable_name (vsi objekti majo isto in ce enmu spremenis, spremenis vsem)
    barva = "rdeca"
    def __init__(self, a, b):
        #constructor
        self.a = a
        self.b = b
        print("To je pravokotnik. Njegovi stranici sta: " + str(self.a) + ", " + str(self.b))
        
    def ploscina(self):
        return self.a*self.b
    
    def obseg(self):
        return 2*(self.a + self.b)

    def __del__(self):
        #destructor
        #zazenemo z ukazom del object_name ali pa ko se program konca
        print("Bye bye pravokotnik.")

class Kvadrat(Pravokotnik):
    def __init__(self, a):
        super(Kvadrat, self).__init__(a, a)

class Student():
    def __init__(self, ime, vpisna_st, letnik):
        self.ocene = {}
        self.vpisna_st = vpisna_st
        self.ime = ime
        self.letnik = letnik
    
    def oceni(self, predmet, ocena):
        self.ocene[predmet] = ocena

    def napreduj(self):
        for predmet,ocena in self.ocene.items():
            if ocena < 6:
                print("Niste opravili predmeta: " + predmet +". Vas uspeh je: " + str(ocena))
                return False
        self.letnik += 1
        return True

class Fakulteta():
    def __init__(self):
        self.studenti = {}
    
    def vpis(self, student):
        self.studenti[student.ime] = {
            "vpisna stevilka" : student.vpisna_st,
            "letnik" : student.letnik,
            "ocene" : student.ocene
        }
    
    def izpis(self, student):
        self.studenti.pop(student.ime)
           

if __name__ == "__main__":
    #izvaja se samo ko klicemo direktno ta file ne ob vsakem importu
    prav = Pravokotnik(5,6)
    print(prav.a) #vrne v katerem programu je, kaksnega tipa je ter kje v spominu je
    del prav

    kvad = Kvadrat(7)
    print(kvad.ploscina())

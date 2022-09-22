import pickle

if __name__ == "__main__":
    #dolocimo iz kje bomo brali podatke s picklom in kaj bomo z datoteko pocel (r-read, b-binarno)
    h = open("tocka.pkl", 'rb')

    #povemo kaj hocemo pisat, kam in kaksno compresijo hocemo (optional)
    l1 = pickle.load(h)

    h.close()
    print(l1)
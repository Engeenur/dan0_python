import pickle

if __name__ == "__main__":
    l1 = [1, 2, 2, 6, 6, 7]
    
    #dolocimo kam bomo shranjeval podatke s picklom in kaj bomo z datoteko pocel (w-write, b-binarno)
    h = open("tocka.pkl", 'wb')

    #povemo kaj hocemo pisat, kam in kaksno compresijo hocemo (optional)
    pickle.dump(l1, h, pickle.HIGHEST_PROTOCOL)

    h.close()

    #bolj varno
    with open("tocka2.pkl", 'wb') as h:
        pickle.dump(l1, h, pickle.HIGHEST_PROTOCOL)
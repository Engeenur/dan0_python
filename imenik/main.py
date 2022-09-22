

def main():
    imenik = {
        "anica" : "031000000", 
        "stef" : "031000001", 
        "blaz" : "031000002",
        "andrej": "031000003",
        "cene": "031000004",   
        "boris": "031000005"
    }

    for k in imenik:
        if "ori" in k:
            print("Klicem " + k + ": " + imenik[k])


if __name__ == "__main__":
    main()
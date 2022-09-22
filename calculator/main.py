operacije = ("+", "-", "/", "*", "^")
operacija = input("Izberi racunsko operacijo (+,-,/,*,^): ")

while operacija not in operacije:
    print("Napacen vnos operacije.")
    operacija = input("Izberi racunsko operacijo (+,-,/,*,^): ")

stevilo1 = input("Vnesite prvo stevilo: ")
stevilo2 = input("Vnesite drugo stevilo: ")
rezultat_str = "Rezultat operacije je: "

if operacija == "+":
    rezultat = float(stevilo1) + float(stevilo2)
elif operacija == "-":
    rezultat = float(stevilo1) - float(stevilo2)
elif operacija == "/":
    rezultat = float(stevilo1) / float(stevilo2)
elif operacija == "*":
    rezultat = float(stevilo1) * float(stevilo2)
elif operacija == "^":
    rezultat = float(stevilo1) ** float(stevilo2)

print(rezultat_str + str(rezultat))
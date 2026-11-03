#!/usr/bin/env python3

def aendere_immutable_variable(x: int):
    print(f"Ursprünglicher Wert in der Funktion (immutable): {x}")
    print(f"    Speicheradresse: {id(x)}")
    x += 10  # Bei immutable Variablen wie int wird eine neue Speicheradresse verwendet
    print(f"Geänderter Wert in der Funktion (immutable): {x}")  
    print(f"    Speicheradresse: {id(x)}")
    return x  # Rückgabe des neuen Werts, um die Änderung zu reflektieren

zahl = 20
print(f"Vor Funktionsaufruf (immutable): {zahl}")
print(f"    Speicheradresse: {id(zahl)}")
zahl =aendere_immutable_variable(zahl)
print(f"Nach Funktionsaufruf (immutable): {zahl}, Speicheradresse: {id(zahl)}") 
print(f"    Speicheradresse: {id(zahl)}")

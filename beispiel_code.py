import sys
import gc

# Reference Count Beispiel
# Liste von Zahlen
x = [1, 2, 3]

print("Reference count of x:", sys.getrefcount(x))  # Gibt die Referenzanzahl von x aus

y = [3, 4, 5]
y.append(x)

print("Reference count of x:", sys.getrefcount(x))  # Gibt die Referenzanzahl von x aus

del y
print("Reference count of x:", sys.getrefcount(x))  # Gibt die Referenzanzahl von x aus

# Garbage Collection Beispiel
x = 2
del x
print(f"Garbage collector: {gc.collect()} Objekte.")



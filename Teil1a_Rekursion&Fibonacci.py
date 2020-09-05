# Ramon Zehnder
# Semesterarbeit Teil 1a: Rekursion mit Python anhand der Fibonacci-Folge
# STATUS: Version 0.5 - Work In Progress


### ------------BONUS - Exception Handler: Eingabe der gesuchten fib Zahl [n] durch Input-----------------

# Mit dem Input kann die gewünschte n-te Ziffer der Fibonacci-Folge dynamisch definiert werden.
def nteZahl():
    try:
        eingabe = int(input('Geben sie die n-te Zahl ein: ')) + 1
        fib(eingabe)
    # Der Exception Handler fangt falsche Eingaben ab und aktiviert die Funktion WrongInput
    except IndexError:
        WrongInput()
    except ValueError:
        WrongInput()

# Bei falscher Eingabe wird die Eingabe wiederholt und auf den Fehler aufmerksam gemacht
def WrongInput():
    print("Eingabe muss eine ganze Zahl grösser als '1' sein. Versuchen Sie es erneut.")
    nteZahl()

### ----------------fib Funktion1---------------------------------
# Aufgabe 1

def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)

# Beispiel: Ausgabe der 8ten Stelle von der Fibonacci-Folge
print(fib2(8))


### -------------fib Funktion2 Iterativ--------------------------
# Aufgabe 2 & 5

def fib(n):
    a, b = 0, 1
    # (n) wird in der Funktion nteZahl definiert

    for i in range(n):
        # Mit dem Befehl wird jedes mal der Wert  von a in die Liste c hinzugefügt.
        # Mit dieser Methode kann gleichzeitig die letzte Stelle der Fibonacci-Folge und die Anzahl Durchläufe (n) ermittelt werden.
        c.append(a)
        a, b = b, a + b

    # Gibt die n-te Zahl der Fibonacci-Folge bzw. die Letze Ziffer aus der Liste "c" aus.
    print(c[-1])
    # Mit dem Befehl kann mittels der Liste die Anzahl Durchläufe ausgelesen werden.
    print(len(c))

# c wird als leere Liste definiert um nachher mit der Fibonacci-Folge zu füllen.
c = []
nteZahl()

### -----------------timeit Timer für die Funktion fib(n)-----------------------------
# Aufgabe 4

import timeit

# Die Funktion fib(n) wird getimed.
# WORK IN PROGRESS
print(timeit.timeit("""def fib(n):
    a, b = 0, 1,
    for i in range(n):
        # Mit dem Befehl wird jedes mal der Wert  von a in die Liste c hinzugefügt
        c.append(a)
        # Fibonacci-Folge
        a, b = b, a + b""", number=1))








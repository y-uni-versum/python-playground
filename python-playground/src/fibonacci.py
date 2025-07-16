'''
## Aufgabe 1
Fibonacci-Folge (mit Funktion und for-Schleife):
Schreibe eine Funktion fibonacci(n), die die ersten n Zahlen der Fibonacci-Folge zurückgibt.
Die Fibonacci-Folge beginnt mit den Zahlen 0 und 1, und jede nachfolgende Zahl ist die Summe der beiden vorherigen Zahlen.
Verwende dann diese Funktion, um die ersten 10 Zahlen der Fibonacci-Folge auszugeben.

### Erklärung:
Die Fibonacci-Folge ist eine mathematische Sequenz von Zahlen,
bei der jede Zahl die Summe der beiden vorhergehenden Zahlen ist.
Die beginnt oft mit den Zahlen 0 und 1.

Mathematisch ausgedrückt lautet die Definition:
F(n)=F(n−1)+F(n−2)F(n)=F(n−1)+F(n−2)

Hierbei steht F(n)F(n) für die nn-te Zahl in der Fibonacci-Folge,
F(n−1)F(n−1) für die (n−1)(n−1)-te Zahl und F(n−2)F(n−2) für die (n−2)(n−2)-te Zahl.
Die Basisfälle sind F(0)=0F(0)=0 und F(1)=1F(1)=1.
Die ersten paar Zahlen der Fibonacci-Folge sehen so aus:
0,1,1,2,3,5,8,13,21,34,…
'''

fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(f'Zahlenfolge nach Fibonacci: {fibonacci(i)}')

print('---')


# Unittest mit Hilfe der Klasse Triangle

## Wie geht man vor?

a) Man erklaert den Schuelern das Problem der Dreiecksklasse.
Dazu gehoeren:
-> Namen der Fehlerklasse
-> Name der Klasse und der Methoden
-> zulaessige Werte fuer den Kontruktor (int, float)
-> alles was es fuer die Schnittstellen noch zu wissen gibt.

b) Hausaufgabe oder Schulaufgabe fuer die Schüler: Erstellen der Klasse Triangle

c) Beim naechsten Treffen koennen die Schueler mit der vom Lehrer ausgegebenen
Testklasse ihre Triangle-Klasse testen.

Nähere Infos zu den Problemen mit der Triangle-Klasse finden sich in der Praesentation
von Herrn Dr. Spillner.

```python
#--- Hinweise -----
class TriangleException(Exception):
	"""our own exception class"""

class Triangle:
	def __init__(self,a,b,c):
		"""Constr. triangle. Expects three sides."""

	def show(self):
		"""Showing the triangle including the two cathetuses and the hypotenuse."""

	def __str__(self):
		"""gets us a string-object representation"""

	def isIsosceles(self):
		"""Pruefen auf Gleichschenkligkeit"""
```



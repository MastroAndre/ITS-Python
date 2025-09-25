from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

p1: Paziente = Paziente("Andrea", "Rossi", "001")
p2: Paziente = Paziente("Giorgio", "Bianchi", "002")
p3: Paziente = Paziente("Mario", "Verdi", "003")
p4: Paziente = Paziente("Bruno", "Gialli", "004")

pazienti1: list[Paziente] = [p1, p2, p3]
pazienti2: list[Paziente] = [p4]

d1: Dottore = Dottore("Bau", "Bau", "Pediatra", 7.5)
d2: Dottore = Dottore("Miao", "Miao", "Ostetrico", 12.2)

d1.setAge(40)
d2.setAge(46)

d1.greet()
d2.greet()

fattura1: Fattura = Fattura(pazienti1, d1)
fattura2: Fattura = Fattura(pazienti2, d2)

print(f"\nSalario {d1}: {fattura1.getSalary()} euro")
print(f"Salario {d2}: {fattura2.getSalary()} euro")


fattura1.removePatient(p2)
fattura2.addPatient(p2)

print(fattura1.getSalary())
print(fattura2.getSalary())

print(f"\nIn totale l'ospedale ha incassato: {(fattura1.getSalary())+(fattura2.getSalary())} euro")
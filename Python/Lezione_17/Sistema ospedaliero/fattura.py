from dottore import Dottore
from paziente import Paziente

class Fattura:
    __patient: list[Paziente]
    __doctor: Dottore
    __fatture: int
    __salary: int

    def __init__(self, patient: list[Paziente], doctor: Dottore):
        if doctor.isAValidDoctor() == True:
            self.__doctor = doctor
            self.__patient = patient
            self.__fatture = len(patient)
            self.__salary = 0
        
        else:
            self.__patient = None
            self.__doctor = None
            self.__fatture = None
            self.__salary = None
            raise ValueError("Non è possibile creare la classe fattura poichè il dottore non è valido!")
        
    def getSalary(self) -> int:
        self.__salary = self.__doctor.getParcel() * len(self.__patient)
        return self.__salary
    
    def getFatture(self):
        self.__fatture = len(self.__patient)
        return self.__fatture
    
    def addPatient(self, newPatient: Paziente):
        self.__patient.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del dottor {self.__doctor.getLastName()} è stato aggiunto il paziente {newPatient.getIdCode()}")
    
    def removePatient(self, idCode: str):
        for p in self.__patient:
            if p.getIdCode() == idCode:
                self.__patient.remove(p)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del dottor {self.__doctor.getLastName()} è stato rimosso il paziente {idCode}")
        
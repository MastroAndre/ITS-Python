from persona import Persona

class Dottore(Persona):
    __specialization: str
    __parcel: float

    def __init__(self, first_name, last_name, specialization, parcel):
        super().__init__(first_name, last_name)
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            self.__specialization = None
            print("La specializzazione inserita non è una stringa")

        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            self.__parcel = None
            print("La parcella inserita non è un float")

    def setSpecialization(self, specialization):
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            self.__specialization = None
            print("La specializzazione inserita non è una stringa")
    
    def setParcel(self, parcel):
        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            self.__parcel = None
            print("La parcella inserita non è un float")

    def getSpecialization(self) -> str:
        return self.__specialization
    
    def getParcel(self) -> float:
        return self.__parcel
    
    def isAValidDoctor(self):
        if int(self.getAge()) > 30:
            print(f"Doctor {self.getName()} {self.getLastName()} is valid")
            return True
        else:
            print(f"Doctor {self.getName()} {self.getLastName} is not valid")
            return False

    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self.__specialization}")

    def __str__(self):
        return f"{self.getName()} {self.getLastName()}"
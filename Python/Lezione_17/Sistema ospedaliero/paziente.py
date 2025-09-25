from persona import Persona

class Paziente(Persona):
    __code: str

    def __init__(self, first_name, last_name, code):
        super().__init__(first_name, last_name)
        if isinstance(code, str):
            self.__code = code
        else:
            self.__code = None
    
    def setIdCode(self, IdCode):
        self.__code = IdCode

    def getIdCode(self) -> str:
        return self.__code
    
    def patientinfo(self):
        print(f"Paziente: {self.getName()} {self.getLastName()}\nID: {self.__code}")

    
class Persona:
    __first_name: str
    __last_name: str
    __age: int

    def __init__(self, first_name, last_name):
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            self.__first_name = None
            print("Il nome inserito non è una stringa")

        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            self.__last_name = None
            print("Il cognome inserito non è una stringa")

        if isinstance(first_name, str) and isinstance(last_name, str):
            self.__age = 0
        else:
            self.__age = None

    def setName(self, first_name):
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            raise ValueError("Il nome inserito non è una stringa!")
        
    def setLastName(self, last_name):
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            raise ValueError("Il cognome inserito non è una stringa!")
        
    def setAge(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError("L'età deve essere un numero intero")
    
    def getName(self) -> str:
        return self.__first_name
    
    def getLastName(self) -> str:
        return self.__last_name
    
    def getAge(self) -> str:
        return self.__age
    
    def greet(self) -> str:
        print(f"Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.__age} anni!")
        
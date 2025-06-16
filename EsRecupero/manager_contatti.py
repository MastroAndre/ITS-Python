class ContactManager:

    def __init__(self, contacts: dict[str, list[str]]) -> None:
        self.contacts = contacts

    def create_contact(self, name: str, phone_numbers: list[str]) -> dict[str, list[str]]:

        contatto: dict[str, list[str]] = {}
        contatto[name] = phone_numbers
        if name in self.contacts.keys():

            print("Errore: il contatto esiste già")
        
        else:
            self.contacts[name] = phone_numbers
            return contatto
    
    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:

        contatto: dict[str, list[str]] = {}
        contatto[contact_name] = self.contacts[contact_name]

        if contact_name not in self.contacts:
            print("Errore: il contatto non esiste")
        
        elif phone_number in self.contacts[contact_name]:
            print("Errore: numero già esistente")
        
        else:
            self.contacts[contact_name].append(phone_number)
            return contatto

    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:

        contatto: dict[str, list[str]] = {}
        contatto[contact_name] = self.contacts[contact_name]

        if contact_name not in self.contacts:
            print("Errore: il contatto non esiste")

        elif phone_number not in self.contacts[contact_name]:
            print("Errore: il numero non esiste")    

        else:
            self.contacts[contact_name].remove(phone_number)
            return contatto
        
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict[str, list[str]]:

        contatto: dict[str, list[str]] = {}
        contatto[contact_name] = self.contacts[contact_name]

        if contact_name not in self.contacts:
            print("Errore: il contatto non esiste")

        elif old_phone_number not in self.contacts[contact_name]:
            print("Errore: il numero non esiste") 

        else:
            self.contacts[contact_name].remove(old_phone_number)
            self.contacts[contact_name].append(new_phone_number)
            return contatto
        
    def list_contacts(self) -> list[str]:

        contatti: list[str] = []

        for key in self.contacts.keys():
            contatti.append(key)

        return contatti

    def list_phone_numbers(self, contact_name: str) -> list[str]:

        if contact_name not in self.contacts.keys():
            print("Errore: il contatto non esiste")

        else:
            return self.contacts[contact_name]
        
    def search_contact_by_phone_number(self, phone_number: str) -> list[str]:

        contatti: list[str] = []

        for key, value in self.contacts.items():
            if phone_number in value:
                contatti.append(key)

        if not contatti:
            print("Nessun contatto trovato con questo numero di telefono")

        else:
            return contatti  

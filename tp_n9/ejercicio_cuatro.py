class Contact:
    def __init__(self, name, phone, email):
        self.name=name
        self.phone=phone
        self.email=email
        
    def __str__(self):
        return f"Nombre: {self.name}, numero: {self.phone}, email: {self.email}"
        
class ContactList:
    def __init__(self):
        self.contacts=[]
    
    def new_contact(self):
        name=input("Nombre del contacto: ")
        phone=int(input("Numero del contacto: "))
        email=input("Email del contacto: ")
        contact=Contact(name, phone, email)
        self.contacts.append(contact)
        
    def contacts_list(self):
        if not self.contacts:
            print("La agenda esta vacia")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"Contacto {i}:\n{contact}")
                
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name==name:
                print("Contacto encontrado: \n", contact)
                return
            else:
                print(f"No se encontro ningun contacto con el nombre {name}")
                
    def update_contact(self, name, new_phone, new_email):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone=new_phone
                contact.email=new_email
                print("Contacto actualizado")
                return
            else:
                print(f"No se encontro ningun contacto con el nombre {name}")
                
    
def main():
    my_contact_list=ContactList()
    while True:
        print("\nMenu de la agenda: ")
        print("1. Añadir contacto")
        print("2. Lista de contacto")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Cerrar agenda")
        opc=input("Seleccione una opcion: ")
        
        if opc=="1":
            my_contact_list.new_contact()
        elif opc=="2":
            my_contact_list.contacts_list()
        elif opc=="3":
            name=input("Nombre del contacto a buscar: ")
            my_contact_list.search_contact(name)
        elif opc=="4":
            name=input("Nombre del contacto a editar: ")
            new_phone=input("Nuevo telefono: ")
            new_email=input("Nuevo email: ")
            my_contact_list.update_contact(name, new_phone, new_email)
        elif opc=="5":
            print("Agenda cerrada")     
            break
    
        else:
            print("Opcion no valida, porfavor seleccione una valida") 
            
            
main()  
        
            
        
    
        
        
        

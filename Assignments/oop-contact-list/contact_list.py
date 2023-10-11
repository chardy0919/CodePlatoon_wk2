class ContactList:
    def __init__(self, name, contacts):
        self.name = name
        self.contacts = contacts # a list of objects
    
    @property
    def get_name(self):
        return self.name
    
    @property
    def get_contacts(self):
        return self.contacts
    
    @get_contacts.setter
    def set_contacts(self, new_contacts):
        self.contacts = new_contacts
    
    @get_name.setter
    def set_name(self, new_name):
        self.name = new_name
    
    def add_contact(self, obj):
        self.contacts.append(obj)
    
    def remove_contact(self, name):
        for person in self.get_contacts:
            if person['name'] == str(name):
                self.contacts.remove(person)
    
    def find_shared_contacts(self, other_list):
        shared_list = []
        for people in self.get_contacts:
            if people in other_list.get_contacts:
                shared_list.append(people)
        return shared_list
            
    
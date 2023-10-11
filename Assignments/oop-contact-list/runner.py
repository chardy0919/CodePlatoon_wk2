from contact_list import ContactList
contacts = [{'name': 'Alice', 'number': '123-4567'}]
my_list = ContactList("my list", contacts)

my_list.remove_contact('Alice')
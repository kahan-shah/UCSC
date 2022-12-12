# Kahan Shah
# Assignment 8.2 Loadable Contact list with init and more fuctions
# This program takes a text file and finds the specific part of a person's contact information that was in the text file
# Acknowledgments: https://www.geeksforgeeks.org/interact-with-files-in-python/, https://www.youtube.com/watch?v=Uh2ebFW8OYM, once again my roomie Arin Gadre helping me fix the problem I had loading the file.

class ContactList:
    def __init__(self, filename):
    
        # Call the load_from_file function to get contacts
        self.__contacts = self.load_from_file(filename)  # __ to make it private

    # Opens the file that is given in reading mode and goes throught each line and splits the contactsand creates a dictionary out of it.
    def load_from_file(self, filename):
        result = {}
        with open(filename, mode="r", encoding="utf-8") as file:
            for contact in file:
                data = contact.strip().split("\t")
                contact_dict = {
                    "name": data[0],
                    "email": data[1],
                    "phone": data[2],
                    "address": data[3]
                }
                result[contact_dict["name"]] = contact_dict
        return result

    # This function checks if the name exists and returns their email
    def get_email(self, name):
        if self.__contacts.get(name, None) is not None:
            return self.__contacts.get(name).get("email")
        else:
            return None
    # This function checks if the name exists and gets their phone number
    def get_phone(self, name):
        if self.__contacts.get(name, None) is not None:
            return self.__contacts.get(name).get("phone")
        else:
            return None

# This function checks if the name exists and gets their address
    def get_address(self, name):
        if self.__contacts.get(name, None) is not None:
            return self.__contacts.get(name).get("address")
        else:
            return None
    def get_email_list(contact_list,names_list):
        lst=[]
        for i in names_list:
            if i in contact_list:
                lst.append(contact_list[i]["email"])
            else:
                print('Error: "{}" not found in the contact list'.format(i))
        return lst

    # This function makes a list out of all the phone numbers in the file
    def get_phone_list(contact_list,names_list):
        lst=[]
        for i in names_list:
            if i in contact_list:
                lst.append(contact_list[i]["phone"])
            else:
                print('Error: "{}" not found in the contact list'.format(i))
        return lst

    # This function makes a list out of all the addresses in the file
    def get_address_list(contact_list,names_list):
        lst=[]
        for i in names_list:
            if i in contact_list:
                lst.append(contact_list[i]["address"])
            else:
                print('Error: "{}" not found in the contact list'.format(i))
        return lst

    # This fuction creates a dictionary and adds the contacts
    def add_contact(self, data: tuple):  
        contact_dict = {
            "name": data[0],
            "email": data[1],
            "phone": data[2],
            "address": data[3]
        }
        self.__contacts[contact_dict["name"]] = contact_dict

    # This fuction removes contacts from the dictionary
    def remove_contact(self, name):
        if self.__contacts.get(name, None) is not None:
            del self.__contacts[name]

    # This fuction gets all the names
    def get_all_names(self):
        return [contact["name"] for contact in self.__contacts.values()]

    # This fuction gets all the email addresses
    def get_all_emails(self):
        return [contact["email"] for contact in self.__contacts.values()]
    # This fuction gets all the phone numbers
    def get_all_phones(self):
        return [contact["phone"] for contact in self.__contacts.values()]
    # This fuction gets all the home addresses
    def get_all_addresses(self):
        return [contact["address"] for contact in self.__contacts.values()]

    def display(self):
        for contact in self.__contacts.values():
            print("{}\t\t{}\t\t{}\t\t{}".format(contact.get("name"), contact.get("email"),
                                                contact.get("phone"), contact.get("address")))
    # Magic methods
    def __str__(self):
        return "Contacts ({}): {}.".format(len(self.__contacts), ", ".join(self.get_all_names()))



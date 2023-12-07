from faker import Faker
faker = Faker('pl_PL')

class Card:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

        # nadpisuję metodę __str__
    def __str__(self):
        return f"{self.name} {self.surname}"
        # dodaję metodę contact() 
    def contact(self):
        return f"Kontaktuję się z: {self.name} {self.surname}"
        # definiuję dynamiczny atrybut do zwracania długości imienia i nazwiska
    @property
    def label_lengh(self):
        return len(self.name) + len(self.surname) + 1

class BaseContact(Card):
    def __init__(self, priv_number, email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.priv_number = priv_number
        self.email = email
        
    def contact(self):
        print(f"Kontaktuję się z {self.name} {self.surname} pod numerem telefonu {self.priv_number}")

class BussinessContact(Card):
    def __init__(self, bussiness_number, company, occupation, email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bussiness_number = bussiness_number
        self.company = company
        self.occupation = occupation
        self.email = email

    def contact(self):
        print(f"Kontaktuję się z {self.name} {self.surname} pod numerem telefonu {self.bussiness_number}")

def create_contacts(card_type, card_quantity):
    if card_type == BaseContact:
        return [BaseContact(name=faker.first_name(), surname=faker.last_name(), priv_number=faker.phone_number(), email=faker.email()) for i in range(card_quantity)]
    else:
        return [BussinessContact(name=faker.first_name(), surname=faker.last_name(), bussiness_number=faker.phone_number(), company=faker.company(), occupation=faker.job(), email=faker.company_email()) for i in range(card_quantity)]

example_contact_list = create_contacts(BussinessContact, 3)
#[print(contact) for contact in example_contact_list]

example_contact_list[0].contact()
label = example_contact_list[0].label_lengh
print(f"Długość etykiety = {label}")
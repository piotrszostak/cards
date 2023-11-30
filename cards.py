from faker import Faker
faker = Faker('pl_PL')

class Card:
    def __init__(self, name, surname, company, occupation, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.occupation = occupation
        self.email = email
        
        # nadpisuję metodę __str__
    def __str__(self):
        return f"{self.name} {self.surname}; {self.email}"
        # dodaję metodę contact() 
    def contact(self):
        return f"Kontaktuję się z: {self.name} {self.surname}; {self.email}"
        # definiuję dynamiczny atrybut do zwracania długości imienia i nazwiska
    @property
    #jak wywołać? TODO 
    def full_name_lengh(self):
        return len(f"{self.name} {self.surname}")

five_fake_cards = [Card(name=faker.first_name(), surname=faker.last_name(), company=faker.company(), occupation=faker.job(), email=faker.company_email()) for i in range(5)]

by_name = sorted(five_fake_cards, key=lambda item: item.name)
by_surname = sorted(five_fake_cards, key=lambda item: item.surname)
by_email = sorted(five_fake_cards, key=lambda item: item.email)

def list_basic_info(list):
    for item in list:
        print(f"{item.name} {item.surname}, {item.email}")
#list_basic_info(by_name)

# list comprehension
#[print(name) for name in by_name]

# using * and sep parameter to print out list
#print(*by_surname, sep="\n")


def list_full_info(list):
    for item in list:
        print(f"{item.name} {item.surname} pracuje w {item.company} jako {item.occupation}, email: {item.email}")
#list_full_info(five_fake_cards)

#by_name[0].full_name_lengh()
from faker import Faker
faker = Faker('pl_PL')

class Card:
    def __init__(self, name, surname, company, occupation, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.occupation = occupation
        self.email = email
        
        # nadpisuję metodę __str__ INSTANCJI klasy Card, żeby wyświetlało się w konsoli jako string
    def __str__(self):
        return f'{self.name} {self.surname}; {self.email}'

five_fake_cards = [Card(name=faker.first_name(), surname=faker.last_name(), company=faker.company(), occupation=faker.job(), email=faker.company_email()) for i in range(5)]
print(five_fake_cards[0])
print(five_fake_cards)

def list_basic_info(list):
    for item in list:
        print(f"{item.name} {item.surname}, {item.email}")

#list_basic_info(faker_list)

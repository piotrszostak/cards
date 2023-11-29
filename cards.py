from faker import Faker
faker = Faker('pl_PL')

class Card:
    def __init__(self, name, surname, company, occupation, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.occupation = occupation
        self.email = email

person1 = Card(name='Teodozja', surname='Rutkowska', company='Club Wholesale', occupation='specjalista ds. administracji', email='teosia@mail.com')
person2 = Card(name='Dominika', surname='Pawłowska', company='La Petite Boulangerie', occupation='dyrektor ds. zakupów', email='dominikapawlowska@mail.com')
person3 = Card(name='Klara', surname='Duda', company='Al\'s Auto Parts', occupation='recepcjonistka', email='klara.duda@mail.com')
person4 = Card(name='Krzysztof', surname='Kowalski', company='Pelican Labs', occupation='laborant', email='krzysztof.kowalski@mail.com')
person5 = Card(name='Ewa', surname= 'Nowak', company='Saint Petersburg Brewery', occupation='specjalista ds. produkcji', email='ewa.nowak@mail.com')

persons = [person1, person2, person3, person4, person5]

def list_basic_info(list):
    for item in list:
        print(f"{item.name} {item.surname}, {item.email}")

list_basic_info(persons)

faker_list = []
def add_fake_card():
    for i in range(5):
        faker_list.append(Card(name=faker.name(), surname=faker.name(), company=faker.company(), occupation=faker.job(), email=faker.email()))

add_fake_card()
list_basic_info(faker_list)


# nadpisuję metodę __str__ klasy Card, żeby wyświetlało się w konsoli jako string
def __str__(self):
    return f"{self.name} {self.surname}, {self.email}"

print(person2)
from faker import Faker
from geraCsv import criaCsv

if __name__ == "__main__":
    l = Faker('pt_BR')

    listaNames  = []
    listaPhones = []

    quantidade = 100

    for _ in range(quantidade):
        a = l.name()
        b = l.cellphone_number()
        listaNames.append(a)
        listaPhones.append(b)

    result = criaCsv(listaNames, listaPhones, quantidade)
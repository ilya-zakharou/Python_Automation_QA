import random

from data.data import Person
from faker import Faker #установить библиотеку для генерации фальшивых данных. pip install faker.

faker_en = Faker('En')

def generator_person ():
    return Person(
        first_name=faker_en.first_name(),
        last_name=faker_en. last_name(),
        email=faker_en.email(),
        current_address=faker_en.address(), #address-рандом адрес.
        mobile=faker_en.msisdn(), #msisdn - генерит рандомные телефоные номера
        subject='English'
    )

def generated_file():
    path = rf'D:\PythonCourse\pythonProject1\text{random.randint(10,100)}.txt'
    file = open(path,'w')
    file.write(f'Hello File{random.randint(23,100)}')
    file.close()
    return path
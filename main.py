from collections import UserDict


def value_error_decorator(inner):
    def wraper(*args):
        try:
            return inner(*args)
        except ValueError:
            return 'ValueError'
    return wraper


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)
        self.name = name.title()


class Phone(Field):
    def __init__(self, phone: str()):
        super().__init__(phone)
        if len(phone) == 10 and phone.isdigit():
            self.phone = int(phone)
        else:
            raise ValueError


class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    @value_error_decorator
    def add_phone(self, phone: str):
        '''Phone number must be 10 numbers long'''
        if len(phone) == 10:
            self.phones.append(Phone(phone))
        else:
            self.value = phone

    @value_error_decorator
    def remove_phone(self, phone):
        '''Phone number must be 10 numbers long'''
        num_index = []
        if [num_index.append(self.phones.index(x)) for x in self.phones if x.phone == int(phone)]:
            self.phones.pop(*num_index)
        else:
            print(f'{phone} not detected')

    def edit_phone(self, old_phone, phone):
        '''Phone number must be 10 numbers long'''
        num_index = []
        if [num_index.append(self.phones.index(x)) for x in self.phones if x.phone == int(old_phone)]:
            self.phones.pop(*num_index)
            self.phones.insert(*num_index, Phone(phone))
        else:
            raise ValueError('Phone not detected')

    @value_error_decorator
    def find_phone(self, phone=None):
        '''Phone number must be 10 numbers long'''
        if phone is None:
            return ', '.join(str(x.phone) for x in self.phones)
        elif int(phone) in [x.phone for x in self.phones]:
            return Phone(phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        self.data = dict()

    def add_record(self, item):
        self.data[str(item.name)] = item

    def find(self, name):
        for key, value in self.data.items():
            if name == key:
                return value

    def delete(self, name):
        for key, value in self.data.items():
            if name == key:
                self.data.pop(key)
                break




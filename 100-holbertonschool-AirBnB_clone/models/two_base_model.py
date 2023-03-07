import json

class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'country': self.country
        }

    @classmethod
    def from_dict(cls, dict_):
        return cls(dict_['name'], dict_['age'], dict_['country'])

    def save_to_file(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def load_from_file(cls, file_path):
        with open(file_path, 'r') as f:
            dict_ = json.load(f)
        return cls.from_dict(dict_)

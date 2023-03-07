import uuid


class Carro:
    __objects = {}
    def __init__(self):
        self.id = uuid.uuid4()

    def __str__(self):
        return "{}".format(self.id)


new_objeto = Carro()
print(new_objeto)

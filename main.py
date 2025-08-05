users=['Toxir','Ali']
print(users[0])


def say_hello(name:str):
    return f'Assalom alaykum, {name}'
print(say_hello('Ali'))


class Car():
    def __init__(self,model:str,brand:str,price:float,color:str):
        self.model=model
        self.brand=brand
        self.price=price
        self.color=color
    
    def to_dict(self):
        return self.__dict__
        
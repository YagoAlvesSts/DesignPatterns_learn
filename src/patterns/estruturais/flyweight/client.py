from flyweight_factory import FlyweightFactory


def add_car_to_police_database(
    factory: FlyweightFactory, plates: str, owner: str,
    brand: str, model: str, color: str
) -> None:
    print("\n\nClient: Adicionando carro ao banco de dados. ")
    flyweight = factory.get_flyweight([brand, model, color])
    #O código do cliente armazena ou calcula o estado extrínseco e o transmite
    # aos métodos do flyweight.

    flyweight.operation([plates, owner])
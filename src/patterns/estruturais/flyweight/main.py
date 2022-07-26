from flyweight_factory import FlyweightFactory
from client import add_car_to_police_database




if __name__ == "__main__":
    """
    Flyweight: Exibindo o estado compartilhado ({s}) e único ({u})
    """

    from datetime import date
    today = date.today()
    print("Today's date:", today)

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweight()

    add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweight()



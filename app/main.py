class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[self.name] = self


def create_person_list(people_list: list) -> list:
    Person.people = {}

    persons = [Person(pupu["name"], pupu["age"]) for pupu in people_list]

    for pupu in people_list:
        person_instance = Person.people[pupu["name"]]

        wife_name = pupu.get("wife")
        if wife_name is not None:
            person_instance.wife = Person.people[wife_name]

        husband_name = pupu.get("husband")
        if husband_name is not None:
            person_instance.husband = Person.people[husband_name]

    return persons

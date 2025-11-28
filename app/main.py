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

    persons = [Person(p["name"], p["age"]) for p in people_list]

    for p in people_list:
        person_instance = Person.people[p["name"]]

        wife_name = p.get("wife")
        if wife_name is not None:
            person_instance.wife = Person.people[wife_name]

        husband_name = p.get("husband")
        if husband_name is not None:
            person_instance.husband = Person.people[husband_name]

    return persons
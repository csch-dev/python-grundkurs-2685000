from aufgaben_package.personen import Person

def test_init():
    person = Person("Carla", 47)
    assert person.name == "Carla"
    assert person.alter == 47

def test_str():
    person = Person("Carla", 47)
    assert str(person) == "Carla (47)"  

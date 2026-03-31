from smartphone import Smartphone


catalog = [
    Smartphone("Samsung", "S20", "+79109207711"),
    Smartphone("Realme", "10", "+79209108834"),
    Smartphone("Honor", "X7D", "+79991234576"),
    Smartphone("LG", "G10 lite", "+79309209911"),
    Smartphone("Apple", "16 pro", "+79209101111")]

for smartphone in catalog:
    print(f"{smartphone.name} - {smartphone.model}. {smartphone.number}")


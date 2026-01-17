from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79161234567"),
    Smartphone("Samsung", "Galaxy S21", "+79161234568"),
    Smartphone("Xiaomi", "Mi 11", "+79161234569"),
    Smartphone("Huawei", "P40", "+79161234570"),
    Smartphone("Nova", "Techno", "+79029608004")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model} - {phone.number}")
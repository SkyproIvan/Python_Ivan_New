from address import Address
from mailing import Mailing


from_address = Address("157810", "г. Кострома", "ул. Ленина", "д. 15", "кв. 65")
to_address = Address("156025", "г. Нерехта", "ул.Тургенева", "д. 5", "кв. 3")
Mail = Mailing(from_address, to_address, 1000, "123456789")

print(Mail)


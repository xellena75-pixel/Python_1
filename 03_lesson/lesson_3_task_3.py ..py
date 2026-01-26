
from Mailing import Mailing
from Address import Address

from_address = Address("660131", "Красноярск", "Ленина улица", "94", "501")
to_address = Address("692501", "Сосновоборск", "Курчатова проспект", "10", "1")

mailing = Mailing(to_address, from_address, 500, "ABCD1234")

mailing.print_mailing()

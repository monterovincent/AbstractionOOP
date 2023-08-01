from Abstractfulltimemplyee import FulltimeEmployee
from Abstrahouremploye import HourlyEmployee
from Abstrapayrollemp import Payroll

payroll = Payroll()
Abstractfulltimemployee = FulltimeEmployee('john','doe', 56788)
Abstractfulltimemployee2 = FulltimeEmployee('jane','doe', 56788)
Abstrahouremploye = HourlyEmployee('jenny','simith', 200, 50)
payroll.add(Abstractfulltimemployee)
payroll.add(Abstractfulltimemployee2)
payroll.add(Abstrahouremploye)


payroll.add(HourlyEmployee('ken','wills',223,3344))
payroll.add(HourlyEmployee('kevin','mills',47457, 565))

print(payroll.print())

class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  def bonus(self,amount):
    return (amount*self.salary)/100
  def tax(self,amount):
    return (amount*self.salary)/100
  def net_salary(self):
    return self.salary+self.bonus(10)-self.tax(5)
s1=Employee("sameera",30000)
bonus_result=s1.bonus(10)
print(bonus_result)
tax_result=s1.tax(5)
print(tax_result)
result=s1.net_salary()
print(result)
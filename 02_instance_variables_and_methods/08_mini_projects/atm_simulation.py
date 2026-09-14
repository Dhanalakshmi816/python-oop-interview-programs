class ATM:
  def __init__(self,name,number,balance,pin):
    self.name=name
    self.number=number
    self.balance=balance
    self.pin=pin
    self.transaction=0
  def deposit(self,amount):
    if amount>0:
      self.balance=self.balance+amount
      self.transaction=self.transaction+1
    else:
      print("insufficient balance")
  def withdraw(self,amount):
    if amount>0 and amount<=self.balance:
      self.balance=self.balance-amount
      self.transaction=self.transaction+1
    else:
      print("invalid withdraw")
  def verify_pin(self,pin):
    if self.pin==pin:
      return "pin verified"
    else:
      return "pin not verified"
  def transaction_count(self):
    return self.transaction 
s1=ATM("sameera","A101",10000,1234)
s1.deposit(5000)
print(s1.balance)
s1.withdraw(3000)
print(s1.balance)
result1=s1.verify_pin(1234)
print(result1)
result2=s1.transaction_count()
print(result2)

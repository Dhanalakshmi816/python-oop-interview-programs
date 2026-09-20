class BankAccount:
  def __init__(self,name,number,balance):
    self.name=name
    self.number=number
    self.__balance=balance
    self.__transactions=0
  def deposit(self,amount):
    if amount>0:
      self.__balance=self.__balance+amount
      self.__transactions=self.__transactions+1
    else:
      print("invalid balance")
  def withdraw(self,amount):
    if amount>0 and amount<=self.__balance:
      self.__balance=self.__balance-amount
      self.__transactions=self.__transactions+1
    else:
      print("insufficient balance")
  def transfer(self,other_account,amount):
    if amount>0 and amount<=self.__balance:
      self.__balance=self.__balance-amount
      self.__transactions=self.__transactions+1
      other_account.__balance=other_account.__balance+amount
      other_account.__transactions=other_account.__transactions+1
    else:
      print("transfer failed")
  def get_balance(self):
    return self.__balance
  def get_transaction(self):
    return self.__transactions
s1=BankAccount("sameera","A101",25000)
s2=BankAccount("rahul","A102",10000)
s1.deposit(5000)
s1.withdraw(3000)
s1.transfer(s2,7000)
result=s1.get_balance()
print(result)
result1=s1.get_transaction()
print(result1)
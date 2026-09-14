class ShoppingCart:
  def __init__(self,name,price,quantity):
    self.name=name
    self.price=price
    self.quantity=quantity
  def total_price(self):
    if self.price>0 and self.quantity>0:
      return self.price*self.quantity
    else:
      return "not posibble"
  def discount(self,percentage):
    if 0<=percentage<=100:
      return (percentage*self.total_price())/100
  def final_bill(self):
    return self.total_price()-self.discount(10)
s1=ShoppingCart("laptop",50000,2)
result1=s1.total_price()
print(result1)
result2=s1.discount(10)
print(result2)
result3=s1.final_bill()
print(result3)
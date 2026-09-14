class Product:
  def __init__(self,name,price,stock):
    self.name=name
    self.price=price
    self.stock=stock
  def increase(self,purchase):
    if purchase>0:
      self.stock=self.stock+purchase
  def decrease(self,sell):
    if sell>0 and sell<=self.stock:
      self.stock=self.stock-sell
    else:
      return "sale failed"
  def display(self):
    return self.stock
  def value(self):
    if 0<self.price:
      return self.price*self.display()
s1=Product("laptop",50000,10)
increase_result=s1.increase(5)
decrease_result=s1.decrease(3)
result=s1.display()
print(result)
value_result=s1.value()
print(value_result)

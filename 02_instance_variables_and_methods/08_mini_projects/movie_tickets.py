class MovieTicket:
  def __init__(self,name,seats,price,seats_book):
    self.name=name
    self.seats=seats
    self.price=price
    self.seats_book=seats_book
  def total_amount(self):
    if self.seats_book<=self.seats:
      return self.price*self.seats_book
    else:
      return "booking failed"
  def remaining(self):
    if self.seats_book<=self.seats:
      return self.seats-self.seats_book
    else:
      return self.seats
s1=MovieTicket("avatar",20,300,25)
result1=s1.total_amount()
print(result1)
result2=s1.remaining()
print(result2)
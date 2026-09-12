class Student:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
  def total(self):
    sum=0
    for i in self.marks:
      sum=sum+i
    return sum
  def average(self):
    return self.total()/len(self.marks)
  def highest(self,students):
    name=" "
    largest=0
    for i in students:
      if i.average()>largest:
        largest=i.average()
        name=i.name
    return name
s1=Student("sameera",[80, 75, 90])
s2=Student("Rahul",[70, 80, 85])
s3=Student("Priya",[90, 95, 88])
students=[s1,s2,s3]
result=s1.total()
result1=s1.average()
print(result1)
result2=s2.average()
print(result2)
result3=s3.average()
print(result3)
topper=s1.highest([s1,s2,s3])
print(topper)
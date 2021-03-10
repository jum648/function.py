
def courses(*args):
  for subject in args:
    print(subject)
courses("Big Data","CCNA","OOP2")

def courses(*args):
  for subject in args:
    return subject
print(courses("Big Data","CCNA","OOP2"))

def courses(**kwargs):
  for key, value in kwargs.items():
    print("{}:{}" .format(key,value))
courses(first='big data',second='CCNA',third='HCIA')

def kenya(county="Mommbasa"):
  print("I am from" +county)
kenya()
kenya("Nairobi")
kenya("Kiambu")
kenya("Bungoma")

def my_function(food):
  for x in food:
    print(x)
fruits=["apple","banana","cherry"]
my_function(fruits)
















# class

class Service:

     ## 1
     secret = "영구는 배꼽이 두 개다."

     ## 2
     def sum(self, a, b):
          result = a + b
          print("%s + %s = %s입니다." % (a, b, result))

#########################################

class Service:
	secret = "영구는 배꼽이 두 개다!!!!"
	def setname(self, name):
		self.name = name
	def sum(self, a, b):
		result = a + b
		print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))

#########################################

class Service:
	secret = "영구는 배꼽이 두 개다!!!!"
	def __init__(self, name):
		self.name = name
	def sum(self, a, b):
		result = a + b
		print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))
		
#########################################

class FourCal:
     def setdata(self, first, second):
          self.first = first
          self.second = second

     def sum(self):
          result = self.first + self.second
          return result

     def mul(self):
          result = self.first * self.second
          return result

     def sub(self):
          result = self.first - self.second
          return result

     def div(self):
          result = self.first / self.second
          return result

#########################################

### "Differences between None __init__ and __init__"

class HousePark:
     lastname = "박"
     def setname(self, name):
          self.fullname = self.lastname + name
     def travel(self, where):
          print("%s, %s여행을 가다." % (self.fullname, where))

class HousePark:
     lastname = "박"
     def __init__(self, name):
          self.fullname = self.lastname + name

     def travel(self, where):
          print("%s, %s 여행을 가다." % (self.fullname, where))

### "상속(Inheritance)"

class HouseKim(HousePark):
	lastname = "김"

### "오버라이딩(Overriding)"

class HousePark:
     lastname = "박"

     def __init__(self, name):
          self.fullname = self.lastname + name

     def travel(self, where):
          print("%s, %s으로 여행을 갔다." % (self.fullname, where))

     def love(self, other):
          print("%s, %s 사랑에 빠졌다." % (self.fullname, other.fullname))

	## __add__ 함수 => pey + juliet
     def __add__(self, other):
          print("%s, %s 결혼했다." % (self.fullname, other.fullname))

     def fight(self, other):
          print("%s, %s 싸웠다." % (self.fullname, other.fullname))

	## __sub__ 함수 => pey - juliet
     def __sub__(self, other):
          print("%s, %s 이혼했다." % (self.fullname, other.fullname))


class HouseKim(HousePark):
     lastname = "김"

     def travel(self, where, day):
          print("%s, %s으로 %d일 여행을 갔다." % (self.fullname, where, day))


pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.travel("부산")
juliet.travel("부산", 3)
pey.love(juliet)
pey + juliet
pey.fight(juliet)
pey - juliet


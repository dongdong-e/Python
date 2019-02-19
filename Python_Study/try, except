try:
     f = open('foo.txt', 'r')
except FileNotFoundError as e:
     print(str(e))
else:
     data = f.read()
     f.close()
     
###Error Pass#########################

try:
     f = open("나없는파일", 'r')
except FileNotFoundError:
     pass

###NotImplementedError#########################

class Bird:
     def fly(self):
          raise NotImplementedError

class Eagle(Bird):
     def fly(self):
          print("very fast")

eagle = Eagle()
eagle.fly()

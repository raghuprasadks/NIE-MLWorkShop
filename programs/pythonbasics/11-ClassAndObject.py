#Class
class myClass():    
    def method1(self):
        print("myClass:method1")
    def method2(self, name):
        print("myClass:method2:Name " , name)


mc = myClass()
mc.method1()
mc.method2("raghu")

print(__name__)

def main():
    # exercise the class methods
    c = myClass()
    c.method1()
    c.method2("Python")
    
    c1 = myClass()
    c1.method1()
    c1.method2("Machine Learning")
if (__name__ == "__main__"):
    main()
    
class student():
    def register(self,regno,name,standard,section):        
        self.regno = regno
        self.name = name
        self.standard = standard
        self.section = section
        
    def information(self):
        print('Regno ',self.regno,' Name ',self.name,' Standard ',self.standard,' Section ',self.section)
        
bhavikaa = student()
bhavikaa.register(101,'Bhavikaa','9','A')
bhavikaa.information()
shloka = student()
shloka.register(102,'Shloka','9','C')
shloka.information()

print('Enter student information')
regno = int(input('Enter Registration Number'))
name = input('Enter your name')
std = int(input('Enter your standard'))
sec = input ('Enter your section')
newstd = student()
newstd.register(regno,name,std,sec)
newstd.information()
   
class Animal:
    def eat(self):
        print('Eating')
        
class Dog(Animal):
    def bark(self):
        print('Barking')
d= Dog()
d.eat()
d.bark()
#Multi level
class Animal:
    def eat(self):
        print('Eating')
class Dog(Animal):
    def bark(self):
        print('Barking')
class BabyDog(Dog):
    def weep(self):
        print('Weeping ')
d= BabyDog()
d.eat()
d.bark()
d.weep()

#Inheritance
class myClass():
    def method1(self):
        print("Parent:method1")
    def method2(self, name):
        print("Parent Method 2 :",name)
    def method3(self,city):
        print ("You are from ", city)
#class childClass():
class childClass(myClass):
    def method1(self):
        #myClass.method1(self)
        print("ChildClass:method1")
    def method2(self):
        print("childClass:method2")
def main():
    # exercise the class methods
    c2 = childClass()
    c2.method1()
    c2.method2()
    c2.method3("Bengaluru")
if (__name__ == "__main__"):
    main()
    
    
    
class Bank():
   def __init__(self,name,address,noOfBranch):
       print('init of bank')
       self.name = name
       self.address = address
       self.noOfBranch = noOfBranch
       print ('bank details :name ',self.name,' address : ',self.address,' no of branches ',self.noOfBranch )
       
   def rateOfInterest(self):
       return 0
   
   def calculateInterest(self,p,r,t):
       return p*r*t/100

class SBI(Bank):
   def __init__(self,name,address,noOfBranch):
       print('init of sbi')
       Bank.__init__(self,name,address,noOfBranch)
       
   def rateOfInterest(self):
       print('interest rate of sbi')
       return 6

class Karnataka(Bank):
    def __init__(self,name,address,noOfBranch):
        print('init of Karnataka')
        Bank.__init__(self,name,address,noOfBranch)
       
    def rateOfInterest(self):
        print('interest rate of Karnataka')
        return 6.5

sbi = SBI('State Bank of India','Nariman point,Mumbai',1000)
roi = sbi.rateOfInterest()
interest =sbi.calculateInterest(100000,roi,1)
print('interest from sbi is ',interest)
 
kar = Karnataka('Karnataka Bank','Nehru Road,Mangaluru',1003)
roi = kar.rateOfInterest()
interest =kar.calculateInterest(100000,roi,1)
print('interest from karnataka bank is ',interest)


class vehicle():
    def __init__(self,make,model,yom,vtype,price,speed,stype):
        self.make = make
        self.model = model
        self.yom = yom
        self.vtype = vtype
        self.price = price
        self.speed = speed
        self.stype = stype
        
    def start(self):
        self.speed = 0
        self.sype = "Kick Start"
        
    def accelerate(self):
        self.speed = 0
    
    def stop(self):
        self.speed = 0
    
    def info(self):
        return " Make : ",self.make ," Model ",self.model
    
class bike(vehicle):
    def start(self):
        self.speed = 0
        self.sype = "Button Start"
    def accelerate(self):
        self.speed = self.speed + 5
        
        
class car(vehicle):
    def __init__(self,make,model,yom,vtype,price,speed,stype,ac):
        vehicle.__init__(self,make,model,yom,vtype,price,speed,stype)
        self.ac = ac
           
    def start(self):
        self.speed = 0
        self.sype = "Button Start"
    def accelerate(self):
        self.speed = self.speed + 10
    def info(self):
        self.commoninfo = vehicle.info(self)
        return self.commoninfo + ' AC :',self.ac

himalayan = bike('Royal Enfield ','Himalayan',2020,'petrol',200000,160,'Kick start')
himalayan.start()
himalayan.accelerate()
himalayan.stop()
himalayan.info()


class ipl():
    def __init__(self,name,team,runs,wickets):
        self.name = name
        self.team = team
        self.runs = runs
        self.wickets = wickets
    def info (self):
        return 'IPL Players : Name ',self.name, ' Team : ',self.team
iplplayers = []
vk = ipl('Virat','RCB',890,0)
iplplayers.append(vk)
kl = ipl('K Rahul','XXIP',590,0)
iplplayers.append(kl)
bumrah = ipl('Bumrah','MI',59,19)
iplplayers.append(bumrah)
jadeja = ipl('Jadeja','CSK',465,12)
iplplayers.append(jadeja)
max = 0
maxrungetter = ''
for i in iplplayers:
    print ('Name ', i.name,' runs : ',i.runs,' wickets ',i.wickets)
    if (i.runs > max):
        max = i.runs
        maxrungetter = i.name        
print('maximum runs ',max)
print('maximum run getter  ',maxrungetter)


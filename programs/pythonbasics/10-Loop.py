#Loop - while
def whileLoop():
    x=1
    while(x<=20):
        print('Number is ',x)
        x = x+1
    print(x)
whileLoop()
#Loop - for loop
def forLoop():
#   x=0
    for x in range(30,0,-3):
        print('For Loop ',x)
forLoop()

def forLoop1():
#   x=0
    for x in range(1,11,2):
        print('For Loop ',x)
forLoop1()

def forLoop2():
#   x=0
    for x in range(10,1,-2):
        print('For Loop ',x)
forLoop2()


#Loop - for loop String
def forLoopString():
    months = ['january','February','March','April','May','June','July','August','September','October','November','December']
    for m in months:
        print ('Months ', m)
forLoopString()
#Break
def forLoopWithBreak():
    #x=0
    for x in range(1,11):
        if(x==8):
            break
        print('For Loop with break',x)
forLoopWithBreak()
#Continue
def forLoopWithContinue():
#    x=0
    for x in range(1,11):
        if(x==8):
            continue
        print('For Loop with continue ',x)
forLoopWithContinue()
#Enumerate
def enumerateSample():
    months = ['january','February','March','April','May','June','July','August','September','October','November','December']
    for i,m in enumerate(months):
        print ('Months : i : ', i+1, ' : m ',m)
enumerateSample()
#Repeate same statement
def repeatSame():
    for i in '134567894556':
        print("Numbers", i)
repeatSame()
def repeatSame():
    for i in 'RAGHU':
        print("Alphabets", i)
repeatSame()


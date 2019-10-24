print("Value of __name__",__name__)

def youCanCallMe():
    print('You can call me')
    print('This is the second statement')

print('This is the third statement')
def evenOrOdd(num1):
    if(num1%2==0):
        print(num1,' is even ')
        print('testing indentation if')                  
    else:
        print(num1, ' is odd ')
        print('testing indentation else')        
evenOrOdd(9)

def addition(num1,num2):
    sum = num1 + num2;
    print('sum of ',num1, ' , ',num2,' is ',sum)
addition(10,15)

def subtraction():
    num1 = 17
    num2 = 10
    result = num1-num2
    print('result is ',result)
subtraction()

def multiplication(num1,num2):
    result = num1 * num2
    return result
res = multiplication(100,3)
print('result of multiplication is ',res)

def simpleInterest(p,r,t):
    i=(p*r*t)/100
    return i
interest = simpleInterest(10000,6,1)
print('interest is ',interest)
    


def main():
    print ('This is from main function')
    youCanCallMe()

if(__name__=='__main__'):
    main()
print ('Another statement')


'''
# c

import <stdio.h>

int main()
{
	
}

# java


public class MyClass{
	
	public static void main(String args[])
	{

	}
}
'''
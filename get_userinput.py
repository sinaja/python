
#define a class for an Input
class Input:
    #member variable which stores the input value
    ip = ''
    #Base Class GetInput method uses the keyboard to get input from end user and stores it in 'ip'
    def GetInput(self):
      self.ip =   input("please type any old string: ")    
    #Simple method to print the input value stored in ip
    def Print_Input(self):
        print(self.ip)    

# define a test class which inherits from the Input class (this makes it the same Type as the Input Class) - this is knows as a Derived Class
# the drived class (testInput) can redefine (override) the GetInput module already defined in the base class (Input Class)
class testInput(Input):
    #Drived Class uses a teststring instead of keyboard input
    def GetInput(self):
        self.ip = "TestString"

#define a module (get_userinput) to get input such that you have to pass an Input Type as argument (so this can be either Input OR testInput)
#this technique is called Dependency Injection (inject the dependency as an argument - so you can control the behaviour of what your code depends on)
#def get_userinput(Input):
 #   Input.GetInput()
  #  Input.Print_Input() 

#Use myInput = Input() in the module 
#Use myInput = testInput() in unit tests 
#myInput = testInput()
#get_userinput(myInput)
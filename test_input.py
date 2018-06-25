import unittest
import get_userinput
    
# define a test class which inherits from the Input class (this makes it the same Type as the Input Class) - this is knows as a Derived Class
# the drived class (testInput) can redefine (override) the GetInput module already defined in the base class (Input Class)
class testInput(get_userinput.Input):
    #Drived Class uses a teststring instead of keyboard input
    def __init__(self, testData):
        self.ip = testData
    
    def GetInput(self):
        return self.ip 


class Test(unittest.TestCase):
    def test_input(self):
        MyInput = testInput('TestString1')
        #get_userinput.get_userinput(MyInput)
        self.assertEqual(MyInput.ip,'TestString1')
        print (MyInput.ip)

if __name__ =='__main__':
    unittest.main()



class StringManipulator:
    def __init__(self):
        self.text = ""


    def getString(self):
        self.text = input("Enter a String: ")

    def printString(self):
        print("Uppercase String: ", self.text.upper())


def test_class():
    obj = StringManipulator()
    obj.getString()
    print("Output: ")
    obj.printString()

test_class()
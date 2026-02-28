class Animal:
    def speak(self):
        print("animal makes sound...")

class dog(Animal):
    def speak(self):
        print("dog barks")

class cat(Animal):
    def speak(self):
        print("cat makes meowww")


A = Animal()
D = dog()
C = cat()

A.speak()
D.speak()
C.speak()
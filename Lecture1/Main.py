from classes import Myclass, AnotherClass

def main():
    print("===== Starting Class Demonstration =====\n")

    # Create instances
    obj1 = Myclass()
    obj2 = AnotherClass("Hi, I am AnotherClass instance!")

    # Accessing class and instance variables
    print(f"obj1.myvariable = {obj1.myvariable}")
    print(f"obj2.myvariable = {obj2.myvariable}")
    print(f"Myclass.common = {Myclass.common}\n")

    # Modify and demonstrate effects on instances
    obj1.common = 99
    Myclass.common = 42

    print("--- After modifications ---")
    print(f"obj1.common (instance variable) = {obj1.common}")
    print(f"obj2.common (class variable) = {obj2.common}")
    print(f"Myclass.common = {Myclass.common}\n")

    # Demonstrate function behavior
    result1 = obj1.myfunction(5, 10)
    result2 = obj2.myfunction(2, 3)
    print(f"obj1.myfunction(5,10) returned: {result1}")
    print(f"obj2.myfunction(2,3) returned: {result2}\n")

    # Add a custom property dynamically
    obj2.new_property = "Dynamic attribute example"
    print(f"obj2.new_property: {obj2.new_property}")

    print("\n===== Class Demonstration Completed =====")

if __name__ == "__main__":
    main()

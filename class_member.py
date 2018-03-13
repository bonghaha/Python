class Cs:
    @staticmethod
    def static_method():
        print("Static method")

    @classmethod
    def class_method(cls):
        print("Class method")

    def instance_method(self):
        print("instance_method")


Cs.static_method()
Cs.class_method()
i = Cs()
i.instance_method()

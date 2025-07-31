class CustomString:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return CustomString(self.value + other.value)

    def __mul__(self, times):
        return CustomString(self.value * times)

    def to_uppercase(self):
        return self.value.upper()

    def __str__(self):
        return self.value
    
s1 = CustomString("Anudip")
s2 = CustomString("Foundation")
s3 = s1 + s2
print(s3)
print(s3 * 2)
print(s3.to_uppercase())

# a class, which have a class parameter and have a same instance parameter

class laptop_info:
    brand_name = "Laptop Information"

    def __init__(self, brand_name=None):
        self.brand_name = brand_name


s = laptop_info("SONY VAIO")
print("%s: Branded as %s" %(laptop_info.brand_name, s.brand_name))

d = laptop_info()
d.brand_name = "DELL INSPIRON"
print("%s: Branded as %s" %(laptop_info.brand_name, d.brand_name))


# =========================

class Car:
    name = "CAR"

    def __init__(self, name=None):
        self.name = name


honda = Car("Honda")
print("%s name is %s" % (Car.name, honda.name))

toyota = Car()
toyota.name = "Toyota"
print("%s name is %s" % (Car.name, toyota.name))

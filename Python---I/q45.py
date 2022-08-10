# class named American which has a static method called printNationality.

class American(object):
    @staticmethod
    def printNationality():
        print("America")

anAmerican = American()
anAmerican.printNationality() # this will not run if @staticmethod does not decorates the function.
                              # Because the class has no instance.
American.printNationality()   # this will run even though the @staticmethod
                              # does not decorate printNationality()
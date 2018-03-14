class Person(object):
    def __init__(self, name, education):
        self.name = name
        self.education = education

    def work(self):
        print('%s goes to work.' % self.name)


class Employee(Person):
    def __init__(self, name, education, employer):
        super(Employee, self).__init__(name, education)
        self.employer = employer

    def work(self):
        print('%s goes to work for %s' % self.name, self.employer)


class Programmer(Employee):
    def __init__(self, name, education, employer, program):
        super(Programmer, self).__init__(name, education, employer)
        self.program = program

    def work(self):
        print("%s is working with %s for %s." % self.name, self.program, self.employer)

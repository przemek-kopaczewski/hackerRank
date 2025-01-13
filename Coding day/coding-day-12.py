class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, id, scores):
        super().__init__(firstName, lastName, id)
        self.id = self.idNumber
        self.scores = scores

    def calculate(self):
        if 90 <= sum(self.scores)/len(self.scores) <= 100:
            return 'O'
        elif 80 <= sum(self.scores)/len(self.scores) < 90:
            return 'E'
        elif 70 <= sum(self.scores)/len(self.scores) < 80:
            return 'A'
        elif 55 <= sum(self.scores)/len(self.scores) < 70:
            return 'P'
        elif 40 <= sum(self.scores)/len(self.scores) < 55:
            return 'D'
        elif sum(self.scores)/len(self.scores) < 40:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.diffrences = []
        for element1 in range(len(self.__elements)):
            for element2 in range(element1+1, len(self.__elements)):
                self.diffrences.append(abs(self.__elements[element1]-self.__elements[element2]))
        return self.diffrences

    @property
    def maximumDifference(self):
        return max(self.computeDifference())

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
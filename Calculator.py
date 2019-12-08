import re
class DoComplex:
    def __init__(self, x=0 + 0j, y=0 + 0j):
        self.x = x
        self.y = y * 1j
        self.z = self.x + self.y

    def GetValue(self):
        print(self.z)

    def ImagPart(self):
        print(self.x)

    def RealPart(self):
        print(self.y)

    def Add(self, comone=0, comtwo=0):
        print(comone, comtwo)
        self.z = comone + comtwo
        print(self.z)
        return self.z

    def Multiply(self, comone=0, comtwo=0):
        self.z = comone * comtwo
        print(self.z)
        return self.z


whatnext = "5"
arr = ["", "", "", "", ""]
g = 0
m = 0
i = 0

while (whatnext != 3):
    print("What you want to do now")
    print("1.Create new complex number")
    print("2.Calculator")
    print("3.End")
    whatnext = input("Select a number")
    if whatnext == 1:
        re = input("Real Part:")
        im = input("Imaginary Part:")
        k = DoComplex(int(re), int(im))
        k.GetValue()
    if whatnext == 2:
        equation = str(input("Put your equation here each element separeted by space: "))
        equation = equation.replace(" ", "")
        if (equation.__contains__("j")):
            print ("Im here2")
            numbers = equation.replace("+"," ")
            numbers = numbers.replace("-"," ")
            numbers = numbers.replace("*"," ")
            numbers = numbers.replace("/"," ")
            numbers = numbers.split(" ")
            signs = re.split("[0-9]",equation)
            print(equation)
            z = signs.__contains__("")
            while z is True:
                print(signs)
                signs.remove("")
                z = signs.__contains__("")
            le = signs.__len__()
            p = range(le)
            sums = 0
            for s in p:
                if s == 0:
                    if signs[s] == "+":
                        sums = numbers[s]+numbers[s+1]
                    if signs[s] == "-":
                        sums = numbers[s]-numbers[s+1]
                    if signs[s] == "/":
                        sums = numbers[s]/numbers[s+1]
                    if signs[s] == "*":
                        sums = numbers[s]*numbers[s+1]
                else:
                    if signs[s] == "+":
                        sums = sums+numbers[s+1]
                    if signs[s] == "-":
                        sums = sums-numbers[s+1]
                    if signs[s] == "/":
                        sums = sums/numbers[s+1]
                    if signs[s] == "*":
                        sums = sums*numbers[s+1]
            print(equation)
        else:
            for c in equation:
                if (((c != "*") and (c != "-") and (c != "+")) or i == 0):
                    arr[g] += c
                elif (c == "*"):
                    m = 1
                    g += 1
                else:
                    g += 1
                    arr[g] += c
                i += 1
            print(arr)
            comone = complex(arr[0] + arr[1])
            comtwo = complex(arr[2] + arr[3])
            l = DoComplex()
            if (m == 1):
               l.Multiply(comone, comtwo)
            else:
                l.Add(comone, comtwo)
            print(l.z)

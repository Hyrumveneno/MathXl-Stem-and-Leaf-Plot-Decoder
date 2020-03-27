#!/usr/bin/python3
"""
(c) Hyrum Baker 2020
Hyrumveneno@gmail.com
"""

## The string of numbers
## Replace the numbers in there with a paste. Numbers can range 0-109.
x = """
1
0
00
2
10
15
17
2
5
3
7
79
55
66
22
88
89
98
99
44
22
34
100
108
23
"""

## Making the lists
x_0 = []
x_1 = []
x_2 = []
x_3 = []
x_4 = []
x_5 = []
x_6 = []
x_7 = []
x_8 = []
x_9 = []
x_10 = []

## Make the strings
x0 = ""
x1 = ""
x2 = ""
x3 = ""
x4 = ""
x5 = ""
x6 = ""
x7 = ""
x8 = ""
x9 = ""
x10 = ""

## Spliting the list
x = x.split()

## The calculator - For the aspiring programers I'll explain
def calc(i, n):
    if x[i].endswith(n) == True:
        return n
    else: 
        q = x[int(i)].split(n)
        q.remove("")
        q = q[0]
        return n

## Loop once for each number
for i in range(len(x)):
    if len(x[i]) == 1:
        x_0.append(x[i])
    ## If 2 digits
    elif len(x[i]) == 2:
        ## If 0x
        if x[i].startswith("0"): 
            x_0.append(calc(i, "0"))
        ## If 1
        elif x[i].startswith("1"): 
            x_1.append(calc(i, "1"))
        ## If 2
        elif x[i].startswith("2"): 
            x_2.append(calc(i, "2"))
        ## If 3
        elif x[i].startswith("3"):
            x_3.append(calc(i, "3"))
        ## Ect
        elif x[i].startswith("4"):
            x_4.append(calc(i, "4"))

        elif x[i].startswith("5"):
            x_5.append(calc(i, "5"))

        elif x[i].startswith("6"):
            x_6.append(calc(i, "6"))

        elif x[i].startswith("7"):
            x_7.append(calc(i, "7"))

        elif x[i].startswith("8"):
            x_8.append(calc(i, "8"))

        elif x[i].startswith("9"):
            x_9.append(calc(i, "9"))

    elif len(x[i]) == 3:
        if x[i].startswith("10"):
               x_10.append(calc(i, "10"))

## Make it pretty
x0, x2, x3, x4, x5, x6, x7, x8, x9, x10 = ", ".join(x_0), ", ".join(x_1), ", ".join(x_2), ", ".join(x_3),", ".join(x_4), ", ".join(x_5), ", ".join(x_6), ", ".join(x_7), ", ".join(x_8), ", ".join(x_9)
x10 = ", ".join(x_10)

## Final print
print("0  = {0}\n1  = {1}\n2  = {2}\n3  = {3}\n4  = {4}\n5  = {5}\n6  = {6}\n7  = {7}\n8  = {8}\n9  = {9}\n10 = {10}\n".format(x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10))
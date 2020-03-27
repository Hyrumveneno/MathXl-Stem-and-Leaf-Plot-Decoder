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

## The calculator - For the aspiring programers I 'll explain
## Loop once for each number
for i in range(len(x)):
    if len(x[i]) == 1:
        x_0.append(x[i])

    elif len(x[i]) == 2:
        ## If 0x
        if x[i].startswith("0"): 
            ## If it is 0 and not 0x
            if x[i].endswith("0") == True:
                x_0.append("0")
            ## If 0x
            else: 
                ## Ok split the 0 of and delete it
                q = x[int(i)].split("2")
                ## Delete the empty string
                q.remove("")
                ## Remove the extra list it is in
                q = q[0]
                ## Add to main list
                x_0.append(q)
        ## If 1
        elif x[i].startswith("1"): 
            if x[i].endswith("1") == True:
                x_1.append("1")
            else: 
                q = x[int(i)].split("1")
                q.remove("")
                q = q[0]
                x_1.append(q)
        ## If 2
        elif x[i].startswith("2"): 
            if x[i].endswith("2") == True:
                x_2.append("2")
            else: 
                q = x[int(i)].split("2")
                q.remove("")
                q = q[0]
                x_2.append(q)
        ## If 3
        elif x[i].startswith("3"):
            if x[i].endswith("3") == True:
                x_3.append("3")
            else:
                q = x[int(i)].split("3")
                q.remove("")
                q = q[0]
                x_3.append(q)
        ## Ect
        elif x[i].startswith("4"):
            if x[i].endswith("4") == True:
                x_4.append("4")
            else:
                q = x[int(i)].split("4")
                q.remove("")
                q = q[0]
                x_4.append(q)

        elif x[i].startswith("5"):
            if x[i].endswith("5") == True:
                x_5.append("5")
            else:
                q = x[int(i)].split("5")
                q.remove("")
                q = q[0]
                x_5.append(q)

        elif x[i].startswith("6"):
            if x[i].endswith("6") == True:
                x_6.append("6")
            else:
                q = x[int(i)].split("6")
                q.remove("")
                q = q[0]
                x_6.append(q)

        elif x[i].startswith("7"):
            if x[i].endswith("7") == True:
                x_7.append("7")
            else:
                q = x[int(i)].split("7")
                q.remove("")
                q = q[0]
                x_7.append(q)

        elif x[i].startswith("8"):
            if x[i].endswith("8") == True:
                x_8.append("8")
            else:
                q = x[int(i)].split("8")
                q.remove("")
                q = q[0]
                x_8.append(q)

        elif x[i].startswith("9"):
            if x[i].endswith("9") == True:
                x_9.append("9")
            else:
                q = x[int(i)].split("9")
                q.remove("")
                q = q[0]
                x_9.append(q)

    elif len(x[i]) == 3:
        if x[i].startswith("10"):
                if x[i].endswith("10") == True:
                    x_10.append("10")
                else:
                    q = x[int(i)].split("10")
                    q.remove("")
                    q = q[0]
                    x_10.append(q)

## Make it pretty
x0 = ", ".join(x_0)
x1 = ", ".join(x_1)
x2 = ", ".join(x_2)
x3 = ", ".join(x_3)
x4 = ", ".join(x_4)
x5 = ", ".join(x_5)
x6 = ", ".join(x_6)
x7 = ", ".join(x_7)
x8 = ", ".join(x_8)
x9 = ", ".join(x_9)
x10 = ", ".join(x_10)

## Final print
print("0  = {0}\n1  = {1}\n2  = {2}\n3  = {3}\n4  = {4}\n5  = {5}\n6  = {6}\n7  = {7}\n8  = {8}\n9  = {9}\n10 = {10}\n".format(x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10))
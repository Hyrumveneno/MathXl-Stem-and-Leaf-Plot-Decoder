## The string of numbers
## Replace the numbers in there with a paste
x = """
55
66
22
44
22
34
23
"""

## Making the lists
x_2 = []
x_3 = []
x_4 = []
x_5 = []
x_6 = []

## Make the strings
x2 = ""
x3 = ""
x4 = ""
x5 = ""
x6 = ""

## Spliting the list
x = x.split()

## The calculator - For the aspiring programers I'll explain
## Loop once for each number
for i in range(len(x)):

  ## If it is 22 and not 2x 
  if x[i].startswith("2") == True and x[i].endswith("2") == True:
      x_2.append("2")
  
  ## If 2x
  if x[i].startswith("2") == True and x[i].endswith("2") == False:
    ## Ok split the 2 of and delete it
    q = x[int(i)].split("2")
    ## Delete the empty string
    q.remove("")
    ## Remove the extra list it is in
    q = q[0]
    ## Add to main list
    x_2.append(q)

  ## If it is 3
  if x[i].startswith("3") == True and x[i].endswith("3") == True:
      x_3.append("3")
  if x[i].startswith("3") == True and x[i].endswith("3") == False:
    q = x[int(i)].split("3")
    q.remove("")
    q = q[0]
    x_3.append(q)

  ## If it is 4
  if x[i].startswith("4") == True and x[i].endswith("4") == True:
      x_4.append("4")
  if x[i].startswith("4") == True and x[i].endswith("4") == False:
    q = x[int(i)].split("4")
    q.remove("")
    q = q[0]
    x_4.append(q) 
  
  ## If it is 5
  if x[i].startswith("5") == True and x[i].endswith("5") == True:
      x_5.append("5")
  if x[i].startswith("5") == True and x[i].endswith("5") == False:
    q = x[int(i)].split("5")
    q.remove("")
    q = q[0]
    x_5.append(q)

  ## If it is 6
  if x[i].startswith("6") == True and x[i].endswith("6") == True:
      x_6.append("6")
  if x[i].startswith("6") == True and x[i].endswith("6") == False:
    q = x[int(i)].split("6")
    q.remove("")
    q = q[0]
    x_6.append(q)

## Make it pretty
x2 = ", ".join(x_2)
x3 = ", ".join(x_3)
x4 = ", ".join(x_4)
x5 = ", ".join(x_5)
x6 = ", ".join(x_6)

## Final print
print("2 = {0}\n3 = {1}\n4 = {2}\n5 = {3}\n6 = {4}\n".format(x2, x3, x4, x5, x6))

#save code as forloopexample.py
print("n to the 2nd power")
for n in range(0,10):
 print (n," to the second power is "+str( n*n))
 #Notice the print in the line above is indented 1 space.

# ~ Here is a while loop example with and if statement
#save code as whileloop.py
#this code converts dec to hex and removes the 0x
d = 0
while d < 256:
 h = hex(d)
 #h = h.replace("0x","")
 print(str(d)+" = $"+h+" ",end="")
 if(d % 10 == 0):
  print()
 d = d + 1

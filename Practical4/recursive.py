#function:generate a recursive sequence
#a is 4
#repeat:
#       a=2*a+3
#       Count laps
#       How many laps completed?
#           if less than 5: keep running
#           if 5: done
a=4
print(a)
for i in range (1,5):
    a=2*a+3
    print(a)
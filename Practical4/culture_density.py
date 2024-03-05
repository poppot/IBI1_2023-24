#Function: find in how many days that cell density will go over 90%
#dansity is 5
#day is 1
#repeat:
#       density=density*2
#       day=day+1
#       check if density is bigger than 90
#       if no: keep running 
#       if yes: done
#       the number of day is how many days that cell density will go over 90 
density=5
d=1
while density<90:
    density=density*2
    d=d+1
day=str(d)
print("in the day "+day+" the cell density will go over 90%")
def s(birth):
    year=birth+18
    if 1972<year<1987:
        return'Roger Moore'
    elif 1986<year<1995:
        return'Timothy Dalton'
    elif 1994<year<2006:
        return'Pierce Brosnan'
    elif 2005<year<2022:
        return'Daniel Craig'
    else:
        return"check the year you input"
birth=int(input(":"))
a=s(birth)
print(a)    
    

x=int(input("x= "))
y=int(input("y= "))
if x>0:
    if y>0:
        q="first"
    else:
        q="fourth"       
else:
    if y>0:
        q="seccond"        
    else:
        q="third"       
print(f"Point P({x},{y}) is in the {q} quadrant of the coordinate system")
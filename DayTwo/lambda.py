#lambda
def add(x,y):
    return x+y

print(add(5,6))

#lambda
add = lambda x,y : x+y

print(add(5,6))
#lambda
add = lambda x,y : x+y if x>y else y

print(add(5,6))



#lambda+map

costs=["$12.98","$9.99","$4.75","$19.95"]

# x=list(map((lambda c:float(c.replace("$",""),costs))))
print(list(map((lambda c:float(c.replace("$",""))),costs)))
#lambda+filter

costs=[12.98,9.99,4.75,19.95]

# x=list(filter((lambda c:c>10),costs))
print(list(filter((lambda c:c>10),costs)))
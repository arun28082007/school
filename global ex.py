c= 12
def show():
    global c
    c = c + 12
    print("Inside show:", c)
show()
c= 10
print("Outside show:", c)
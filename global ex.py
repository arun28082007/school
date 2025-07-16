'''
c= 12
def show():
    global c
    c = c + 12
    print("Inside show:", c)
show()
c= 10
print("Outside show:", c)
'''

s = 3
def get():
    global s
    s = s + 10
    print("Inside get:", s)
def findarea():
    global s
    s = s * s
    print("Inside findarea:", s)
get()
findarea()
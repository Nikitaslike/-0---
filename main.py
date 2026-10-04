import turtle
turtle.speed(1)
turtle.shape('turtle')


def task1():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    
    turtle.exitonclick()

def task2():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90) 
    turtle.forward(100)
    
    turtle.done()
    
def task3():
    count = 0   
    while count < 360:
        turtle.forward(1)
        turtle.left(1)
        count += 1  
        
    turtle.done()
        
def task4():
    size = 20
    count = 0
    
    while count < 10:
        turtle.pendown()


        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90) 

        turtle.penup()

        turtle.backward(10)
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90) 
        size += 20  
        count += 1

    turtle.done()

    turtle.done() 
    
def task5():
    n = 12
    angle = 360 / n
    count = 0
    while count < n:
        turtle.right(angle)
        turtle.forward(100)
        turtle.stamp()
        turtle.backward(100)
        count += 1
        
    turtle.done() 
    
def task6():
    size = 0
    count = 0

    while count < 200:
        turtle.forward(size)
        turtle.left(8)
        size += 0.2
        count += 1

    turtle.done()  
    
def task7():
    size = 10
    count = 0
    
    while count < 30: 
        turtle.forward(size)
        turtle.left(90) 
        size += 5        
        count += 1 
        
    turtle.done() 

while True:
    
    print("Оберіть яку черепашку запустити: ")
    choose = int(input())

    try: 
        if choose == 1:
            task1()
        elif choose == 2:
            task2()
        elif choose == 3:
            task3()
        elif choose == 4:
            task4()
        elif choose == 5:
            task5()
        elif choose == 6:
            task6()
        elif choose == 7:
            task7()
        elif choose == 0:
            break
        else:
            print("Correct number or vanish!!! 𐐘 🤝ඞ")
            
    except turtle.Terminator:
        # знайшов з гпт щоб можна було запустити натсупну черепашку після закриття попередньої, бо інакше програма падає з помилкою.
        import turtle
        turtle.speed(1)
        turtle.shape('turtle')

        turtle.TurtleScreen._RUNNING = True
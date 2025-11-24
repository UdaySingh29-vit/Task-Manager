print("Welcome To Task Manahger")
l = []
d = []


def add_task():
    """Function to add the no of task user had to add in the do list"""
    print("enter no of task you need to add")
    n = int(input())
    while (n > 0):
        s = input("enter task you need to add")
        l.append(s)
        n -= 1


def done_task():
    """Function to remove task from to do list if the user had done it, 
    and add the same task to done list"""
    print("enter task you have done")
    s = input()
    for i in l:
        if s == i:
            l.remove(s)
            d.append(s)


def show():
     """ to print the list of task you will do """
    print("your to-do list:")
    for i in l:
        print("- ", i)
    if (len(d) != 0):
        print("your done task list")
        for i in d:
            print("- ", i)
    else:
        print("do some task lazy fellow")


def exits():
    """To exit from the program at any given point"""
    print("Thank you for using Task Manager")
    if len(l) != 0:
        print("just don't forget about your remaining task")
    show()
    exit()


while True:
    print("""Menu:
          1. to input a task in task manager
         2. to input task what you have done
         3.to show list of task you will do and have done
        4. to exit from the program at any given point\n""")
    c = int(input("enter ypur choice : "))
    if c == 1:
        add_task()
    elif c == 2:
        done_task()
    elif c == 3:
        show()
    elif c == 4:
        exits()
    else:
        print("invalid choice")

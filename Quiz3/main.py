import pen

def new_pen():
    return pen.Pen()




if __name__ == "__main__":
    p = new_pen()
    print(p.check_ink())
    p.write()
    p.write()
    p.write()
    print(p.check_ink())



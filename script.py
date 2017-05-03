import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    ident(tmp)
    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    
    tmp = []
    step = 0.1
    for command in commands:
        print command
        if command[0] == "push":
            print "pushing"
            tmp= stack[len(stack)-1]
            stack.append(tmp)
        elif command[0] == "pop":
            stack.pop()
        elif command[0] == "move":
            tmp= make_translate(command[1], command[2], command[3])
            matrix_mult(stack[len(stack)-1], tmp)
            stack[len(stack)-1] = tmp
        elif command[0] == "rotate":
            theta = float(command[2]) * (math.pi / 180)

            if command[1] == 'x':
                t = make_rotX(theta)
            elif command[1] == 'y':
                t = make_rotY(theta)
            else:
                t = make_rotZ(theta)
            matrix_mult(stack[len(stack)-1], t)
            stack[len(stack)-1] = t
        elif command[0] == 'scale':
            t = make_scale(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(stack[len(stack)-1], t)
            stack[len(stack)-1] = t
            

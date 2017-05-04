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
        if command[0] == "push":
            print "pushing"
            tmp= stack[len(stack)-1]
            stack.append(tmp)
            
        elif command[0] == "pop":
            print "popping"
            stack.pop()
            
        elif command[0] == "move":
            print "moving"
            tmp= make_translate(command[1], command[2], command[3])
            matrix_mult(stack[len(stack)-1], tmp)
            stack[len(stack)-1] = tmp
            
        elif command[0] == "rotate":
            print "rotating"
            theta = float(command[2]) * (math.pi / 180)

            if command[1] == 'x':
                t = make_rotX(theta)
            elif command[1] == 'y':
                t = make_rotY(theta)
            else:
                t = make_rotZ(theta)
                
            matrix_mult(stack[len(stack)-1], t)
            stack[len(stack)-1] = t
            
        elif command[0] == "scale":
            print "scaling"
            t = make_scale(float(command[1]), float(command[2]), float(command[3]))
            matrix_mult(stack[len(stack)-1], t)
            stack[len(stack)-1] = t
            
        elif command[0] == "box":
            print "box"
            tmp= []
            add_box(tmp,
                    float(command[1]), float(command[2]), float(command[3]),
                    float(command[4]), float(command[5]), float(command[6]))
            matrix_mult(stack[len(stack)-1], tmp)
            draw_polygons(tmp, screen, color)
            tmp = []
                    
        elif command[0] == "sphere":
            print "sphere"        
            tmp= []
            add_sphere(tmp,
                       float(command[1]), float(command[2]), float(command[3]),
                       float(command[4]), step)
            matrix_mult(stack[len(stack)-1], tmp)
            draw_polygons(tmp, screen, color)
            tmp = []
            
        elif command[0] == 'torus':
            print "torus"
            tmp= []
            add_torus(tmp,
                      float(command[1]), float(command[2]), float(command[3]),
                      float(command[4]), float(command[5]), step)
            matrix_mult(stack[len(stack)-1], tmp)
            draw_polygons(tmp, screen, color)
            tmp = []

        elif command[0] == "line":
            print "line"
            tmp= []
            add_edge(tmp,
                     float(command[0]), float(command[1]), float(command[2]),
                     float(command[3]), float(command[4]), float(command[5]) )
            matrix_mult(stack[len(stack)-1], tmp)
            draw_lines(tmp, screen, color)

        elif command[0] == "save":
            save_extension(screen, command[1])

        elif command[0] == "display":
            display(screen)
            

                    









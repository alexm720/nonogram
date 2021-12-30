from graphics import *

class nonogram:
    def __init__(self, width, height,width_values,height_values):
        self.width = width                  # width of the board
        self.height = height                # height of the board
        self.width_values = width_values              
        self.height_values = height_values

class vals:
    def __init__(self, row, column, nums):
        self.row = row                     # row number of matrix - will be 0 if column
        self.column = column               # column number of matrix - will be 0 if row
        self.nums = nums

def create_vals(height, width, val):
    new_vals = vals(height,width,val)
    return new_vals

def create_board(board):  
    if (board.width_values is not None and 
    board.height_values is not None):
        return board
    
    for val in range(board.width):
        new_val = create_vals(None,val,[])
        board.width_values.append(new_val)
        del(new_val)
    for height_vals in range(board.height):
        new_val = create_vals(height_vals,None,[])
        board.height_values.append(new_val)
        del(new_val)
    return board


def calculate_lines(res_height, res_width, board_height, board_width,
                    offset_width,offset_height):
    lst_width = []
    lst_height = []
    add_width = (res_width - 2 * offset_width)/board_width
    add_height = (res_height - 2 *offset_height ) /board_height
    sum_height = offset_height
    sum_width = offset_width
    for i in range(board_width-1):
        sum_width += add_width
        lst_width.append(sum_width)
    for x in range(board_height-1):
        sum_height += add_height
        lst_height.append(sum_height)

    return lst_width, lst_height

def calculate_offset(res_height, res_width):
    offset_width = .8 * res_width
    offset_height = .8 * res_height
    return offset_width,offset_height

def call_graphics(board_obj,width = 500, height = 500, color = "light blue"):
    window = GraphWin("graphics window",width,height)
    window.setBackground(color)
    offset_width,offset_height = calculate_offset(height, width)
    board = Rectangle(Point(offset_width,offset_height),Point(width - offset_width,height - offset_height))
    x,y = calculate_lines(height, width, board_obj.height, board_obj.width,offset_width,offset_height)
    print(x,y)
    board.draw(window)
    for i in y:
        aLine = Line(Point(offset_width,i),Point(width - offset_width,i))
        aLine.draw(window)  
    for i in x:
        bLine = Line(Point(i,offset_height),Point(i,height - offset_height))
        bLine.draw(window)        
    window.getMouse()
    window.close()



def main(): 
    width_vals = [create_vals(0,1,1),create_vals(0,2,3),create_vals(0,3,3),create_vals(0,4,2)]
    height_vals = [create_vals(1,0,1),create_vals(2,0,3),create_vals(3,0, 2),create_vals(4,0,3)]
    new_board = create_board(nonogram(5,6, width_vals,height_vals))
    call_graphics(new_board,500,500)



if __name__ == "__main__":
    main()
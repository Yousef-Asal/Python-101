

def rect(height, width, round_fact):
    """
    This function computes the circumference and area of a rectangle
    Inputs:
        height
        width
        round factor
    Outputs:
        Circumference 
        Area
    """
    circumference = round(2 * (height+width), round_fact)
    area = round(height * width, round_fact)

    return circumference, area

def is_square(height, width):
    """
    This function checks if the given values are for a square
    Inputs:
        height
        width
    Outputs:
        Circumference 
        Area
    """
    c,a = rect(height,width,2)

    if height == width:
        print('This is a Square')    
    else:
        print('This is a Rectangle')

    return c, a
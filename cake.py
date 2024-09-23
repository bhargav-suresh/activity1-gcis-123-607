
def rectangle(x,y,color,turta):
    """
    This function draw a rectangle with a filled in color and the parameters used and
    x which is the length, y which is the height, color which specifies the color, and 
    turta which is considered the drawing tool
    x:int
    y:int
    color:str
    rectangle(x,y,color,turta)
    """
    
    turta.begin_fill()
    turta.fillcolor(color)
    turta.fd(x)
    turta.right(90)
    turta.fd(y)
    turta.right(90)
    turta.fd(x)
    turta.right(90)
    turta.fd(y)
    turta.end_fill()


def table(x_table,y_table,color_table,turta,x_legs,y_legs,color_legs):
    """
    This function draws the table and the legs which takes in the length and height and
    color of the table in addition to the length and height of the table legs with also the 
    drawing tool (turta)
    x_table:int
    y_table:int
    color_table:str
    x_legs:int
    y_legs:int
    color_legs:str
    table(x_table,y_table,color_table,turta,x_legs,y_legs,color_legs)
    """
    
    turta.up()
    turta.goto(-x_table/2,0)
    turta.down()
    rectangle(x_table,y_table,color_table,turta)
    turta.right(180)
    leg(x_legs,y_legs,color_legs,turta)
    turta.fd(40)
    turta.right(90)
    leg(x_legs,y_legs,color_legs,turta)
    turta.fd(220)
    turta.right(90)
    leg(x_legs,y_legs,color_legs,turta)
    turta.fd(40)
    turta.right(90)
    leg(x_legs,y_legs,color_legs,turta)



def leg(x_legs,y_legs,color_legs,turta):
    """
    This function draws the legs considering the height, 
    length, and color
    x_legs:int
    y_legs:int
    color_legs:str
    leg(x_legs,y_legs,color_legs,turta)
    """
    rectangle(x_legs,y_legs,color_legs,turta)


def tray(x_tray,y_tray,color_tray,turta):
    """
    This function draws the tray using turta considering the height,
    width and color of the tray
    x_tray:int
    y_tray:int
    color_tray:str
    tray(x_tray,y_tray,color_tray,turta)
    """
    turta.up()
    turta.goto(0,0)
    turta.goto(-x_tray/2,4)
    turta.down()
    rectangle(x_tray,y_tray,color_tray,turta)
    turta.up()
    turta.goto(0,0)
    turta.down()


def layer(x_layer,y_layer,layer_color,turta):
    """
    This function considers the length and width of the layers
    including the color to be drawn and filled in by turta
    x_layer:int
    y_layer:int
    layer_color:str
    layer(x_layer,y_layer,layer_color,turta)
    """
    rectangle(x_layer,y_layer,layer_color,turta)


def cake(x,y_layer_1,layer_color_1,y_layer_2,layer_color_2,y_layer_3,layer_color_3,y_layer_4,layer_color_4,turta):
    """
    This function includes everything in the cake starting with the length, 
    width, and color of each layer decorations drawn by turta
    x:int
    y_layer_1:int
    layer_color_1:str
    y_layer_2:int
    layer_color_2:str
    y_layer_3:int
    layer_color_3:str
    y_layer_4:int
    layer_color_4:str
    """
    turta.up()
    turta.goto(-y_layer_1/2, 4)
    turta.down()
    
    layer(x, y_layer_1, layer_color_1, turta)
    turta.up()
    turta.goto(-y_layer_2/2, x + 4)
    turta.down()
    turta.right(90)

    layer(x, y_layer_2, layer_color_2, turta)
    turta.up()
    turta.goto(-y_layer_3/2 ,x + x + 4)
    turta.down()
    turta.right(90)

    layer(x, y_layer_3, layer_color_3, turta)
    turta.up()
    turta.goto(-y_layer_4/2, x + x + x + 4)
    turta.down()
    turta.right(90)

    layer(x, y_layer_4, layer_color_4, turta)
    turta.down()

    cherry(0, x + x + x + x + 4, 4, "red", turta)
    candle(y_layer_4/4, x + x + x + x + 4, 5, 15, "white", turta)
    turta.right(90)
    candle(-y_layer_4/4, x + x + x + x + 4, 5, 15, "white", turta)
    turta.up()
    turta.goto(-50,80)
    turta.down()
    frosting(turta,180,10,"white")
    turta.right(180)
    frosting(turta,180,10,"white")
    turta.right(180)
    frosting(turta,180,10,"white")
    turta.right(180)
    frosting(turta,180,10,"white")
    turta.right(180)
    frosting(turta,180,10,"white")
    turta.begin_fill()
    turta.fillcolor("white")
    turta.fd(4)
    turta.left(90)
    turta.fd(100)
    turta.left(90)
    turta.fd(4)
    turta.end_fill()



    

def frosting(turta, frosting_extent, frosting_radius, frosting_color):
    """
    This function takes in the parameters to take the arc length, the radius of 
    the frosting, the color and turta for the design to be drawn.
    frosting_extent:int (degree)
    frosting_radius:int
    frosting_color:str
    frosting(turta, frosting_extent, frosting_radius, frosting_color)
    """
    turta.up()
    turta.down()
    turta.fillcolor(frosting_color)
    turta.begin_fill()
    turta.circle(frosting_radius, frosting_extent)
    turta.end_fill()

 


def cherry(x, y, radius, circle_color, turta):
    """
    This function takes both (x,y) coordinates, the radius, and the
    color of the cherry for it to be aligned on the top center of the 
    cake and use turta to draw it
    x:int
    y:int
    radius:int
    circle_color:str
    cherry(x, y, radius, circle_color, turta)
    """
    turta.up()
    turta.goto(x, y + radius * 2)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(circle_color)
    turta.circle(radius)
    turta.end_fill()



def candle(x, y, x_candle, y_candle, candle_color, turta):
    """
    This function takes the parameters: (x,y) coordinates, the height, the
    width, color and turta to draw the candle on top of the cake.
    x:int
    y:int
    x_candle:int
    y_candle:int
    candle_color:str
    candle(x, y, x_candle, y_candle, candle_color, turta)
    """
    turta.up()
    turta.goto(x, y)
    turta.down()
    turta.begin_fill()
    turta.fillcolor(candle_color)
    rectangle(x_candle, y_candle, candle_color, turta)
    turta.end_fill()


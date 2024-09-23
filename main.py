import turtle
from cake import table,tray,cake


def main():
    """
    This function is responsible for the code since all the parameters play an important factor when making the 
    code since it makes the table, tray, cake, and takes in all the measurementsand desired colors and also is resonsible for the
    design which includes the candle, cherry and frosting.
    
    x:int
    x_(objectname): int
    y:int 
    y_(objectname):int
    color_(objectname):str
    layer_color_(layernumber):str
    x_layer_(layernumber):int
    y_layer_(layernumber):int
    
    """
    
    x=20
    x_table=300
    y_table=7
    color_table="black"
    x_legs=100
    y_legs=5
    color_legs="black"
    x_tray=120
    y_tray=6
    color_tray="white"
    
   
    layer_color_1=input("Enter the color of layer 1: ")
    y_layer_1=100

   
    layer_color_2=input("Enter the color of layer 2: ")
    y_layer_2=100

    
    layer_color_3=input("Enter the color of layer 3: ")
    y_layer_3=100

   
    layer_color_4=input("Enter the color of layer 4: ")
    y_layer_4=100
    
    print("your cake is loading...")

    sc=turtle.Screen()                #turtle code
    turta=turtle.Turtle()
    turta.hideturtle()
    
    turta.speed(0)
    

    table(x_table,y_table,color_table,turta,x_legs,y_legs,color_legs)
    tray(x_tray,y_tray,color_tray,turta)
    cake(x,y_layer_1,layer_color_1,y_layer_2,layer_color_2,y_layer_3,layer_color_3,y_layer_4,layer_color_4,turta)
    
    sc.exitonclick()

if __name__=="__main__":
    main()
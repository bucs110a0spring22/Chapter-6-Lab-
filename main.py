import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count=0
    while(n != 1):
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
        count += 1   
    return count


def graph(var):
  writer= turtle.Turtle()
  grapher=turtle.Turtle()
  wn=turtle.Screen()
  wn.bgcolor("light blue") #I gave it a cool color
  wn.setworldcoordinates(0,0,10,10)
  grapher.speed(0)
  grapher.goto(0,0)
  grapher.goto(var+1,0)
  grapher.goto(0,0)
  
  max_so_far = 0

  for start in range(1,var+1):
    result = seq3np1(start)
    grapher.goto(start,result)
    
    result > max_so_far
    max_so_far = result
  
    wn.setworldcoordinates(0,0,start+10,max_so_far+10)
  
    writer.clear()
    writer.goto(0,max_so_far) 
    text = "Maximum so far: " + str(start) + ", " + str(result)
    writer.write(text)
    
    grapher.up()
    grapher.goto(0,0)
    grapher.down()
    grapher.goto(0,max_so_far)
    grapher.up()
    grapher.goto(start,result)
    grapher.down()
      
  '''
  description: makes the graphs, makes the turtles and sets the default world coordinates, makes axis, makes bigger graph everytime max 
  arg: var
  returns: none
  
  '''      

def main():
  var= int(input("Please input a positive value "))
  if (var) <= 0:
      exit("Invalid value")
  else:
      for start in range(1,var+1):
        result = seq3np1(start)
        print("Start is " + str(start) + " and result is " + str(result))
  graph(var)
       
main()

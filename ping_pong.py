
# An initial try for a Ping Pong Game

class PongAI:
    def __init__(self, table_size):
        """
        table_size --   A tuple representing the dimensions of the table.
                        The x and y dimensions of the table are represented by
                                    table_size[0], table_size[1]
                        respectively.
        """
        self.table_size = table_size
        self.ball_loc = []
        
        # add code here if you like
        # (to store data between calls to the method)

    def pong_ai(self, paddle_rect, other_paddle_rect, ball_rect):
        """Return "up" or "down", depending on which way the paddle should go to
        align its centre with the centre of the ball
   
        Keyword arguments:
        paddle_rect -- A rectangle object representing the coordinates of your paddle.
                       The top-left corner of the rectangle is represented by the tuple
                                    paddle_rect.pos[0], paddle_rect.pos[1]
                       The dimensions (width, height) of the paddle are represented by
                                    paddle_rect.size[0], paddle_rect.size[1]
    
        other_paddle_rect -- A rectangle representing the opponent's paddle.
                        It is the same kind of object as above and its attributes
                        can be accessed in the same manner described above.
   
        ball_rect --    A rectangle representing the ball. It is the same kind of object
                        as the two above.
   
        Coordinates start at (0, 0) in the top-left corner.
        They look as follows:
   
   
                0             x
                |------------->
                |
                |             
                |
            y   v
        """          
        
        
            
        self.ball_loc.append(ball_rect)
        pre_x = 0
        #get the x and y coordinates for the last two positions
        if len(self.ball_loc)>1:
            x1 = self.ball_loc[-2].pos[0]+self.ball_loc[-2].size[0]/2
            x2 = self.ball_loc[-1].pos[0]+self.ball_loc[-1].size[0]/2
            y1 = self.ball_loc[-2].pos[1]+self.ball_loc[-2].size[1]/2
            y2 = self.ball_loc[-1].pos[1]+self.ball_loc[-1].size[1]/2
            paddle_y = paddle_rect.pos[1]+paddle_rect.size[1]/2#set the postion of the paddle in the y direciton
            #when the ball is moving horizontally, if the paddle is lower than the ball then make the paddle moving upwards, vice versa            
            if y2 == y1:
                if y2>paddle_y:
                    return "down"
                if y2<paddle_y:
                    return "up"
  
            #calculate the angle of bounce              
            
            if paddle_rect.pos[0] > self.table_size[0]/2: #when the student ai paddle is on the right hand side
                tan_theta = abs((x2-x1)/(y2-y1))
                paddle_x = paddle_rect.pos[0]
                if y2 < y1: #when the ball is moving upwards
                    ball_x=y2*tan_theta + x2 #the x-coordinate of the ball when it touches the bound
                    ball_y=y2-(paddle_x-x2)/(tan_theta) #the y-coordinate predicted of the ball when it is going to hit the paddle
#if the ball re-bounces when it first tounches the bound, count the times of rebounce                    
                    if ball_x< paddle_x:
                        count=0
                        while ball_x < paddle_x: #loop until the ball does not rebound anymore                        
                            pre_x = ball_x
                            ball_x=tan_theta*self.table_size[1]+ball_x #the next x-coordinate of the ball when it doing the next bounce
                            count+=1
#calculate the predicted y-coordinate depending on whether the times of rebounce is odd or even
                        if count%2==1:
                            ball_y=(paddle_x-pre_x)/(tan_theta)       
                        else:
                            ball_y=self.table_size[1]-(paddle_x-pre_x)/(tan_theta) #the y-coordinate of the ball when it is going to hit the paddle
                                       
                elif y2 > y1: #when the ball is moving downwards
                    ball_x=(self.table_size[1]-y2)*tan_theta + x2
                    ball_y=y2+(paddle_x-x2)/(tan_theta) #the y-coordinate of the ball when it is going to hit the paddle
                    if ball_x < paddle_x:
                        count=0
                        while ball_x<paddle_x:                       
                            pre_x = ball_x
                            ball_x=tan_theta*self.table_size[1]+ball_x
                            count+=1
                        if count%2==1:
                            ball_y=self.table_size[1]-(paddle_x-pre_x)/(tan_theta)
                        else:
                            ball_y=(paddle_x-pre_x)/(tan_theta) 
                                    
                                    
            else: #when the student ai paddle is on the left hand side
                tan_theta = abs((x2-x1)/(y2-y1))
                paddle_x = paddle_rect.pos[0] + paddle_rect.size[0]
                if y2 < y1: #when the ball is moving upwards
                    ball_x=x2-(y2*tan_theta)
                    ball_y=y2 - x2/tan_theta #the y-coordinate predicted of the ball when it is going to hit the paddle               
                    if ball_x > 0:
                        count = 0
                        while ball_x > 0:
                            pre_x = ball_x
                            count+=1
                            ball_x=ball_x-(tan_theta*self.table_size[1])
                        if ball_x <=0:
                            if count%2 == 0:
                                ball_y = self.table_size[1] - (ball_x-paddle_x) / tan_theta
                            if count%2 != 0:
                                ball_y = (ball_x-paddle_x)/(tan_theta)

                elif y2 > y1: #when the ball is moving upwards
                    ball_x=x2-((self.table_size[1]-y2)*tan_theta)
                    ball_y=y2 + x2/tan_theta
#if the ball re-bounces when it first tounches the bound, count the times of rebounce                    
                    if ball_x>0:
                        count=0
                        while ball_x>0:
                            pre_x = ball_x
                            count+=1
                            ball_x=ball_x-(tan_theta*self.table_size[1])
#calculate the predicted y-coordinate depending on whether the times of rebounce is odd or even
                        if ball_x <= 0:
                            if count%2 == 0:
                                ball_y = (ball_x-paddle_x)/(tan_theta)
                            if count%2 != 0:
                                ball_y= self.table_size[1] - (ball_x-paddle_x) / tan_theta
                                       
 #if the paddle is lower than the ball then make the paddle moving upwards, vice versa           
            if paddle_y > ball_y:
                return "up"
           
            if paddle_y < ball_y:
                return "down"
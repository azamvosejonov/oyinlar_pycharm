# from turtle import Turtle
#
# START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
# UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0
# DISTANCE = 20
# class Snake:
#     def __init__(self):
#         self.segments = []
#         self.create_snake()
#         self.head = 0
#
#     def create_snake(self):
#             for position in START_POSITION:
#                 new_segment = Turtle('square')
#                 new_segment.color('white')
#                 new_segment.penup()
#                 new_segment.goto(position)
#                 self.segments.append(new_segment)
#
#
#     def move(self):
#         for seg_num in range(len(self.segments)-1,0,-1):
#             new_x = self.segments[seg_num-1].xcor()
#             new_y = self.segments[seg_num-1].ycor()
#             self.segments[seg_num].goto(new_x, new_y)
#         self.segments[self.head].forward(DISTANCE)
#
#     def extend(self):
#         new_segment=Turtle('square')
#         new_segment.color('white')
#         new_segment.penup()
#         new_segment.goto(self.segments[-1].position())
#         self.segments.append(new_segment)
#
#     def up(self):
#         if self.segments[self.head].heading()!=DOWN:
#             self.segments[self.head].setheading(UP)
#     def down(self):
#         if self.segments[self.head].heading()!=UP:
#             self.segments[self.head].setheading(DOWN)
#     def left(self):
#         if self.segments[self.head].heading()!=RIGHT:
#           self.segments[self.head].setheading(LEFT)
#     def right(self):
#         if self.segments[self.head].heading()!=LEFT:
#            self.segments[self.head].setheading(RIGHT)
#

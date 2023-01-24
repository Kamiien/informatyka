BJS	    = main.o
SOURCE	= main.cpp
HEADER	= 
OUT	    = opengl.exe
CC	    = g++
FLAGS	  = -g -c -Walli
LFLAGS  = -I./include -L./lib -lglfw3 -lopengl32 -lgdi32

all: $(OBJS)
		$(CC) -g $(OBJS) -o $(OUT) $(LFLAGS)

main.o: main.cpp
		$(CC) $(FLAGS) main.cpp 


clean:
		rm -f $(OBJS) $(OUT)


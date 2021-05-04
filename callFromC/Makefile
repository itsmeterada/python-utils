PROGS	= callFromC
ALL:	$(PROGS)

CC = gcc
CXX = g++

ifeq ($(shell uname),Darwin)
else
endif
CXXFLAGS += -D_THREAD_SAFE
CXXFLAGS += -O0 -g
#CFLAGS += -std=c++11
#$(eval PYTHONINC := $(shell which python | sed -e 's/python/include/'))
#CXXFLAGS += -I$(PYTHONINC)
$(eval PYTHONINC := $(shell python3-config --embed --cflags))
CXXFLAGS += $(PYTHONINC)

ifeq ($(shell uname),Darwin)
LIBS =
#LIBS += -framework GLUT -framework OpenGL -framework Cocoa
#LIBS += -L/opt/X11/lib
else
LIBS = 
endif
LDFLAGS = $(LIBS)
#$(eval PYTHONLIB := $(shell which python | sed -e 's/python/libs/'))
#LDFLAGS += -L$(PYTHONLIB) -lpython3
$(eval PYTHONLIB := $(shell python3-config --embed --ldflags))
LDFLAGS += $(PYTHONLIB)

.cpp.o:
	rm -f $*.o
	$(CXX) -c $(CXXFLAGS) $*.cpp

#$(PROGS): $(OBJS)
#	rm -f $@
#	$(CXX) -o $@ $(OBJS) $(LDFLAGS)

callFromC: callFromC.o
	rm -f $@
	$(CXX) -o $@ $@.o $(LDFLAGS)

clean:
	rm -f $(PROGS) *.o core

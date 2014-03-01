DEPS = $(OBJS:.o=.d)
CC = gcc
CFLAGS = -I../../include -g3 -Wall -fpic -std=gnu99 -MMD -MP -DDEBUG -O3 
BIN = locks
LDLIBS = -lm -lrt -pthread  -D_POSIX_C_SOURCE=200112L -D_GNU_SOURCE

##### Objects

OBJS = 

all: $(BIN)

$(BIN): $(OBJS)
	$(CC) $(LDFLAGS) $(OBJS)  $(LDLIBS) -o ../$(BIN)

%.d: %.c

check-syntax:
	$(CC) -o nul -S ${CHK_SOURCES}

clean:
	rm -f $(OBJS) $(BIN) *.d
	rm ../$(BIN)
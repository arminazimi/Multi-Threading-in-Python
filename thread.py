from time import sleep , perf_counter
from threading import Thread

# without treading  ==> 4s
start = perf_counter()
def C(x):
    print(f'start {x} ....')
    sleep(2)
    print(f'end {x} ....')
C('1')
C('2')
end = perf_counter()
print( end - start )

# with tread   ==> 2s
start = perf_counter()
def A(x):
    print(f'start {x} ....')
    sleep(2)
    print(f'end {x} ....')
t1 = Thread(target=A, args=(1,))
t2 = Thread(target=A, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()

end = perf_counter()
print( end - start )


# with using a class  ==> 2s
start = perf_counter()

def B(x, delay):
    print(f'start {x} ....')
    sleep(delay)
    print(f'end {x} ....')

class ShowThread(Thread):
    def __init__(self, x , delay):
        super().__init__()
        self.x = x
        self.delay = delay

    def run(self):
        B(self.x, self.delay)

t3 = ShowThread('1',2)
t4 = ShowThread('2',2)

t3.start()
t4.start()

t3.join()
t4.join()

end = perf_counter()
print( end - start )


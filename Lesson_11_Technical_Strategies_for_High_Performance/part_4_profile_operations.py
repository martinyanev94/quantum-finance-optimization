import cProfile

def main_operations():
    for _ in range(10000):
        print("Some operation happening...")

cProfile.run('main_operations()')


class Random:
    '''Iterator for random sequence'''
    def __init__(self, iter):
        self.iter = iter
        self.enumirate_list = list(range(len(iter)))
    
    def __iter__(self):
        return self
    
    def __next__(self):
        import random
        if len(self.enumirate_list) == 0:
            raise StopIteration
            return
        choice = random.choice(self.enumirate_list)
        self.enumirate_list.remove(choice)
        return self.iter[choice]


if __name__ == '__main__':
    for i in Random('anaconda'):
        print(i, end='')

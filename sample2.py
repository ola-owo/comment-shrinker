#!/usr/bin/env python3
import random
# Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur,
# adipisci velit

class FakeClass(object):
    '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut magna
tincidunt, pharetra sem adipiscing, volutpat lectus. Donec ut metus blandit,
pharetra est vel, scelerisque nisl. Suspendisse condimentum dui quis varius
congue. '''
    def __init__(self, attr):
        """Aenean auctor leo ut lacus tristique viverra.    Cras et lectus ac
nibh imperdiet sollicitudin nec vitae tellus."""
        self.attr = attr
def fakeFunc(a, b=3, c=True):
    """Aenean eget augue eget ante malesuada feugiat.""" #this line shouldn't be split
    if a:
        pass
    else:
        c = b**2 + c
def fake2():
    '''Aenean tincidunt dictum faucibus. Morbi nisl diam, tempus in orci id,
semper lobortis odio. Duis laoreet, turpis vitae euismod accumsan, metus sem
dictum nibh, vitae posuere mi purus sed lorem. Duis sed est vel turpis mollis
fermentum id eu ligula.'''
    fakeFunc(random.randint(0,1))

for i in range(10):
    print('Nope!')


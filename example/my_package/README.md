# My Package

This is a simple python package.

## Installation

Clone this repo and install by running:

```commandline
$ pip install -e example/my_package
```

## Testing

Run the following script directly in the terminal:

```commandline
$ python -c """
import time
from my_package.utils import is_prime

start = time.time()
iters = 250001
for i in range(2, iters):
    is_prime(i)

print(f'{iters} iterations took: {round(time.time() - start, 4)} seconds.')
"""
```
* Expected output: it might take about a minute to run all the iterations.

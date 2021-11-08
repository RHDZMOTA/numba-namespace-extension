# My Package (Compiled)

This python package uses the `my_package` namespace and
adds a `compiled` module composed by the "compiled" version of the
functions registered in the `registry.json` file.

During the installation process, the `registry.json` functions 
will be compiled using [Numba AOT](https://numba.pydata.org/numba-doc/latest/reference/aot-compilation.html). 
This results in about a 10X performance improvement.

Consider that the modules used on the `registry.json` file should be available
at the installation runtime. For this example, this means having the `my_package` previously
installed (i.e., `pip install -e example/my_package`).

By using the same namespace in both the original python package and the compiled version, we ensure
that we can import the `compiled` submodule using the same access pattern. Once both packages are installed,
imports should look as following:

Import original function (only requires `my_package`)
```python
from my_pacakge.utils import is_prime
```

Import compiled function (only requires `my_package_compiled`)
```python
from my_package.compiled.utils import is_prime
```

Import both functions (requires `my_package` and `my_package_compiled`)
```python
from my_package.utils import is_prime as is_prime_original
from my_package.compiled.utils import is_prime as is_prime_compiled
```


## Installation

Clone this repo and install by running:

```commandline
$ pip install -e example/my_package_compiled
```

## Testing

Run the following script directly in the terminal:

```commandline
$ python -c """
import time
from my_package.compiled.utils import is_prime

start = time.time()
iters = 250001
for i in range(2, iters):
    is_prime(i)

print(f'{iters} iterations took: {round(time.time() - start, 4)} seconds.')
"""
```
* Expected output: about 10 seconds to run all the iterations.

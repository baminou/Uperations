[![Build Status](https://travis-ci.org/baminou/Uperations.svg?branch=master)](https://travis-ci.org/baminou/Uperations)

## Uperations

This Python framework helps you create command line tools with re-usable and sharable commands.
View the official documentation at [https://www.uperations.com](https://www.uperations.com).

[A base library](https://github.com/baminou/Uperations-base) is already registered in this project to help you get started fast.

The main components to know are Libraries, Operations and Commands.

* Operations: An action that has to be executed.
* Library: A group of operations
* A command to execute in the terminal to run the Operation

## Installation
This project uses python3 and was built using python 3.7.0
```bash
git clone https://github.com/baminou/Uperations.git
pip install -r requirements.txt
```

## Create a library
The first thing to do is to create a library to contain your operations.
```bash
./main.py base make:library {LIBRARY_NAME}
```

## Register your library to the project

### boot.py
The boot() function in the file boot.py is the first function that is called once the
program starts. In this function, the Kernel of the program is initialized. The kernel contains
the libraries that you need in your project mapped to console command entry point. You can
add as many libraries as you need in the Kernel.
```python

from uperations.kernel import Kernel
from uperation_base import Base
from libraries.{YOUR_LIBRARY} import {YOUR_LIBRARY_CLASS}

def boot():
    Kernel.get_instance().set_libraries({
        Base.name(): Base(),
        {YOUR_LIBRARY_CLASS}: {YOUR_LIBRARY_CLASS}()
    })
```

### Kernel
The Kernel is the a singleton that can be accessible in any operations and
and that is shared in the entire project. 
```python
from uperations.kernel import Kernel

...
kernel = Kernel.get_instance()
...
```
The Kernel contains the libraries registered in the project
```python
...
kernel.get_libraries()
...
```

### Create an operation
Once you have a library, you can start adding operations.
```bash
./main.py base make:operation {LIBRARY_NAME} {OPERATION_NAME}
```

### Add your operation to the library for access in command line
1. Open ./libraries/{LIBRARY_NAME}/{LIBRARY_NAME}/\__init__.py
2. Import your operation class at the top of the file.
```python
from .{operation_package} import {OperationClass}
```
3. Add to the dict operations
```python
@staticmethod
    def operations():
        return {
            ...,
            {command}:{OperationClass}
        }

```

### List all available operations
```bash
./main.py base list:operations
```

### Retrieve information about a library
```bash
./main.py base {LIBRARY_NAME} -h
```

### Retrieve information about an operation
```bash
./main.py base {LIBRARY_NAME} {OPERATION_NAME} -h
```
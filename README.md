# Magic Squares Generator
This repository contains a Python code to generate magic squares.

## What is a Magic Square?
A magic square is a square grid of numbers in which the sums of the numbers in each row, each column, and both main diagonals are the same.

## Usage
To use the code you can either run *magicSquare.py* and enter number n(in order to get magic square of size nxn) or you can import function **make_magic_square(n)** which will return you magic square as matrix
```python
make_magic_square(3) # [[8, 1, 6]
                     #  [3, 5, 7]
                     #  [4, 9, 2]]
make_magic_square(4) # [[16, 2,  3,  13]
                     #  [5,  11, 10, 8]
                     #  [9,  7,  6,  12]
                     #  [4,  14, 15, 1]]
```


## Unittests
This branch also has built-in tests that you can run with command
```bash
python3 -m unittest magicSquare.py
```

## History of changes
003b3a2 (unittests) : Added efficiency test

d006d5d (unittests) : Added unittest for magicSquare

942883d (main) : completed program
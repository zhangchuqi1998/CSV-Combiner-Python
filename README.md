# CSV-Combiner

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)



## Instruction

### Combiner

Before running the combiner make sure python and pandas library is installed
to install pandas on windows run ```py      -m pip install pandas```, on macOS run ```sudo pip install pandas```

To run the combiner, in the terminal inside the csv-combiner folder type
```sh
py .\csvCombiner.py .\fixtures\accessories.csv .\fixtures\clothing.csv combined.csv
```
after ```py .\csvCombiner.py``` put any source file, followed by a single output file each divided by a single space.

### Unit test

Before running the unit test make sure unittest and pyexcel is installed

Run the unit test, in the terminal type
```
py .\csvCombiner-test.py
```


## License

MIT

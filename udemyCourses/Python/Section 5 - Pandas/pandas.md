# Pandas

Python version of Excel

- Pandas is an open source library built on top of NumPy.
- It allows for fast analysis and data cleaning and preparation.
- It excels in performance and productivity.
- It also has built-in visualization features.
- It can work with data from a wide variety of sources.
- its also called python's excel

## Installation

```
conda install pandas
pip install pandas
```

### Series

The first main data type we will learn about for pandas is the Series data type. Let's import Pandas and explore the Series object.

A Series is very similar to a NumPy array (in fact it is built on top of the NumPy array object). What differentiates the NumPy array from a Series, is that a Series can have axis labels, meaning it can be indexed by a label, instead of just a number location. It also doesn't need to hold numeric data, it can hold any arbitrary Python Object.

Checkout the Series section from the jupyter note book specified in the virtualEnvironment in Section 2

### Data Frames

DataFrames are the workhorse of pandas and are directly inspired by the R programming language. We can think of a DataFrame as a bunch of Series objects put together to share the same index. Think of it more like a table.

Checkout the Series section from the jupyter note book specified in the virtualEnvironment in Section 2

### Data Input and Output

Below are the list of data sources for python that are widely used.

- CSV
- Excel
- HTML
- SQL

#### Packages needed

sqlalchemy
lxml
html5lib
beautifulsoup4


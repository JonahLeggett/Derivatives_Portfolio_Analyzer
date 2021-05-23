# Derivatives_Portfolio_Analyzer
This financial application is built to solve the problem of a small individual investor who focuses their portfolio on derivatives trading, who can't easily parse and analyzie their options trading strategies within their portfolios. This application and analysis is meant to provide an easier way for our investor to analyze their portfolio, with a focus on comparing different options strategies employed over time. It is built to automate the data exploration process for the end-user, but allowing them to import a csv file of raw data from their trading platform, and load it into a CLI application that automatically recognizes and sorts the data into the different strategies used by the investor. The investor can then query the tool to analyze any stock ticker or strategy they used, to visualize the successes and failures of their trades. This also provides a metrics dashboard that originates in a Jupiter notebook, but is deployed as a web link through the Voila tool. This allows the investor to easily deploy and visualize the analysis of their portfolio as a whole. 

---

## Technologies

This project leverages python 3.7 with the following packages:


* [pandas1.2.4](https://pandas.pydata.org) - Open source data analysis and manipulation tool, built on top of the Python programming language.

* [hvplot.pandas](https://hvplot.holoviz.org/user_guide/Pandas_API.html) - A high-level plotting API for the PyData ecosystem built on HoloViews.

* [numpy](https://numpy.org) -T he fundamental package for scientific computing with Python.

* [sqlalchemy](https://www.sqlalchemy.org) - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

* [os] - This module provides a portable way of using operating system dependent functionality.

* [dotenv] - Dotenv is a zero-dependency module that loads environment variables from a .env file into process.env. 

* [pathlib](https://pypi.org/project/pathlib/) - For constructing new paths from names of files and from other paths, checking for various properties of paths, and creating files and folders at specific paths.

* [requests](https://pypi.org/project/requests/) - The requests library is the de facto standard for making HTTP requests in Python.

* [alpace_trade_api](https://alpaca.markets) - Free stock trading API for making algorithmic trading.

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

---

## Installation Guide

Before running the application first install the following dependencies.

```python
pip install jupyterlab
-AND-
pip install voila

```

---

## Usage

To use the Derivatives Portfolio Analyzer simply clone the repository and run the **derivatives_portfolio_analyzer.ipynb** with:

```python
jupyter lab
```
-OR-

run the following code in your terminal:
```python
voila derivatives_portfolio_analyzer.ipynb
``` 

To use the San Derivatives Portfolio Analysis Application simply clone the repository and run the following code in your terminal:

```python
app.py
```

Then, follow the prompts from the CLI. You will need to enter the relative path of your CSV file from your trading platform, then follow prompts to analyzee your options trades!

## CLI Import Steps and Images


---

## Contributors

Brought to you by Jonah A. Leggett, Samuel Yang, and Brett Hudson. You can reach us at: 

jonah.leggett@gmail.com
samueljinyang@gmail.com
bhudzen@gmail.com 

You can add us at LinkedIn: 
(https://www.linkedin.com/in/jonah-l-29278a8a/)


---

## License

mit

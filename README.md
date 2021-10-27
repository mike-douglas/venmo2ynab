# venmo2ynab

This is a command-line tool for converting exported [Venmo](https://venmo.com) CSV statement files to a compatible format for importing into [YNAB](https://youneedabudget.com).

The tool accepts an arbitrary number of CSV files that you can export from the [Venmo web interface](https://venmo.com/account/statement) and generates a single CSV that YNAB accepts. It exports the transactions in the "Option 2" format (combining both outflow and inflow transactions into one field) found in the [YNAB Formatting a CSV File](https://docs.youneedabudget.com/article/921-formatting-csv-file) document.

## Usage

1. Log into Venmo, and go to [your statements](https://venmo.com/account/statement).
2. Download some CSVs of statements.
3. [Install venmo2ynab](#installation).
4. Run `venmo2ynab STATEMENT_FILE_HERE transactions-4-ynab.csv` to convert your statements to a YNAB compatible format.
5. Go to the Venmo account you set up in [YNAB](https://youneedabudget.com) and click the "Import" button. Upload the `transactions-4-ynab.csv` file with all of your transactions.

## Installation

This script uses [python3](https://python.org). Its only dependency is [Click](https://click.palletsprojects.com/en/8.0.x/), a tool for making command-line scripts easy.

Installing is a snap. Clone this repo and run:

```python
pip3 install .
```

## License

See [LICENSE.md](LICENSE.md).

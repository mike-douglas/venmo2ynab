import csv
import sys

from datetime import datetime

def read_transactions(input_file):
    with open(input_file) as csvin:
        in_reader = csv.reader(csvin, delimiter=',', quotechar='"')
        next(in_reader)
        next(in_reader)
        headers = next(in_reader)
        next(in_reader)

        for row in in_reader:
            yield dict(zip(headers, row))

def write_transactions(transactions, output_file):
    with open(output_file, 'w') as csvout:
        fieldnames = ['Date', 'Payee', 'Memo', 'Amount']
        out_writer = csv.DictWriter(csvout, delimiter=',', quotechar='"', fieldnames=fieldnames, extrasaction='ignore')
        out_writer.writeheader()

        for row in transactions:
            if len(row['Amount (total)']) > 0:
                is_outflow = True if row['Amount (total)'][0] == '-' else False
                date = datetime.strptime(row['Datetime'], '%Y-%m-%dT%H:%M:%S')
                out_writer.writerow({
                    'Date': date.strftime('%m/%d/%Y'),
                    'Payee': row['From'] if is_outflow else row['To'],
                    'Memo': row['Note'],
                    'Amount': '{}{}'.format('-' if is_outflow else '', row['Amount (total)'][2:]),
                })

if __name__ == '__main__':
    transactions = []
    for input_file in sys.argv[1:-1]:
        transactions += list(read_transactions(input_file))
    
    write_transactions(transactions, sys.argv[-1])
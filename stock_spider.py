# stock_spider.py
# Description: Obtain stock data

import yahoo_finance
import urllib.request
import csv

URL_SNP_CSV = 'https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv'

def get_snp_constituents():
    resp = urllib.request.urlopen(URL_SNP_CSV)
    string = resp.read().decode('utf-8').splitlines()
    csvreader = csv.reader(string)
    next(csvreader, None) # skip header
    
    constituents = []
    
    for row in csvreader:
        constituents.append(row)
        print(row)
    return constituents

def get_symbol_price(symbol):
    # Probably could multithread this to speed up the API request
    yahoo_stock = yahoo_finance.Share(symbol)
    return yahoo_stock.get_price()
    
if __name__ == '__main__':
    snp500 = get_snp_constituents()
    for row in snp500:
        print("{} [{}]: {}".format(row[0], row[1], get_symbol_price(row[0])))

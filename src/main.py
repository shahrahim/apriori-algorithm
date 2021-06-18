import os
import csv
from rich.table import Table
from rich.console import Console
from collections import Counter
import random
import itertools

def get_transactions(db_file):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        return list(reader)

def apriori_algo(db_file, support, confidence):
    transactions = get_transactions(db_file)
    display_transaction_table(transactions)

    run_algo(transactions, support, confidence)

def run_algo(transactions, support, confidence):
    item_bucket = get_initial_item_bucket(transactions)

    num_transactions = len(transactions[1:])

    current_f = {}

    for i in itertools.count(start=1):
        itemset_tracker = set()

        display_itemset_table(item_bucket,f"C{i}")

        prune_itemset(item_bucket, itemset_tracker, num_transactions, support)

        if(len(item_bucket) == 0):
            break

        current_f = item_bucket
        display_itemset_table(current_f, f"F{i}")

        itemsets = itertools.combinations(itemset_tracker, i+1)
        item_bucket = get_item_bucket(transactions, item_bucket, itemsets)

def prune_itemset(item_bucket, itemset_tracker, num_transactions, support):
    for item in item_bucket.copy():
        if not is_frequent_item(support, item_bucket[item], num_transactions):
            del item_bucket[item]

    for item in item_bucket.keys():
        itemset_tracker.update(item.split(","))

def get_initial_item_bucket(transactions):
    item_bucket = {}

    for row in transactions[1:]:
        for item in row[1:]:
            item_str = item.lstrip()

            if item_str not in item_bucket:
                item_bucket[item_str] = 0
            item_bucket[item_str]+=1

    return item_bucket

def get_item_bucket(transactions, orig_item_bucket, itemsets):
    item_bucket = {}
    for itemset in itemsets:
        item_str = ','.join(itemset)

        if item_str not in item_bucket:
            item_bucket[item_str] = 0

        for transaction in transactions[1:]:
            if is_itemset_present(transaction, itemset):
                item_bucket[item_str] +=1

    return item_bucket

def is_itemset_present(transaction, itemset):
    return all(x in transaction for x in list(itemset))

def is_frequent_item(support, num_occurences, num_transactions):
    return (num_occurences/num_transactions) >= support

def get_formatted_item(item):
    return f"{{{item}}}"

def display_transaction_table(transactions):
    table = Table()
    table.add_column("TID")
    table.add_column("Items")

    for transaction in transactions[1:]:
        table.add_row(transaction[0], ','.join(transaction[1:]))

    console = Console()
    console.print(table)

def display_itemset_table(item_bucket, display_type):
    table = Table()
    table.add_column("Itemset")
    table.add_column("Support")

    for item in item_bucket:
        table.add_row(get_formatted_item(item), str(item_bucket[item]))

    console = Console()
    console.print("\n")
    console.print(display_type, style="bold blue")
    console.print(table)

filename = os.path.join(os.getcwd(), 'db_2.csv')

apriori_algo(filename, random.randint(15,20) / 100, random.randint(15,40) / 100)
# apriori_algo(filename, 40 / 100, random.randint(15,40) / 100)

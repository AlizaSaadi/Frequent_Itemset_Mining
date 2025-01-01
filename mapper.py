#!/usr/bin/env python3

import sys
import itertools

# Function to generate candidate itemsets of size k
def generate_candidate_itemsets(itemsets, k):
    candidates = []
    # Generate combinations of size k
    for subset in itertools.combinations(itemsets, k):
        candidates.append(subset)
    return candidates

transactions = []
for line in sys.stdin:
    # Split the line into individual items
    items = line.strip().split()
    transactions.append(items)

min_support = 2
k = 1


item_counts = {}
for transaction in transactions:
    for item in transaction:
        item_counts[item] = item_counts.get(item, 0) + 1

for item, count in item_counts.items():
    if count >= min_support:
        print(f"{item}\t{count}")

while True:
    candidate_itemsets = generate_candidate_itemsets(item_counts.keys(), k+1)
    if not candidate_itemsets:
        break

    item_counts = {}
    for transaction in transactions:
        for candidate_set in candidate_itemsets:
            if all(item in transaction for item in candidate_set):
                item_counts[candidate_set] = item_counts.get(candidate_set, 0) + 1

    for itemset, count in item_counts.items():
        if count >= min_support:
            itemset_str = ' '.join(itemset)
            print(f"{itemset_str}\t{count}")

    # Increment itemset length for next iteration
    k += 1


#!/usr/bin/env python3

import sys
from collections import defaultdict

item_counts = defaultdict(int)
itemset_counts = defaultdict(int)

for line in sys.stdin:
    itemset, count = line.strip().split('\t')
    items = itemset.split()
    item_counts[itemset] = int(count)
    for item in items:
        itemset_counts[item] += int(count)

for itemset in item_counts.keys():
    items = itemset.split()
    if len(items) > 1:
        for i in range(1, len(items)):
            antecedent = items[:i]
            consequent = items[i:]
            antecedent_str = ' '.join(antecedent)
            consequent_str = ' '.join(consequent)
            confidence = item_counts[itemset] / item_counts[antecedent_str]
            expected_confidence = item_counts[itemset] / itemset_counts[antecedent[-1]]
            interest = confidence - expected_confidence
            print(f"{antecedent_str} => {consequent_str}\n confidence = {confidence}\n interest = {interest}\n")


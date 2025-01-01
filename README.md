This project implements a MapReduce-based algorithm for frequent itemset mining and association rule generation. The mapper generates candidate itemsets and computes their frequency, while the reducer calculates confidence and interest for association rules.

Features:

Frequent Itemset Mining: Identifies frequent itemsets with a minimum support threshold using the Apriori algorithm.

Association Rule Generation: Produces rules with confidence and interest metrics for each association.

Scalable MapReduce Framework: Designed to process large datasets in a distributed environment.

Requirements:

Python 3.x

Hadoop or any MapReduce-compatible framework

Code Highlights:

Mapper (mapper.py)
-> Frequent Itemset Generation:
    Generates candidate itemsets of increasing sizes (k) using combinations.
    Filters itemsets based on the minimum support threshold.

Reducer (reducer.py)
-> Support and Confidence:
    Aggregates itemset counts and computes confidence for association rules.
    Calculates interest to assess the strength of rules beyond expected frequency.

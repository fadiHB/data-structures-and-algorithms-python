# Hashtables

In computing, a hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.

## Challenge

Implement a Hashtable

## Approach & Efficiency

| Method | Time | Space |
| :----------- | :----------- | :----------- |
| add |O(1) | O(1) |
| get |O(n) | O(1) |
| contains |O(n) | O(1) |
| get_hash |O(n) | O(1) |

## API
<!-- Description of each method publicly available in each of your hashtable -->
* add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
* get: takes in the key and returns the value from the table.
* contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
* get_hash: takes in an arbitrary key and returns an index in the collection.

[PR_link](https://github.com/fadiHB/data-structures-and-algorithms-python-401d2/pull/29)
# Hash Table in Python

A hash table built from scratch in Python, with no built-in hash functions.

## How it works

The hash function adds up the Unicode code point of every character in the key. For example, `golf` hashes to 424. That number is used as the bucket where the key-value pair is stored.

Keys that hash to the same number share one bucket, which is a nested dictionary. For example, `fcc` and `cfc` both hash to 300:

```python
{300: {"fcc": "coding", "cfc": "chemical"}}
```

## Methods

| Method | What it does |
| --- | --- |
| `hash(string)` | Returns the sum of the code points in the string |
| `add(key, value)` | Stores the pair in the bucket for the key's hash |
| `remove(key)` | Deletes only that key's pair, and does nothing if the key is missing |
| `lookup(key)` | Returns the value for the key, or `None` if it is missing |

## Usage

```python
from hash_table import HashTable

ht = HashTable()
ht.add("golf", "sport")
print(ht.lookup("golf"))   # sport
ht.remove("golf")
print(ht.lookup("golf"))   # None
```

## Run the tests

```bash
python -m unittest -v
```

## Files

- `hash_table.py`: the `HashTable` class
- `test_hash_table.py`: unit tests covering each requiremen

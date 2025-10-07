
A **dictionary** in Python is a collection of comma-separated key-value pairs enclosed within curly braces `{}`. It is an ordered, mutable, and indexed data structure that does not allow duplicate keys. From Python 3.7 onward, dictionaries maintain insertion order.

## Syntax and Structure

Dictionaries are defined using curly braces `{}` with key-value pairs separated by colons `:` and pairs separated by commas.
For example:

```python
var = {k1: v1, k2: v2, k3: v3}
```

A practical example is:

```python
square = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(type(square))  # <class 'dict'>
```

Keys must be unique and immutable (e.g., strings, integers, or tuples), while values can be any data type and may be duplicated.[^1][^2]

## Key Characteristics

- **Uniqueness of Keys**: Each key must be unique. If a duplicate key is used, the last value assigned to that key will overwrite the previous one.[^2][^1]
- **Immutability of Keys**: Keys must be of an immutable type such as strings, integers, or tuples. Mutable types like lists cannot be used as keys.[^3][^2]
- **Mutability of Dictionary**: The dictionary itself is mutable—meaning you can add, modify, or remove key-value pairs after creation.[^1][^2]

For instance:

```python
numbers = {1: 1, 2: 4, 3: 6, 4: 16, 5: 25, 3: 9}
print(numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Here, the key `3` appears twice, but only the last value `9` is retained.[^4][^2]

## Dictionary Methods

Python provides several built-in methods for manipulating dictionaries:


| Method | Description |
| :-- | :-- |
| `clear()` | Removes all elements from the dictionary [^5] |
| `copy()` | Returns a shallow copy of the dictionary [^5] |
| `fromkeys(keys, value)` | Creates a new dictionary with specified keys and value [^5] |
| `get(key, default)` | Returns the value for the key, or default if key not found [^5] |
| `items()` | Returns a view of key-value pairs as tuples [^5] |
| `keys()` | Returns a view of all keys [^5] |
| `pop(key, default)` | Removes and returns the value for the specified key [^5] |
| `popitem()` | Removes and returns the last inserted key-value pair [^5] |
| `setdefault(key, default)` | Returns value if key exists, else inserts key with default value [^5] |
| `update(dict)` | Updates the dictionary with key-value pairs from another dictionary [^5] |
| `values()` | Returns a view of all values [^5] |

These methods allow efficient access, modification, and traversal of dictionary data. For example, `items()` enables iterating over both keys and values simultaneously.[^6][^4]

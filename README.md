# 🔢 Big Integer ADT — Linked List Practicum

> Platform-independent arbitrary-precision integers implemented in Python, using both a **singly linked list** and a **Python list** as the underlying storage.

---

## 📋 Table of Contents

- [Background](#-background)
- [Project Structure](#-project-structure)
- [Features](#-features)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
  - [Creating a BigInteger](#creating-a-biginteger)
  - [toString](#tostring)
  - [comparable](#comparable)
  - [arithmetic](#arithmetic)
  - [bitwise\_ops](#bitwise_ops)
  - [Assignment Combo Operators](#assignment-combo-operators)
- [Implementation Details](#-implementation-details)
- [Assignment Reference](#-assignment-reference)

---

## 📖 Background

Hardware integers are limited by architecture (e.g., ±2,147,483,647 on 32-bit systems).
When we need integers with **more than 19 digits**, we must implement them in software.

This project defines a **Big Integer ADT** that stores each decimal digit in a separate node/element, supporting:

- Arbitrarily large (and small) integer values
- All standard arithmetic and bitwise operators
- Python-style assignment combo operators

---

## 📁 Project Structure

```
big-integer-adt/
│
├── big_integer_linked_list.py   # Problem 1(a) + Problem 2 — Singly Linked List
├── big_integer_list.py          # Problem 1(b) + Problem 2 — Python List
└── README.md
```

---

## ✨ Features

### Problem 1 — Core ADT

| Method | Description |
|---|---|
| `BigInteger(initValue="0")` | Construct from a decimal string |
| `toString()` | Return decimal string representation |
| `comparable(other, op)` | Compare with `<`, `<=`, `>`, `>=`, `==`, `!=` |
| `arithmetic(rhsInt, op)` | Arithmetic: `+`, `-`, `*`, `//`, `%`, `**` |
| `bitwise_ops(rhsInt, op)` | Bitwise: `\|`, `&`, `^`, `<<`, `>>` |

### Problem 2 — Assignment Combo Operators

| Arithmetic | Bitwise |
|---|---|
| `+=` `-=` `*=` `//=` `%=` `**=` | `<<=` `>>=` `\|=` `&=` `^=` |

---

## 🚀 Getting Started

No external dependencies required — only the **Python Standard Library**.

```bash
# Clone the repository
git clone https://github.com/<your-username>/big-integer-adt.git
cd big-integer-adt

# Run the linked list demo
python big_integer_linked_list.py

# Run the Python list demo
python big_integer_list.py
```

> Requires **Python 3.7+**

---

## 📌 Usage

### Creating a BigInteger

```python
from big_integer_linked_list import BigInteger  # or big_integer_list

a = BigInteger("45839")
b = BigInteger("100")
c = BigInteger("-250")

print(a)   # 45839
print(c)   # -250
```

---

### toString

```python
a = BigInteger("123456789012345678901234567890")
print(a.toString())
# 123456789012345678901234567890
```

---

### comparable

```python
a = BigInteger("500")
b = BigInteger("300")

print(a.comparable(b, '>'))    # True
print(a.comparable(b, '=='))   # False
print(a.comparable(b, '!='))   # True

# Also works with Python operators directly:
print(a > b)    # True
print(a == b)   # False
```

---

### arithmetic

```python
a = BigInteger("45839")
b = BigInteger("100")

print(a.arithmetic(b, '+'))    # 45939
print(a.arithmetic(b, '-'))    # 45739
print(a.arithmetic(b, '*'))    # 4583900
print(a.arithmetic(b, '//'))   # 458
print(a.arithmetic(b, '%'))    # 39
print(b.arithmetic(BigInteger("3"), '**'))  # 1000000

# Also works with Python operators directly:
print(a + b)    # 45939
print(a * b)    # 4583900
```

---

### bitwise_ops

```python
x = BigInteger("12")   # binary: 1100
y = BigInteger("10")   # binary: 1010

print(x.bitwise_ops(y, '|'))              # 14  (1110)
print(x.bitwise_ops(y, '&'))              # 8   (1000)
print(x.bitwise_ops(y, '^'))              # 6   (0110)
print(x.bitwise_ops(BigInteger("2"), '<<'))  # 48
print(x.bitwise_ops(BigInteger("1"), '>>'))  # 6

# Also works with Python operators directly:
print(x | y)    # 14
print(x << BigInteger("2"))    # 48
```

---

### Assignment Combo Operators

```python
z = BigInteger("50")

z += BigInteger("10")   # z = 60
z -= BigInteger("5")    # z = 55
z *= BigInteger("3")    # z = 165
z //= BigInteger("2")   # z = 82
z %= BigInteger("7")    # z = 5
z **= BigInteger("3")   # z = 125

w = BigInteger("60")
w <<= BigInteger("2")   # w = 240
w >>= BigInteger("1")   # w = 120
w |=  BigInteger("15")  # w = 127
w &=  BigInteger("63")  # w = 63
w ^=  BigInteger("5")   # w = 58
```

---

## 🔧 Implementation Details

### Linked List (`big_integer_linked_list.py`)

Digits are stored in a **singly linked list**, with the **head pointing to the least-significant digit**.

```
Integer 45839:

head → [9] → [3] → [8] → [5] → [4] → None
        ↑                              ↑
  least-significant            most-significant
```

Each `_Node` holds:
- `digit` — a single decimal digit (0–9)
- `next`  — reference to the next node

### Python List (`big_integer_list.py`)

Digits are stored in a **Python list** with the same logical ordering:

```
Integer 45839:

_digits = [9, 3, 8, 5, 4]
            ↑           ↑
     least-sig     most-sig
```

Both implementations share the same public API, making them drop-in interchangeable.

---

## 📚 Assignment Reference

| Problem | Description | File |
|---|---|---|
| **1(a)** | Big Integer ADT using a singly linked list | `big_integer_linked_list.py` |
| **1(b)** | Big Integer ADT using a Python list | `big_integer_list.py` |
| **2**    | Add assignment combo operators (`+=`, `-=`, `*=`, `//=`, `%=`, `**=`, `<<=`, `>>=`, `\|=`, `&=`, `^=`) to both implementations | Both files |

---

## 🧑‍💻 Author

> *Praktikum Struktur Data — Linked List*

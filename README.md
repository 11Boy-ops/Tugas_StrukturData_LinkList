# 🔢 Big Integer ADT — Praktikum Linked List

> Bilangan bulat presisi arbitrer yang tidak bergantung pada platform, diimplementasikan dalam Python menggunakan **singly linked list** dan **Python list** sebagai penyimpanan data.

---

## 📋 Daftar Isi

- [Latar Belakang](#-latar-belakang)
- [Struktur Proyek](#-struktur-proyek)
- [Fitur](#-fitur)
- [Memulai](#-memulai)
- [Penggunaan](#-penggunaan)
  - [Membuat BigInteger](#membuat-biginteger)
  - [toString](#tostring)
  - [comparable](#comparable)
  - [arithmetic](#arithmetic)
  - [bitwise\_ops](#bitwise_ops)
  - [Operator Penugasan Kombinasi](#operator-penugasan-kombinasi)
- [Detail Implementasi](#-detail-implementasi)
- [Referensi Tugas](#-referensi-tugas)

---

## 📖 Latar Belakang

Bilangan bulat pada perangkat keras dibatasi oleh arsitektur (misalnya, ±2.147.483.647 pada sistem 32-bit).
Ketika kita membutuhkan bilangan bulat dengan **lebih dari 19 digit**, kita harus mengimplementasikannya secara perangkat lunak.

Proyek ini mendefinisikan **Big Integer ADT** yang menyimpan setiap digit desimal dalam node/elemen terpisah, dengan dukungan:

- Nilai bilangan bulat yang sangat besar (dan kecil) secara arbitrer
- Semua operator aritmatika dan bitwise standar
- Operator penugasan kombinasi bergaya Python

---

## 📁 Struktur Proyek

```
big-integer-adt/
│
├── big_integer_linked_list.py   # Soal 1(a) + Soal 2 — Singly Linked List
├── big_integer_list.py          # Soal 1(b) + Soal 2 — Python List
└── README.md
```

---

## ✨ Fitur

### Soal 1 — ADT Inti

| Metode | Deskripsi |
|---|---|
| `BigInteger(initValue="0")` | Konstruksi dari string desimal |
| `toString()` | Mengembalikan representasi string desimal |
| `comparable(other, op)` | Membandingkan dengan `<`, `<=`, `>`, `>=`, `==`, `!=` |
| `arithmetic(rhsInt, op)` | Aritmatika: `+`, `-`, `*`, `//`, `%`, `**` |
| `bitwise_ops(rhsInt, op)` | Bitwise: `\|`, `&`, `^`, `<<`, `>>` |

### Soal 2 — Operator Penugasan Kombinasi

| Aritmatika | Bitwise |
|---|---|
| `+=` `-=` `*=` `//=` `%=` `**=` | `<<=` `>>=` `\|=` `&=` `^=` |

---

## 🚀 Memulai

Tidak diperlukan dependensi eksternal — hanya **Python Standard Library**.

```bash
# Clone repositori
git clone https://github.com/<username-anda>/big-integer-adt.git
cd big-integer-adt

# Jalankan demo linked list
python big_integer_linked_list.py

# Jalankan demo Python list
python big_integer_list.py
```

> Membutuhkan **Python 3.7+**

---

## 📌 Penggunaan

### Membuat BigInteger

```python
from big_integer_linked_list import BigInteger  # atau big_integer_list

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

# Juga bisa menggunakan operator Python langsung:
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

# Juga bisa menggunakan operator Python langsung:
print(a + b)    # 45939
print(a * b)    # 4583900
```

---

### bitwise_ops

```python
x = BigInteger("12")   # biner: 1100
y = BigInteger("10")   # biner: 1010

print(x.bitwise_ops(y, '|'))              # 14  (1110)
print(x.bitwise_ops(y, '&'))              # 8   (1000)
print(x.bitwise_ops(y, '^'))              # 6   (0110)
print(x.bitwise_ops(BigInteger("2"), '<<'))  # 48
print(x.bitwise_ops(BigInteger("1"), '>>'))  # 6

# Juga bisa menggunakan operator Python langsung:
print(x | y)    # 14
print(x << BigInteger("2"))    # 48
```

---

### Operator Penugasan Kombinasi

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

## 🔧 Detail Implementasi

### Linked List (`big_integer_linked_list.py`)

Digit disimpan dalam **singly linked list**, dengan **head menunjuk ke digit paling tidak signifikan**.

```
Bilangan 45839:

head → [9] → [3] → [8] → [5] → [4] → None
        ↑                              ↑
  paling tidak signifikan       paling signifikan
```

Setiap `_Node` menyimpan:
- `digit` — satu digit desimal (0–9)
- `next`  — referensi ke node berikutnya

### Python List (`big_integer_list.py`)

Digit disimpan dalam **Python list** dengan urutan logika yang sama:

```
Bilangan 45839:

_digits = [9, 3, 8, 5, 4]
            ↑           ↑
     paling tdk sig   paling sig
```

Kedua implementasi memiliki API publik yang sama sehingga dapat digunakan secara bergantian.

---

## 📚 Referensi Tugas

| Soal | Deskripsi | File |
|---|---|---|
| **1(a)** | Big Integer ADT menggunakan singly linked list | `big_integer_linked_list.py` |
| **1(b)** | Big Integer ADT menggunakan Python list | `big_integer_list.py` |
| **2**    | Menambahkan operator penugasan kombinasi (`+=`, `-=`, `*=`, `//=`, `%=`, `**=`, `<<=`, `>>=`, `\|=`, `&=`, `^=`) ke kedua implementasi | Kedua file |

---

## 🧑‍💻 Penulis

> *Praktikum Struktur Data — Linked List*

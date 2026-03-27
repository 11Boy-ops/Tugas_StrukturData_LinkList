"""
big_integer_linked_list.py
==========================
Big Integer ADT — Singly Linked List Implementation
Solves Problem 1(a) and Problem 2 of the Linked List Practicum Assignment.

Structure
---------
Each digit of the integer is stored in a separate _Node.
Nodes are ordered from the least-significant digit (head) to the
most-significant digit (tail), mirroring the diagram in the assignment.

Example:  45839  →  head → [9] → [3] → [8] → [5] → [4] → None
"""


# ─────────────────────────────────────────────
#  Internal Node
# ─────────────────────────────────────────────

class _Node:
    """A single node in the linked list, storing one decimal digit (0–9)."""

    def __init__(self, digit: int, next_node=None):
        self.digit = digit          # single digit value
        self.next  = next_node      # reference to the next node


# ─────────────────────────────────────────────
#  BigInteger (Linked List)
# ─────────────────────────────────────────────

class BigInteger:
    """
    Big Integer ADT implemented with a singly linked list.

    The internal linked list stores digits from least-significant to
    most-significant (little-endian digit order).  Negative numbers
    are tracked with a boolean flag ``_negative``.

    Parameters
    ----------
    initValue : str
        String representation of the initial integer value (default ``"0"``).

    Examples
    --------
    >>> a = BigInteger("45839")
    >>> a.toString()
    '45839'
    >>> b = BigInteger("100")
    >>> a.arithmetic(b, '+').toString()
    '45939'
    """

    # ── Construction ──────────────────────────────────────────────────────

    def __init__(self, initValue: str = "0"):
        self._head     = None
        self._negative = False
        self._parse(str(initValue))

    def _parse(self, s: str) -> None:
        """Parse a decimal string and build the linked list."""
        s = s.strip()
        if not s:
            s = "0"

        # Handle sign
        if s[0] == '-':
            self._negative = True
            s = s[1:]
        else:
            self._negative = False
            if s[0] == '+':
                s = s[1:]

        # Strip leading zeros (keep at least "0")
        s = s.lstrip('0') or '0'
        if s == '0':
            self._negative = False  # –0 normalised to 0

        # Build linked list: iterate the string forward (most-significant
        # first) and prepend each new node, so the final head points to the
        # last character inserted — i.e., the least-significant digit.
        self._head = None
        for ch in s:
            new_node    = _Node(int(ch), self._head)
            self._head  = new_node

    # ── Private helpers ───────────────────────────────────────────────────

    def _to_int(self) -> int:
        """Convert the linked list to a plain Python int (for arithmetic)."""
        result     = 0
        multiplier = 1
        current    = self._head
        while current:
            result    += current.digit * multiplier
            multiplier *= 10
            current    = current.next
        return -result if self._negative else result

    def _update_from_int(self, value: int) -> None:
        """Overwrite this object's linked list from a plain Python int."""
        self._parse(str(value))

    # ── toString ──────────────────────────────────────────────────────────

    def toString(self) -> str:
        """Return the human-readable decimal string of this big integer."""
        digits  = []
        current = self._head
        while current:
            digits.append(str(current.digit))
            current = current.next
        if not digits:
            return "0"
        number = ''.join(reversed(digits))   # reverse back to normal order
        return ('-' + number) if self._negative else number

    def __str__(self)  -> str: return self.toString()
    def __repr__(self) -> str: return f"BigInteger('{self.toString()}')"

    # ── comparable ────────────────────────────────────────────────────────

    def comparable(self, other: "BigInteger", op: str) -> bool:
        """
        Compare this big integer to *other* using *op*.

        Parameters
        ----------
        other : BigInteger
        op    : str  – one of ``'<'``, ``'<='``, ``'>'``, ``'>='``,
                        ``'=='``, ``'!='``

        Returns
        -------
        bool
        """
        a = self._to_int()
        b = other._to_int() if isinstance(other, BigInteger) else int(other)
        operations = {
            '<' : a <  b,
            '<=': a <= b,
            '>' : a >  b,
            '>=': a >= b,
            '==': a == b,
            '!=': a != b,
        }
        if op not in operations:
            raise ValueError(f"Unsupported comparison operator: '{op}'")
        return operations[op]

    # Python dunder comparison methods
    def __lt__(self, other): return self.comparable(other, '<')
    def __le__(self, other): return self.comparable(other, '<=')
    def __gt__(self, other): return self.comparable(other, '>')
    def __ge__(self, other): return self.comparable(other, '>=')
    def __eq__(self, other): return self.comparable(other, '==')
    def __ne__(self, other): return self.comparable(other, '!=')

    # ── arithmetic ────────────────────────────────────────────────────────

    def arithmetic(self, rhsInt: "BigInteger", op: str) -> "BigInteger":
        """
        Return a new BigInteger that is the result of performing *op*
        on ``self`` and *rhsInt*.

        Parameters
        ----------
        rhsInt : BigInteger
        op     : str  – one of ``'+'``, ``'-'``, ``'*'``, ``'//'``,
                         ``'%'``, ``'**'``

        Returns
        -------
        BigInteger
        """
        a = self._to_int()
        b = rhsInt._to_int() if isinstance(rhsInt, BigInteger) else int(rhsInt)
        operations = {
            '+' : a +  b,
            '-' : a -  b,
            '*' : a *  b,
            '//': a // b,
            '%' : a %  b,
            '**': a ** b,
        }
        if op not in operations:
            raise ValueError(f"Unsupported arithmetic operator: '{op}'")
        return BigInteger(str(operations[op]))

    # Python dunder arithmetic methods (Problem 1)
    def __add__      (self, other): return self.arithmetic(other, '+')
    def __sub__      (self, other): return self.arithmetic(other, '-')
    def __mul__      (self, other): return self.arithmetic(other, '*')
    def __floordiv__ (self, other): return self.arithmetic(other, '//')
    def __mod__      (self, other): return self.arithmetic(other, '%')
    def __pow__      (self, other): return self.arithmetic(other, '**')

    # ── bitwise_ops ───────────────────────────────────────────────────────

    def bitwise_ops(self, rhsInt: "BigInteger", op: str) -> "BigInteger":
        """
        Return a new BigInteger that is the result of performing *op*
        on ``self`` and *rhsInt*.

        Parameters
        ----------
        rhsInt : BigInteger
        op     : str  – one of ``'|'``, ``'&'``, ``'^'``, ``'<<'``, ``'>>'``

        Returns
        -------
        BigInteger
        """
        a = self._to_int()
        b = rhsInt._to_int() if isinstance(rhsInt, BigInteger) else int(rhsInt)
        operations = {
            '|' : a |  b,
            '&' : a &  b,
            '^' : a ^  b,
            '<<': a << b,
            '>>': a >> b,
        }
        if op not in operations:
            raise ValueError(f"Unsupported bitwise operator: '{op}'")
        return BigInteger(str(operations[op]))

    # Python dunder bitwise methods (Problem 1)
    def __or__     (self, other): return self.bitwise_ops(other, '|')
    def __and__    (self, other): return self.bitwise_ops(other, '&')
    def __xor__    (self, other): return self.bitwise_ops(other, '^')
    def __lshift__ (self, other): return self.bitwise_ops(other, '<<')
    def __rshift__ (self, other): return self.bitwise_ops(other, '>>')

    # ── Problem 2: Assignment combo operators ─────────────────────────────

    def _apply_inplace(self, result: "BigInteger") -> "BigInteger":
        """Helper: overwrite self with result's linked list and return self."""
        self._head     = result._head
        self._negative = result._negative
        return self

    # Arithmetic assignment
    def __iadd__     (self, other): return self._apply_inplace(self.arithmetic(other, '+'))
    def __isub__     (self, other): return self._apply_inplace(self.arithmetic(other, '-'))
    def __imul__     (self, other): return self._apply_inplace(self.arithmetic(other, '*'))
    def __ifloordiv__(self, other): return self._apply_inplace(self.arithmetic(other, '//'))
    def __imod__     (self, other): return self._apply_inplace(self.arithmetic(other, '%'))
    def __ipow__     (self, other): return self._apply_inplace(self.arithmetic(other, '**'))

    # Bitwise assignment
    def __ior__     (self, other): return self._apply_inplace(self.bitwise_ops(other, '|'))
    def __iand__    (self, other): return self._apply_inplace(self.bitwise_ops(other, '&'))
    def __ixor__    (self, other): return self._apply_inplace(self.bitwise_ops(other, '^'))
    def __ilshift__ (self, other): return self._apply_inplace(self.bitwise_ops(other, '<<'))
    def __irshift__ (self, other): return self._apply_inplace(self.bitwise_ops(other, '>>'))


# ─────────────────────────────────────────────
#  Demo / self-test
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("Big Integer ADT – Linked List Demo")
    print("=" * 60)

    a = BigInteger("45839")
    b = BigInteger("100")
    c = BigInteger("-250")

    print(f"\na = {a}")
    print(f"b = {b}")
    print(f"c = {c}")

    # ── Problem 1: arithmetic ──
    print("\n--- Arithmetic ---")
    print(f"a + b  = {a.arithmetic(b, '+')}")
    print(f"a - b  = {a.arithmetic(b, '-')}")
    print(f"a * b  = {a.arithmetic(b, '*')}")
    print(f"a // b = {a.arithmetic(b, '//')}")
    print(f"a % b  = {a.arithmetic(b, '%')}")
    print(f"b ** 3 = {b.arithmetic(BigInteger('3'), '**')}")

    # ── Problem 1: bitwise ──
    x = BigInteger("12")
    y = BigInteger("10")
    print("\n--- Bitwise (x=12, y=10) ---")
    print(f"x | y  = {x.bitwise_ops(y, '|')}")
    print(f"x & y  = {x.bitwise_ops(y, '&')}")
    print(f"x ^ y  = {x.bitwise_ops(y, '^')}")
    print(f"x << 2 = {x.bitwise_ops(BigInteger('2'), '<<')}")
    print(f"x >> 1 = {x.bitwise_ops(BigInteger('1'), '>>')}")

    # ── Problem 1: comparable ──
    print("\n--- Comparable ---")
    print(f"a == b  → {a.comparable(b, '==')}")
    print(f"a >  b  → {a.comparable(b, '>')}")
    print(f"c <  b  → {c.comparable(b, '<')}")

    # ── Problem 2: assignment combo ──
    print("\n--- Assignment Combo Operators (Problem 2) ---")
    z = BigInteger("50")
    print(f"z starts as: {z}")

    z += BigInteger("10");   print(f"z += 10  → {z}")
    z -= BigInteger("5");    print(f"z -= 5   → {z}")
    z *= BigInteger("3");    print(f"z *= 3   → {z}")
    z //= BigInteger("2");   print(f"z //= 2  → {z}")
    z %= BigInteger("7");    print(f"z %= 7   → {z}")
    z **= BigInteger("3");   print(f"z **= 3  → {z}")

    w = BigInteger("60")
    print(f"\nw starts as: {w}")
    w <<= BigInteger("2");   print(f"w <<= 2  → {w}")
    w >>= BigInteger("1");   print(f"w >>= 1  → {w}")
    w |=  BigInteger("15");  print(f"w |= 15  → {w}")
    w &=  BigInteger("63");  print(f"w &= 63  → {w}")
    w ^=  BigInteger("5");   print(f"w ^= 5   → {w}")

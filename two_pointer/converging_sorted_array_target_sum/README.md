# Two Pointers – Converging Pattern

The **Converging Two Pointers** pattern is used on **sorted arrays** to find pairs or triplets that satisfy a condition (usually a target sum).

---

## Core Idea
- Use two pointers:
  - `left` starts at the beginning
  - `right` starts at the end
- Compare values at both pointers and move them **towards each other** based on the condition.

---

## Pointer Movement Logic
- If `sum < target` → move `left` right (increase value)
- If `sum > target` → move `right` left (decrease value)
- If `sum == target` → record result

---

## Why It Works
- Sorting gives order
- Pointer movement is predictable
- Avoids checking all pairs

---

## Complexity
- **Time:** `O(n)` for pairs, `O(n²)` for triplets (e.g. 3Sum)
- **Space:** `O(1)` extra space

---

## Common Problems
- Two Sum II (sorted array)
- 3Sum
- Container With Most Water
- Remove Duplicates from Sorted Array

---

## When to Use
- Array is sorted (or can be sorted)
- Problem asks for pair / triplet conditions
- Brute force is too slow

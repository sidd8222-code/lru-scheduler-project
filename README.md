# 🚀 LRU Cache & Event Scheduler

## 📌 Overview

This project demonstrates the implementation of two core computer science problems:

* **LRU Cache (Least Recently Used Cache)** with O(1) operations
* **Event Scheduler** for detecting overlaps and calculating minimum meeting rooms
* **Room Assignment System** using a priority queue (heap)

The goal of this project is to showcase strong understanding of **data structures, algorithms, and system design fundamentals**.

---

## 🧠 Problem 1: LRU Cache

### 🔹 Description

Implemented an LRU Cache that supports:

* `get(key)` → returns value or -1
* `put(key, value)` → inserts/updates value and evicts least recently used item

### ⚙️ Approach

* Used a **Hash Map** for O(1) lookup
* Used a **Doubly Linked List** to maintain usage order
* Most recently used items are moved to the front
* Least recently used items are removed from the tail

### ⏱ Complexity

* Time: **O(1)** for both `get` and `put`
* Space: **O(n)**

---

## 🧠 Problem 2: Event Scheduler

### 🔹 Features

* Check if all events can be attended (no overlap)
* Calculate minimum number of rooms required
* Assign room numbers dynamically

### ⚙️ Approach

* Sorted events based on start time
* Used **two-pointer technique** to detect overlaps
* Used a **min heap (priority queue)** for room assignment

### ⏱ Complexity

* Time: **O(n log n)**
* Space: **O(n)**

---

## 🧪 Testing

Unit tests are implemented using Python’s `unittest` framework.

### ▶️ Run Tests

```bash
python3 -m unittest discover tests
```

---

## ▶️ How to Run

```bash
python3 main.py
```

---

## 📂 Project Structure

```
lru_scheduler_project/
│
├── lru_cache.py        # LRU Cache implementation
├── scheduler.py        # Event scheduling logic
├── main.py             # Entry point for execution
├── tests/
│   └── test_all.py     # Unit tests
├── README.md
└── venv/
```

---

## ⚡ Key Highlights

* ✅ O(1) optimized LRU Cache
* ✅ Efficient scheduling using sorting & pointers
* ✅ Heap-based room allocation (advanced feature)
* ✅ Unit testing included
* ✅ Edge case handl

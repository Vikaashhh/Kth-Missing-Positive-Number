# Day 35: Kth Missing Positive Number in a Sorted Array
## 🧠 Problem Statement
Given a sorted array of distinct positive integers arr[], and an integer k, find the kth positive number that is missing from arr[].

## Constraints:

arr[] is strictly increasing.

Missing numbers are the ones that are not in arr[] but would be in a continuous sequence starting from 1.

## 📥 Input
arr[] = [2, 3, 5, 6]

k = 2

## 🔁 Output
4

## Explanation: 
The numbers missing from the array are: [1, 4]. The 2nd missing is 4.

## ✅ Approach
🔎 Binary Search (Optimized)
We use binary search to find the position where the count of missing numbers becomes at least k.

## 📌 Steps:
Define the number of missing values at index i as arr[i] - (i + 1)

Apply binary search on the index range [0, len(arr) - 1]

If missing < k, search right; otherwise, search left.

Return low + k, which gives the kth missing number.

## 🧩 Concepts Practiced
Binary Search

Missing Elements Tracking

Mathematical Insight in Sorted Arrays

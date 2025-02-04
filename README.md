Data-structure and Algorithms
------------------------------
This repository contains python implementations for data structures
1. Dynamic Array
   The array of itmes which can grow and shrink. Here, the dynamic array is implemented using static array.
   Array is a linear collection of data items stored ij continguos memory locations
2. Linked List
   A linked list is a linear collection of data items organized in nodes. A node has 2 parts. the actual value and the pointer to the next node. 
   Nodes in a linked list is scattered in the memory but are connected via links.
3. Stack
   Stack is a linear data structure where items are added and removed in LIFO order. i.e. Last In First Out. The items are removed only fromm the top of the Satck
   In Python, Stack can be implemented using arrays (List) or LinkedList (queue or LifoQueue)
   1. Stack using List:
      List requires potential memory reallocation as the stack grows in future
   2. Stack using dequeue:
      Deque is doubly-linked list based ds. Hence does all the operations in O(1) time howmuch ever the stack grows in size.
   3. Stack using LifoQueue:
      LifoQueue is also doubly-linked based ds. It is thread-safe. So the best to use in multi-threaded environment, but compromising the cost of a little bit processing over-head.
   

   

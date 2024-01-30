# DSA interview prep w/ Python

as inspired by https://github.com/kdn251/interviews

View "basic" prerequisite video [here](https://www.youtube.com/watch?v=0K_eZGS5NsU), by Neetcode.io.

Definitely read throughout [this](https://haseebq.com/how-to-break-into-tech-job-hunting-and-interviews/) article by Haseeb Qureshi to feel motivated, guided (and pumped!), specially if you come from a non-cs specific background like me.

View basic algorithms/data structures/techniques roadmap [here](https://neetcode.io/roadmap). This is the base for the leetcode folder.


## Data Structures

---
### Arrays
An array, also called a list in other programming languages, is a data structure allowing the storage of values in continuous spaces of memory.
You can store different types of values such as integers, floats, objects or even other arrays (creating 2D or nd arrays) in them.
In PYTHON, lists are implemented as DYNAMIC ARRAYS, meaning you dont´t need to specify the size of the arrays when declaration is performed.

_Time Complexity:_

- Lookup notation by index = O(1)
- Lookup by value = O(n)
- Array traversal = O(n)
- Array insertion = O(n)
- Array deletion = O(n)

### Linked Lists
Best explanation I found on topic (https://www.youtube.com/watch?v=8hly31xKli0) - Intro to data structures section

Contrary to arrays, which store values on continuous memory location, linked lists store values on random memory locations but each of those also store a reference to the next value in memory.
When we add elements for example, we would just need to change the address located in the element prior to the one we are adding.
We don´t need to preallocate space and insertio is easier.

A <em>double link list</em> would have elements store an address for the element before and after their location.

Link lists are not built in for Python, so there is a need to implement them.

_Time Complexity:_

- Add last element = O(1)
- Remove las element = O(n)
- Linked list traversal = O(n)
- Insert/delete at beginning = O(1)
- Insert/delete at an iterator position O(1)
- Lookup by value = O(n)

### Stacks
The stack data structure is a collection of elements that highlight two basic operations: push (adding elements to the stack) and pop (deleting elements from the stack).

Implements the last-In, First-Out approach, also called LIFO, which states the most recently added element will be removed frist from the strucutre.

_Time Complexity:_

- Search = O(n)
- Access = O(n)
- Insert and Delete (push and pop) - O(1)

### Queues
Consider the stack data structure but now, the element we aim to remove is the first on a queue - FIFO (First In, First Out approach). 
We now call push-add as <em>enqueue</em> and pop-delete as <em>dequeue</em>. The end were elements are added is called tail or back of the queue and the end where elements are removed is called as front or head of the queue.
You can think about a queue as a line of customers waiting for a service.

_Time Complexity:_

- Search = O(n)
- Access = O(n)
- Insert and Delete (enqueue and dequeue) - O(1)
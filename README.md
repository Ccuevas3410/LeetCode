
## Data Structures ##


### Linked List ###

* A **Linked List** is a linear collection of data elements, called nodes, each pointing to the next node by  a pointer. It is a data 
structure consisting of a group of nodes which together represent a sequence.
* **Singly-linked** list: linked list in which each node points to the next node and the last node points to null
* **Doubly-linked** list: linked list in which each node has two pointers, p and n, such that p points to the previous node and n points to the next node; the last node's n pointer points to null
* **Circular-linked** list: linked list in which each node points to the next node and the last node points back to the first node
* Often used in many **List, Queues & Stacks** implementations. It is also used in **Separate Chaining**, which is present in certain Hashtablles to deal with hashing collisions.
* **Time Complexity**:
    * Access: O(n)
    * Search: O(n)
    * Insert: O(1)
    * Remove: O(1)
    
   
### Stack ###   

* A **Stack** is a one ended linear data structure that models a real world stack by only having 2 main operations _push()_ and _pop()_.  Created using a **Linked List** or an **Array**.
* It is a **LIFO (Last In, first out)** data structure. **Pro's**: You can reverse things such as Strings with them. They can preserve order. Great for navigating **Trees**. **Con's**: Searching is linear. You cannot access anything else besides the top.
* Used in **text editors** to undo changes, in **compiler syntax** to match brackets and braces, used in keeping track of previous function calls in **Recursion**, and also used in DFS (Depth First Search) on **Graphs**.
* **Time Complexity**:
    * Access: O(1)
    * Search: O(n)
    * Insert: O(1)
    * Remove: O(1)
    


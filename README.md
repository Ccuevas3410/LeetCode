
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

### Queue ###   

* A **Stack** is a one ended linear data structure that models a real world queue and only has 2 main operations, _queue()_ (Inputting) and _dequeue()_ (Removing).
* It is a **FIFO (First in, first out)** data structure. **Pro's:** **Cons:**
* Used in **real life queues models**, it can be used to keep track of most **recent elements**, also used in BFS (Breath First Search) on **Graphs**.
* **Time Complexity**:
    * Enqueue: O(1)
    * Dequeue: O(n)
    * Peeking: O(1)
    * Contains: O(n)
    * Removal : O(n)
    * Is Empty: O(n)














## Object-Oriented Progamming Concepts (Or as I like to remember them, "AEIP" ) ##

### Abstraction ###
* **Abstraction** means, showcasing only the required things to the outside world while hiding the details.The concept of abstraction focuses on what an object does, instated of how an object is represented or “how it works.” Thus, data abstraction is often used for managing large and complex programs. **Example:** Lets use a HumanBeing class that can talk, walk, hear, eat, but the details of the muscles mechanism and their connections to the brain are hidden from the outside world.

### Encapsulation ###
* **Encapsulation** means that we want to hide unnecessary details from the user. 
* **Example:** When we call from our mobile phone, we select the number and press call button. But the entire process of calling or what happens from the moment we press or touch the call button to the moment we start having a phone conversation is hidden from us.

### Inheritance ###
* **Inheritance** is a feature of object-oriented programming that allows code reusability when a class includes property of another class.
* **Example:** Considering our HumanBeing class, which has properties like hands, legs, eyes, mouth, etc, and functions like walk, talk, eat, see, etc. Man and Woman are also classes, but most of the properties and functions are included in our HumanBeing class. Hence, they can inherit these same methods from class the HumanBeing class.

### Polymorphism ###
* **Polymorphism** is a concept, which allows us to redefine the way something works, by either changing how it is done or by changing the parts used to get it done. This can be done in two ways, overloading and overriding. 
* **Example:** If we walk using our hands, and not legs, here we will change the parts used to perform something. Hence this is called **Overloading**. And if there is a defined way of walking, but I wish to walk differently, but using my legs, like everyone else. Then I can walk like I want, this will be called as **Overriding**.


## System Design - Basic Concepts ##

### Load Balancer ###
* **Load Balancers** help to distribute traffic to many different web servers in order to help with latency, scalability and reliability. Load balancing techniques can optimise the response time for each task, avoiding unevenly overloading compute nodes while other compute nodes are left idle.
* **Example:**  When a user access your website, instead of hitting a single host/web server , you can put a load balancer in that request and it would route the client request to different web servers in order to improve the task or avoid failing the task because that single host is down.

![Alt text](imgs/loadBalancer.png?raw=true "LoadBalancer")

### Caching ###
* Most of the times, you will be querying your database very often and fast. However, your main database will not be able to meet this demand. This is where a **cache** comes in, it is a high-speed data storage layer which stores a subset of data,  so that future requests for that data are served up faster than is possible by accessing the data’s primary storage location. Caching allows you to efficiently reuse previously retrieved or computed data.
* **Example:** When first going into a website, it might take a bit longer to load. But once you load it for the first time, subsequent entries will be faster than the first time, because certain parts of the website will be cached in your computer, and so they will be faster to obtain the next time.
* Different Caching systems: **Memcached**, **Redis**, **CDN Servers (Content Delivery Network)**.

![Alt text](imgs/caching.png?raw=true "Caching")


### Database Sharding ##
* A company like **Twitter** gets their database hammered with new data every second. Splitting your database into different master databases
* Different ways Sharding: 
    * **Vertical Sharding:** Take each table, and you put it into a new machine.
    * **Horizontal Sharding:** Take a single table, and you split it into several machines.

![Alt text](imgs/sharding.png?raw=true "Sharding")

<p align="center">
System Design example
</p>

![Alt text](imgs/systemDesign.png?raw=true "SystemDesign")

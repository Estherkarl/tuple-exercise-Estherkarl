#Task1

my_tuple = (1, "two", 3.0, [4, 5, 6]) 

print(my_tuple[0])  
print(my_tuple[1]) 
print(my_tuple[3]) 

#Task 2

tuple1 = (1, 2, 3) 
tuple2 = (4, 5, 6) 
concatenated_tuple = tuple1 + tuple2 
print(concatenated_tuple)  

tuple3 = (1, 2, 3) 
repeat = tuple3 * 3 
print(repeat) 

#Task 3

my_tuple = (1, 2, 3) 
print(2 in my_tuple)  
print(4 in my_tuple) 


len_tuple = (1, 2, 3) 
print(len(len_tuple)) 

#Task 4
new_tuple = (1, 2, 3)
a, b, c = new_tuple
print(a)  
print(b)  
print(c)  

my_tuple = (1, 2, 3)
new_tuple = (a, b, c) 
print(new_tuple)  

#Task 5: 


my_tuple = (1, 2, 3)
my_list = list(my_tuple) 
print(my_list) 
my_list = [1, 2, 3] 
my_tuple = tuple(my_list)
print(my_tuple) 

'''Task 6: Difference, Intersection, Symmetric Difference
The methods difference(), intersection(), and symmetric_difference() are set operations that can be performed on tuples or sets.

- difference() returns a new tuple or set that contains the elements that are in the first tuple or set but not in the second tuple or set.
- intersection() returns a new tuple or set that contains the elements that are common to both tuples or sets.
- symmetric_difference() returns a new tuple or set that contains the elements that are in either of the tuples or sets, but not in both.

The methods difference_update(), intersection_update(), and symmetric_difference_update() are similar to the above methods, but they modify the original tuple or set instead of returning a new one.

These methods are different from each other in terms of the elements they include in the result and whether they modify the original tuple or set.'''
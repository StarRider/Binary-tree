# Binary-tree
This is a small work on learning the formation of binary tree using python.

<h3>The Node Class</h3>
<p>This is the class which has 3 parts declared in it's __init__ funciton.</p>

```python
def __init__(self,num = None):
        self.data = num
        self.left = None
        self.right = None
```        
    
<p>In this class I have two functions for insertion one of them is bst_insert funciton.<br>Which Inserts the 
data as in binary search search tree.<br> I have explained whats' happenning at each line within the code itself.</p>

```python
 def bst_insert(self,data):
        if self.data is not None:
            print('Root data is ',self.data)
            if data < self.data:
                print('%d is smaller than root data %d'%(data,self.data))
                if self.left is None:
                    print('The left is None so self.left = Node(%d)'%data)
                    self.left = Node(data)
                else:
                    print('The left side is not None. Going to the left Node')
                    self.left.bst_insert(data)
            else:
                print('%d is greater than root data %d'%(data,self.data))
                if self.right is None:
                    print('The right is None so self.right = Node(%d)'%data)
                    self.right = Node(data)
                else:
                    print('The right side is not None. Going to the right Node')
                    self.right.bst_insert(data)
        else:
            print('Data is None but it is a Node which is visited!')
            self.data = data
```
<p> Rest of the functions like printTree and normal insertion are also in there have a look at the code and <br> enjoy it's detail.</p>
<p>Stay Tuned For More<br>StarRider Signing out!</p>

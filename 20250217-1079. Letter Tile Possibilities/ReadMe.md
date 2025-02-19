# discussion of iterative and recursive algorithms

Considering the nature difference between recursion and iterative way, although theoretically they are interchangeable, in practice, it's complicated, because:
1. the flow control and procedure end condition of the iterative algorithm is straightforward, no complex flow break and resume. If a complex recousive function call break, it can be challenge to manage the status and backtracking info/variables.
2. the recoursion algoirthm has can hanle complex break (good hanle complex exploring with natually backtracking), how every, flow control and procedure end condition may not intuitive. 

Both algorithm have their own advantage and disadvantage. Understanding these features helps to choose the right one for a specific problem.


## Challenge of replacing a recursive algoirthms with a loop. 

"The main challenge is to replace the recursion with a loop. Recursion implicitly uses the call stack to track the state. To do this iteratively, I'll need to manage the stack manually. Each stack element should keep track of the current state of groupedTiles and possibly the current position in the loop over the tiles to avoid revisiting previous tiles and ensure all combinations are counted correctly." -- deepSeek

Recoursive algorithm allow break and resume logic flow, which makes the end condition and logic complex, but flexible and intuitive for some problems. 

Due to flexibility and backtracking local variable feature, some recursive algorithm can be extremely challenge to rewrite use loop.

## Replace a loop algoirthms with recursion

It's not so complicated to do it. Here is typical way to. 

Iterative:
```js
function iterative(n)
    x = xbase
    for i = base+1 to n
        x = f(i, x)
    return x
```
Recoursive:
```js
function recursive(n)
    if n == base
        return xbase
    else
        return f(n, recursive(n-1))
```

As long convert the termination condition properly, there should be OK. 
Actually, functional programing use recousive to replace loop almost everywhere as functional languages prefer/enforce immutability.

## Pros and Cons

**Recoursive algorithm**:
- Pros
  - flexible flow control
  - implicitly state tracking
  - Easy backtracking 
  - break large problem to smaller instances of the same problem
- Cons
  - complicated termination condition
  - flexibility of flow control can result in complicite of logic, which is not intuitive in many cases. 
  - stack overflow
  - Not efficient

**Iterative algorithms**
- Pros
  - termination condition is straightforward
  - flow control is simple
  - hanle most problem intuitively
  - Efficient
- Cons
  - Handling backtracking can be challenging and complicated

For these algoirthms without requrements of backtracking state/varibles or clomplicated flow control requirement, two types of algoirthms should be interchangable without big effort.   



## Some cases: trail recursion (No need backtracking)


in the case of tail recursion (No need backtracking), the *return fun(update parameter)* is equivalent to - *update parameter and continue*.  
The return without recursion is equivalent to break the loop and return the result after the loop, or return directly from the loop. 

```python
# implement recursive and interative algorithm for 1+2+3...n
def recursive(n:int, total:int=0) -> int:
    if(n==1):
        return total+1
    if(n%3 == 0):
      return recursive(n-3, total + n)
    else:
      return recursive(n-1, total + n)

def iterative(n:int, total:int=0) -> int:
    while True:
        if(n==1):
            return total+1
        n, total = n-1, total + n

def iterative2(n:int, total:int=0) -> int:
    while True:
        if(n==1):
            total = total+1
            break
        n, total = n-1, total + n
        continue # can be ignored at the end of each loop
    return total

print(recursive(1000)) # will overflow because python doesn't have tail recursion optimization
# print(iterative(1000))

```


```python

# in the case of tail recursion, the return fun(update parameter) is equivalent to - update parameter and continue.  

def recursive(n:int, total:int=0) -> int:
    if(n==1):
        return total+1
    elif(n<1):
        return total
    if(n%3 == 0):
        return recursive(n-2, total + n)
    return recursive(n-1, total + n)

def iterative(n:int, total:int=0) -> int:
    while True:
        if(n==1):
            return total+1
        if(n%3 == 0):
            n, total = n-2, total + n
            continue
        n, total = n-1, total + n
        continue # option at the end of loop

# 10 + 9 + 7 + 6 + 4 + 3 + 1 -> 40
print(recursive(10)) # will overflow because python doesn't have tail recursion optimization
print(iterative(10))
```

## The case requiring backtracking

To rewrite the recursion (needing backtracking) with a loop, the key point is
1. use a stack to manage backtracking call, parameters and localvariables
2. Manually pop the stack when start a loop
3. manually recover the parameters and localvariables from popped data
4. Manually push the stack when minic call to a function
5. Manually control the flow after function by using a codeSession variable and split the code into execution sessions. 

**Clean code:**

```python
def recursive(n:int) -> int:
    if(n==1):
        return 1
    
    rn = recursive(n-1)
    # backtracking
    rn = rn + n # update rn
    return rn

def iterative(n:int) -> int:
    stack = [n]
    codeSession = 0
    while len(stack)>0:
        n = stack.pop()
        if codeSession == 0:
            if(n==1):
                rn = 1
                codeSession = 1
            else:
                stack.append(n)
                stack.append(n-1)
                continue
        
        elif codeSession == 1: 
            # backtracking
            rn = rn + n  
            continue
    return rn
            
print(recursive(10)) 
print(iterative(10))
```


**Code with comment in detail.**
```python
def recursive(n:int) -> int:
    
    print(f'before call: n={n}')
    if(n==1):
        return 1
    
    # return recursive(n-1) +n
    # the return can be break down in to update return value every frame
    rn = recursive(n-1)
    rn = rn + n # update rn
    print(f'After call: n={n}')
    return rn

def iterative(n:int) -> int:
    stack = [n]
    codeSession = 0
    while len(stack)>0:
        n = stack.pop()
        if codeSession == 0:
            print(f'before call: n={n}')
            if(n==1):
                rn = 1
                codeSession = 1
            else:
                stack.append(n)
                stack.append(n-1)
                continue
        
        elif codeSession == 1: # backtracking after break
            rn = rn + n  # update rn every iteration after backtracking           
            print(f'After call: n={n}')
            continue
    return rn
            

print(recursive(10))
print(iterative(10))

```

People may manage the stack pop() at end of each loop when no new calls. This would avoid pop() and push() again into stack when mimicking recursion call. However, pop() at end of each loop logically clear but people can forget pop() at the end of loop. 
```python
def iterative(n:int) -> int:
    stack = [n]
    codeSession = 0
    while len(stack)>0:
        # recover the state
        n = stack[-1]
        if codeSession == 0:
            if(n==1):
                rn = 1
                codeSession = 1
                stack.pop()
                continue
            else:
                stack.append(n-1)
                continue
        
        elif codeSession == 1: 
            # backtracking
            rn = rn + n  
            stack.pop()
            continue
    return rn
            
print(iterative(10))
```
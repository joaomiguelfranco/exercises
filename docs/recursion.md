# Recursion

A recursive call is when the function calls itself and the recursive call is added to the Stack.

```commandline
def factorial(n):
    if n == 1 : return 1
    return n * factorial(n-1)
```
## How does this work?
In every recursive call we add the previous function, its arguments and local variables to the stack, as shown below:
1. `factorial(4)`
2. `factorial(3)` `stack = [factorial(4)]`
3. `factorial(2)` `stack = [factorial(3), factorial(4)]`
4. `factorial(1)` `stack = [factorial(2), factorial(3), factorial(4)]`
5. `1 * factorial(2)` `stack = [factorial(3), factorial(4)]`
6. `1 * 2 * factorial(3)` `stack = [factorial(4)]`
7. `1 * 2 * 3 * factorial(4)` `stack = []`
8. `1 * 2 * 3 * 4` `stack = []`
9. `24`

## When can it be an issue?

- **Stack space**: In some programming languages, the maximum size of the call stack is much less than the space available in the heap, and recursive algorithms tend to require more stack space than iterative algorithms.

- **Performance issues**: due to the overhead required to manage the stack and the relative slowness of function calls.


## Recursion Vs. Iteration
In imperative programming, iteration is preferred, particularly for simple recursion, as it avoids the overhead of function calls and call stack management, but recursion is generally used for multiple recursion (e.g., Depth-First Search algorithm).

In functional languages recursion is preferred, with tail recursion optimization leading to little overhead. Implementing an algorithm using iteration may not be easily achievable.


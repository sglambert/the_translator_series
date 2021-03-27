
def transpose_matrix(m):
    """
    Will transpose a matrix (list of lists)
    e.g.
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    will return matrixT = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    return map(list, zip(*m))


convert this python function (above) into a function in C

A typical function in C looks like this:

return_type function_name( parameter list ) {
   body of the function
}

C does not allow you to return an entire array as an argument to a function (bummer!)
However, you can return a pointer to an array by specifying the array's name without an index.

int arr[5] = { 1, 2, 3, 4, 5 }; 
int *ptr = arr;


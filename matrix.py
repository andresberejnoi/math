#Carlos Andres Berejnoi Bejarano
#Project started on 4/22/2015 at 4:38 PM

#An attempt to write a class with functions that apply to matrices.
# It is based on Linear Algebra concepts.
#==================================================================
#import tabulate
#import padnums                 #not to be used yet. It is a module taken from the internet. Helps with printing tables in a nice way. I have no idea how to use it
import copy
import random
#import operator                 #provides the basic operation functions. It is going to be useful when converting strings into an operator
#oper = {'+': operator.add,  '-':operator.sub,  '*':operator.mul,
#        '/':operator.truediv, '//':operator.floordiv}

def randFloatMatrix(numRows, numCol, bottom_range = 0.3, top_range= 0.8):
        '''Creates a linear array of randomly generated numbers in the range of 0.3 to 0.8.
        The array has a format that works with the matrix class.'''
        matrix = []
        rep = numRows*numCol
        for i in range(rep):
            matrix.append(random.uniform(bottom_range,top_range))         #Assigns random weights to each connection
        M = Matrix(numRows, numCol, matrix)
        return M


def linear_array(Lnested):
    '''Takes a list of lists as input and returns a linear array of that list.'''
    linear = []
    for row in Lnested:
        for item in row:
            linear.append(item)
    return linear

class MatrixError(Exception):
    '''An exception object that can be raised when there is a problem with the matrix'''
    def __init__(self, message = 'Invalid interaction with the Matrix class'):
        self.message = message
    def __str__(self):
        return str(self.message)

    def __repr__(self):
        return str(self)


class Matrix(object):
    '''A matrix object has several of the properties that we can apply to
    matrices.'''
    def __init__(self, m=2, n=2, entries = []):
        '''Initializes a Matrix object.
        self.row_num: an integer; the number of rows in the matrix.
        self.col_num: an integer; the number of rows in the matrix.
        self.matrix: a Python list; the internal representation of a matrix as nested lists.'''
        self.row_num = m
        self.col_num = n
        self.matrix = None
        self._populate_matrix(entries)              #an empty matrix of order mxn is created

    def _populate_matrix(self, entries):
        '''Implements a matrix as nested lists. By defaul, the matrix is
        the zero matrix'''
        self.matrix = []
        using = entries
        if entries == []:
            self.matrix = [[0 for f in range(self.col_num)] for i in range(self.row_num)]
        else:
            for i in range(self.row_num):
                self.matrix.append([])
                for j in range(self.col_num):
                    self.matrix[i].append(using[j])
                using = using[self.col_num:]
# Overloading
    def __str__(self):
        '''Creates a representation of the matrix so that is easier to read.'''
        output= ''
        for i in range(self.row_num):
            for j in range(self.col_num):
                output += str(self.matrix[i][j]) + '\t'
            output += '\n'
        return output

    def __repr__(self):
        ''''''
        return str(self)

    def __copy__(self):
        '''A copy of the Matrix object. It is by default a deep copy.'''
        new_list = linear_array(self.matrix)
        M = Matrix(self.row_num, self.col_num, new_list)
        return M

    def __deepcopy__(self):
        '''Similar to copy'''
        return copy(self)
    
    def __len__(self):
        return self.row_num

    def __getitem__(self, key):
        M =  Matrix(1, len(self.get_row(key)), self.get_row(key))
        return M



    def __add__(self, to_add):
        result = []
        if type(to_add) == Matrix:
            if not (self.get_order() == to_add.get_order()):
                raise MatrixError('The order of the two matrices do not match')
            x = self._one_dimensional()
            y = to_add._one_dimensional()
            for i in range(len(x)):
                result.append(x[i] + y[i])
        else:
            result = [item + to_add for item in linear_array(self.matrix)]

        New = Matrix(self.row_num, self.col_num, result)
        return New

    def __mul__(self, to_mult):
        result = []
        if type(to_mult) == Matrix:
            assert(self.get_order()[1] == to_mult.get_order()[0])
            newRow_size = self.row_num
            newCol_size = to_mult.get_order()[1]
            for i in range(self.row_num):
                lin = self.get_row(i)
                for j in range(to_mult.col_num):
                    lin2 = to_mult.get_col(j)
                    result.append(sum([lin[g] * lin2[g] for g in range(self.row_num)]))
            return Matrix(newRow_size, newCol_size, result)
        else:
            result = [item * to_mult for item in linear_array(self.matrix)]
            New = Matrix(self.row_num, self.col_num, result)
        return New
#===========================================================================
    #Funtions that provide internal information
    def is_square(self):
        '''Return True is the matrix is a square matrix (self.col_num = self.row_num).
        Otherwise, return False'''
        return self.col_num == self.row_num

    def row_len(self):
        '''Returns the number if rows in the matrix'''
        return self.row_num

    def col_len(self):
        '''Returns the number of columns in the matrix.'''
        return self.col_num

    def invertible(self):
        '''Return True if the matrix is invertible, otherwise return False'''
        if self.det() == 0:
            return False
        return True

    #Useful Functions to use somewhere else
    def _cal_iden(self):
        '''Calculates the identity matrix for self.matrix and returns
        a list with the entries in a format that the class accepts.'''
        identity = []
        for i in range(self.row_num):
            for j in range(self.col_num):
                if j == i:
                    identity.append(1)
                else:
                    identity.append(0)
        return identity

    def _one_dimensional(self):
        '''Returns a list of all the items in self.matrix'''
        listed = []
        for row in self.matrix:
            for item in row:
                listed.append(item)
        return listed

#Especial Functions

    #Getters
    def get_order(self):
        '''Returns a tuple containing the order of the matrix.
        This means that a matrix of size MxN will result in a tuple (M,N)'''
        return (self.row_num, self.col_num)
    def get_item(self, row, col = 0):
        '''Returns the item at position self.matrix[row][col]'''
        return self.matrix[row][col]
    def get_row(self, index):
        '''Returns the row at position index, as a list.'''
        return self.matrix[index]

    def get_col(self, index):
        '''Returns the row at position index as a one dimensional list.'''
        return [self.matrix[i][index] for i in range(self.row_num)]

    def get_iden(self):
        '''Returns the identity matrix of self.matrix'''
        return Matrix(self.row_num, self.col_num, self._cal_iden())

    def _get_internal_matrix(self):
        return self.matrix

    #Setters;
    def set_item(self, row, col, val):
        '''Changes the value of self.matrix[row][col] to val'''
        self.matrix[row][col] = val

    def set_row(self, row, entries):
        '''Sets self.matrix[row] to entries'''
        if len(entries) == self.col_num:
            self.matrix[row] = entries                  #NEEDS A FUNCTION TO MAKE SURE THAT THE INPUT IS APPROPIATE
        else:
            raise IndexError("The row you are trying to introduce does not have the correct length.")

    #Matrix operations
    def transpose(self):
        '''Returns the transpose of self.matrix'''
        M_transpose = [self.get_col(i) for i in range(self.col_num)]

        M = Matrix(self.col_num, self.row_num, linear_array(M_transpose))    #M is a Matrix object
        return M

    def row_oper(self, source, arg = 1, destination = None):
        '''Allows row operations to be performed on the matrix.
        source: type == int; the row number that will be used to modify another one.
        arg: type == number; The argument to apply to the source matrix to modify the destination
        destination: type == int; The row that will be changed after the operation is performed.
        op: type == str; a symbol of a math operation, i.e. '+', '-','*','/', '//'.
        For now, it changes the matrix in-place. It might be changed later to return a new matrix.'''
        assert(arg != 0)                #arg can never be zero
        M = copy.copy(self)
        row1 = M.get_row(source)

        if destination == None:
            for i in range(len(row1)):
                row1[i] = row1[i]*arg
        else:
            row2 = M.get_row(destination)
            for i in range(len(row1)):
                row2[i] = row1[i]*arg + row2[i]
        return M

    def det(self):
        '''Returns the determinant of the matrix.'''
        deter = 0
        if self.get_order()==(2, 2):
            deter = self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]

        return deter

#Test objects
def testing():
    x = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = Matrix(3, 3, [23, 4, 5, 6, 7, 8, 10, 11, 15])
    z = Matrix(3, 1, [3, 1, 9])
    w = Matrix(2, 2, [1, 2, 3, 4])
    x * y
    fMatrix = randFloatMatrix(4,5,0.4,0.5)





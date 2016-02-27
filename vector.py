import math


class Vector:
    '''A vector class. Creates an instance of a vector 
    object that works under the properties of vectors.'''
    
    def __init__(self, components=[]):
        '''Initializes an instance of the Vector class.
        components: a list of components coordinates. It starts with x, y, z, ... and so on.'''
  #      self.mag = mag
        self.compo = components
    
        
    def magnitude(self):
        '''Returns the magnitude of the vector, stored in self.magnitude.
        It uses the formula |A| = sqrt(A1^2 + A2^2 + ... + An^2) to calculate it.'''
        mag =sum([(comp**2) for comp in self.compo])
        
        
    def dot(self, vector2):
        '''Computes the dot product for two vetors'''
        if len(self) != len(vector2):
            raise ValueError ("Cannot compute the dot product of vectors of different dimensions")
#        for i in range(min(len(self), len(vector2))):
        new_vec = []
        for v1,v2 in zip(self.compo, vector2.compo):
            new_vec.append(v1*v2)
        
        return sum(new_vec)
            
    
    def __len__(self):
        return len(self.compo)
        
    def __eq__(self, other):
        if self.compo == other.compo:
            return True
        return False
    
    def __getitem__(self, key):
        return self.compo[key]
        
    def __iter__(self):
        for component in self.compo:
            yield component
    
    def __neg__(self):
        new_vec = [-1*comp for comp in self.compo]
        return Vector(new_vec)
    
    def __add__(self, vec_2):
        if len(self) != len(vec_2):
            raise ValueError ("Cannot add two vectors in different dimensions.")
        new_vec = []
        for i in range(len(self)):
            new_vec.append((self.compo[i] + vec_2.compo[i]))
        
        return Vector(new_vec)
    
    def __sub__(self, to_sub):
        return self.__add__(-to_sub)
    
    def __mul__(self, to_mult):
        if type(to_mult)==int or type(to_mult)==float:
            new_vec = []
            for item in self.compo:
                new_vec.append(item*to_mult)
            return Vector(new_vec)
        elif type(to_mult)==Vector:
            assert(len(self)==len(to_mult))
            new_vec = [self[i]*to_mult[i] for i in range(len(self))]
            return Vector(new_vec)
            
        
    def __str__(self):
        return str(tuple(self.compo))
#        rep = '('
#        for comp in self.compo:
#            rep += str(comp) + ', '
#        
#        rep += ')'
#        return rep
#            
            
    def __repr__(self):
        return str(self)
            
            
            
            

# Implementation of B+-tree functionality.

from index import *

# You should implement all of the static functions declared
# in the ImplementMe class and submit this (and only this!) file.
class ImplementMe:

    # Returns a B+-tree obtained by inserting a key into a pre-existing
    # B+-tree index if the key is not already there. If it already exists,
    # the return value is equivalent to the original, input tree.
    #
    # Complexity: Guaranteed to be asymptotically linear in the height of the tree
    # Because the tree is balanced, it is also asymptotically logarithmic in the
    # number of keys that already exist in the index.
    @staticmethod
    def InsertIntoIndex( index, key ):
        if index.nodes != []:
            upper = index.nodes[0].keys.keys[1]
            lower = index.nodes[0].keys.keys[0]
            r = range(lower, upper)
        
        if index.nodes == []:
            index.nodes.append(Node(\
                KeySet((key, -1)),\
                PointerSet((0,0,0))))
            return index
        

        elif index.nodes[0].keys.keys[0] == key or index.nodes[0].keys.keys[1] == key:
            return index
        elif index.nodes[0].keys.keys[1] == -1 and key > index.nodes[0].keys.keys[0]:
            index.nodes[0].keys = KeySet((index.nodes[0].keys.keys[0],key))
            return index
        elif index.nodes[0].keys.keys[1] == -1 and key < index.nodes[0].keys.keys[0]:
            
            index.nodes[0].keys = KeySet((key,index.nodes[0].keys.keys[0]))
            
            return index
        elif key < index.nodes[0].keys.keys[0] and len(index.nodes) == 1:
            
            index.nodes[0].keys = KeySet((index.nodes[0].keys.keys[0],-1))
            index.nodes[0].pointers = PointerSet((1,2,0))
        
            index.nodes.append(Node(\
                KeySet((key, -1)),\
                PointerSet((0,0,2))))
            index.nodes.append(Node(\
                KeySet((index.nodes[0].keys.keys[0], upper)),\
                PointerSet((0,0,0))))
            index.nodes.append(Node(\
                KeySet((-1,-1)),\
                PointerSet((0,0,0))))
            
            return index
        elif key > index.nodes[0].keys.keys[1] and len(index.nodes) == 1:
            first = index.nodes[0].keys.keys[0]
            last = index.nodes[0].keys.keys[1]
            index.nodes[0].keys = KeySet((index.nodes[0].keys.keys[1],-1))
            index.nodes[0].pointers = PointerSet((1,2,0))
            index.nodes.append(Node(\
                KeySet((first, -1)),\
                PointerSet((0,0,2))))
            index.nodes.append(Node(\
                KeySet((last, key)),\
                PointerSet((0,0,0))))
            index.nodes.append(Node(\
                KeySet((-1,-1)),\
                PointerSet((0,0,0))))
            
            return index
        elif key in r and len(index.nodes) == 1:
            first = index.nodes[0].keys.keys[0]
            last = index.nodes[0].keys.keys[1]
            index.nodes[0].keys = KeySet((key,-1))
            index.nodes[0].pointers = PointerSet((1,2,0))
            index.nodes.append(Node(\
                KeySet((first, -1)),\
                PointerSet((0,0,2))))
            index.nodes.append(Node(\
                KeySet((key, last)),\
                PointerSet((0,0,0))))
            index.nodes.append(Node(\
                KeySet((-1,-1)),\
                PointerSet((0,0,0))))
            
            return index
        elif key in r :
            if key > index.nodes[2].keys.keys[0] :
                index.nodes[2].keys = KeySet((index.nodes[2].keys.keys[0],key))
                
                return index
            else:
                index.nodes[2].keys = KeySet((key,index.nodes[2].keys.keys[0]))
                
                return index
        elif key < index.nodes[0].keys.keys[0] :##
            if key > index.nodes[1].keys.keys[0] and index.nodes[1].keys.keys[1] == -1:
                index.nodes[1].keys = KeySet((index.nodes[1].keys.keys[0],key))
                
                return index
            elif key < index.nodes[1].keys.keys[0] and index.nodes[1].keys.keys[1] == -1:
                index.nodes[1].keys = KeySet((key,index.nodes[1].keys.keys[0]))
                return index
            else:
                first = index.nodes[0].keys.keys[0]
                second = index.nodes[0].keys.keys[1]
                third = index.nodes[1].keys.keys[0]
                fourth = index.nodes[3].keys.keys[1]
                index.nodes[0].keys = KeySet((lower,-1))
                index.nodes[0].pointers = PointerSet((1,2,0))
                index.nodes[1].keys = KeySet((key,-1))
                index.nodes[1].pointers = PointerSet((4,5,0))
                index.nodes[2].keys = KeySet((upper,-1))
                index.nodes[2].pointers = PointerSet((7,8,0))

                index.nodes[3].keys = KeySet((-1,-1))
                index.nodes[3].pointers = PointerSet((0,0,0))
                index.nodes.append(Node(\
                KeySet((third, -1)),\
                PointerSet((0,0,5))))
                index.nodes.append(Node(\
                KeySet((lower, -1)),\
                PointerSet((0,0,7))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((key, )),\
                PointerSet((0,0,8))))
                index.nodes.append(Node(\
                KeySet((key, fourth)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                
                return index
        
        elif key > index.nodes[0].keys.keys[1] and index.nodes[3].keys.keys[1] != -1 :
            if key > index.nodes[3].keys.keys[0] and key < index.nodes[3].keys.keys[1]:
                first = index.nodes[0].keys.keys[0]
                second = index.nodes[0].keys.keys[1]
                third = index.nodes[1].keys.keys[0]
                fourth = index.nodes[3].keys.keys[1]
                index.nodes[0].keys = KeySet((upper,-1))
                index.nodes[0].pointers = PointerSet((1,2,0))
                index.nodes[1].keys = KeySet((lower,-1))
                index.nodes[1].pointers = PointerSet((4,5,0))
                index.nodes[2].keys = KeySet((key,-1))
                index.nodes[2].pointers = PointerSet((7,8,0))

                index.nodes[3].keys = KeySet((-1,-1))
                index.nodes[3].pointers = PointerSet((0,0,0))
                index.nodes.append(Node(\
                KeySet((third, -1)),\
                PointerSet((0,0,5))))
                index.nodes.append(Node(\
                KeySet((lower, -1)),\
                PointerSet((0,0,7))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((upper, -1)),\
                PointerSet((0,0,8))))
                index.nodes.append(Node(\
                KeySet((key, fourth)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                
                return index
            else:
                first = index.nodes[0].keys.keys[0]
                second = index.nodes[0].keys.keys[1]
                third = index.nodes[1].keys.keys[0]
                fourth = index.nodes[3].keys.keys[1]
                index.nodes[0].keys = KeySet((upper,-1))
                index.nodes[0].pointers = PointerSet((1,2,0))
                index.nodes[1].keys = KeySet((lower,-1))
                index.nodes[1].pointers = PointerSet((4,5,0))
                index.nodes[2].keys = KeySet((fourth,-1))
                index.nodes[2].pointers = PointerSet((7,8,0))

                index.nodes[3].keys = KeySet((-1,-1))
                index.nodes[3].pointers = PointerSet((0,0,0))
                index.nodes.append(Node(\
                KeySet((third, -1)),\
                PointerSet((0,0,5))))
                index.nodes.append(Node(\
                KeySet((lower, -1)),\
                PointerSet((0,0,7))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((upper, -1)),\
                PointerSet((0,0,8))))
                index.nodes.append(Node(\
                KeySet(( fourth, key)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                index.nodes.append(Node(\
                KeySet((-1, -1)),\
                PointerSet((0,0,0))))
                
                
                return index
        elif key > index.nodes[0].keys.keys[0]  :
            if key > index.nodes[3].keys.keys[0] :
                index.nodes[3].keys = KeySet((index.nodes[3].keys.keys[0],key))
                
                
                return index
            else:
                index.nodes[3].keys = KeySet((key,index.nodes[3].keys.keys[0]))
                
                return index
        
        else:
            return index
       


            
        
    # Returns a boolean that indicates whether a given key
    # is found among the leaves of a B+-tree index.
    #
    # Complexity: Guaranteed not to touch more nodes than the
    # height of the tree
    @staticmethod
    def LookupKeyInIndex( index, key ):
        length = len(index.nodes)
        #print(index.nodes[0].pointers.pointers[2])
        if len(index.nodes) == 1 and index.nodes[0].keys.keys[0] != key and index.nodes[0].keys.keys[1] != key:
            return False
        
        elif len(index.nodes) == 1 and index.nodes[0].keys.keys[0] == key or index.nodes[0].keys.keys[1] == key:
            return True
        elif index.nodes[0].keys.keys[0] == key or index.nodes[0].keys.keys[1] == key:
            return True
        elif len(index.nodes) > 1 and key >= index.nodes[0].keys.keys[1] :
            if index.nodes[3].keys.keys[0] == key or index.nodes[3].keys.keys[1] == key:
                return True
            else:
                return False
        elif len(index.nodes) > 1 and key < index.nodes[0].keys.keys[0] :
            if index.nodes[1].keys.keys[0] == key or index.nodes[1].keys.keys[1] == key:
                return True
            else:
                return False
        elif len(index.nodes) > 1 and key > index.nodes[0].keys.keys[0] and key < index.nodes[0].keys.keys[1] :
            if index.nodes[2].keys.keys[0] == key or index.nodes[2].keys.keys[1] == key:
                return True
            else:
                return False


    # Returns a list of keys in a B+-tree index within the half-open
    # interval [lower_bound, upper_bound)
    #
    # Complexity: Guaranteed not to touch more nodes than the height
    # of the tree and the number of leaves overlapping the interval.
    @staticmethod
    def RangeSearchInIndex( index, lower_bound, upper_bound ):

        r = range(lower_bound, upper_bound)
        store = []
        x = len(index.nodes) 
        
        if lower_bound == upper_bound:
            return store
        else:
           
            while True:
                if lower_bound >= index.nodes[0].keys.keys[1] :
                    if index.nodes[3].keys.keys[0] in r and index.nodes[3].keys.keys[1] in r:
                        store.append(index.nodes[3].keys.keys[0])
                        store.append(index.nodes[3].keys.keys[1])
                        break
                    elif index.nodes[3].keys.keys[0] in r:
                        store.append(index.nodes[3].keys.keys[0])
                        break
                    elif index.nodes[3].keys.keys[1] in r:
                        store.append(index.nodes[3].keys.keys[1])
                        break
                elif lower_bound < index.nodes[0].keys.keys[0] :
                    if lower_bound <= index.nodes[1].keys.keys[0] and index.nodes[1].keys.keys[0] in r and index.nodes[1].pointers.pointers[2] == 2:
                        store.append(index.nodes[1].keys.keys[0])
                        if index.nodes[2].keys.keys[0] not in r and index.nodes[2].pointers.pointers[2] == 3:
                            break
                        elif index.nodes[2].keys.keys[0] in r and index.nodes[2].pointers.pointers[2] == 3:
                            store.append(index.nodes[2].keys.keys[0])
                            if index.nodes[3].keys.keys[0] in r and index.nodes[3].keys.keys[1] in r:
                                store.append(index.nodes[3].keys.keys[0])
                                store.append(index.nodes[3].keys.keys[1])
                                break
                elif index.nodes[0].keys.keys[0] in r :
                    
                    if index.nodes[2].keys.keys[0] in r :
                        store.append(index.nodes[2].keys.keys[0])
                        if index.nodes[3].keys.keys[0] in r and index.nodes[3].keys.keys[1] in r:
                            store.append(index.nodes[3].keys.keys[0])
                            store.append(index.nodes[3].keys.keys[1])
                            break
                        
                        elif index.nodes[3].keys.keys[0] in r:
                            store.append(index.nodes[3].keys.keys[0])
                            break
                        
                        elif index.nodes[3].keys.keys[1] in r:
                            store.append(index.nodes[3].keys.keys[1])
                            break
                break


                        
            store = list(dict.fromkeys(store))   
            store.sort()
            return store
                        
        
        

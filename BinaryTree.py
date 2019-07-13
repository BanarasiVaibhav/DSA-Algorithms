class BinaryTree:
  
  class _Node:
    
    __slots__='element','_left','_right'
    
    
    def __init__(self,element,left=None,right=None):
      self._element=element
      self._left=left
      self._right=right


  def __init__(self):
    self.root=None
    self.size=0
  
  def maketree(self,e,left,right):
    self.root=self._Node(e,left._root,right._root)
    self.left=None
    self.right=None
  

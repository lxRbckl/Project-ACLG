# import <


# >


class buildLetter:
   
   
   def __init__(self):
      '''  '''
      
      self._letter = None
      self._company = '[company]'
      self._position = '[position]'
      self._reasoning = '[reasoning]'


   def build(self, ref):
      '''  '''
      
      format = ref['format']
      
      # replace company <
      # replace position <
      # replace reasoning <
      format.replace('')
      
      # >
   
   
   @property
   def letter(self): return self._letter
# import <


# >


class buildLetter:
   
   
   def __init__(self):
      '''  '''
      
      self._letter = None
      self._company = '[company]'
      self._position = '[position]'


   def build(self, ref):
      '''  '''
      
      format = ref['format']
      
      # replace company <
      # replace position <
      format = format.replace(self._company, ref['company'])
      format = format.replace(self._position, ref['position'])
      
      # >

      self._letter = format
   
   
   @property
   def letter(self): return self._letter
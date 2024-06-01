# import <
from lxrbckl.local import (
   
   fileSet, 
   fileGet,
   getProjectPath

)

# >


class manageData:
   
   
   def __init__(self):
      '''  '''
      
      self._datapath = 'source/data'
      self.uploadpath = 'source/assets'
      self.projectpath = getProjectPath()
      
      self.letter = ['format']
      self._modifiable = ['signature', 'format']
      self.details = ['company', 'position', 'signature']
      
      
   @property
   def header(self): return fileGet(f'{self._datapath}/header.json')
   
   
   @property
   def body(self): return fileGet(f'{self._datapath}/body.json')
   
   
   @body.setter
   def body(self, ref): 
      
      if (ref != (body := self.body)): 
      
         for i in self._modifiable: body[i] = ref[i]
         fileSet(body, f'{self._datapath}/body.json')
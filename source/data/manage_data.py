# import <
from lxrbckl.local import (fileSet, fileGet)

# >


class manageData:
   
   
   def __init__(self):
      '''  '''
      
      self._datapath = '/source/data'
      self._uploadpath = '/source/assets'
      
      self._modifiable = ['format']
      
      self.letter = ['format']
      self.details = ['company', 'position']
      
      
   @property
   def header(self): return fileGet(pFile = f'{self._datapath}/header.json')
   
   
   @property
   def body(self): return fileGet(pFile = f'{self._datapath}/body.json')
   
   
   @body.setter
   def body(self, ref): 
      
      if (ref != (body := self.body)): 
      
         for i in self._modifiable: body[i] = ref[i]
         fileSet(pData = body, pFile = f'{self._datapath}/body.json')
         
         
   def upload(self, filename, data):
      '''  '''
      
      pass
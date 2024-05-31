# import <
from dash import Dash
from lxrbckl.local import (fileSet, fileGet)
from dash_bootstrap_components import themes

# >


application = Dash(
   
   name = 'ACLG',
   title = 'ACLG',
   assets_folder = 'source/assets',
   suppress_callback_exceptions = True,
   external_stylesheets = [
      
      themes.GRID,
      themes.BOOTSTRAP
      
   ]
   
)
server = application.server


class data:
   
   
   def __init__(self):
      '''  '''
      
      self._datapath = '/source/data'
      self._uploadpath = '/source/assets'
      
      self._modifiable = ['format']
      self.letter = ['reason', 'format']
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
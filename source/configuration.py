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
      
      self.fpath = '/source/data'
      
      self.form = ['reason', 'letter']
      self.details = ['company', 'position']
      
      
   @property
   def header(self): return fileGet(pFile = f'{self.fpath}/header.json')
   
   
   @property
   def body(self): return fileGet(pFile = f'{self.fpath}/body.json')
   
   
   @body.setter
   def body(self, val): fileSet(pData = val, pFile = f'{self.fpath}/body.json')
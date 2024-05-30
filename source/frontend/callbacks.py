# import <
from .modal import modal

from ..configuration import application
from lxrbckl.local import (fileSet, fileGet)
from dash.dependencies import (Input, Output, State)

# >


class callbacks:
   
   
   def __init__(self):
      '''  '''
      
      self.modal = modal()
      
   
   
   def register(self):
      '''  '''
      
      # self.callbackBuild()
      self.callbackRefresh()
   
   
   # def callbackBuild(self):
   #    '''  '''
      
   #    @application.callback(
         
   #       Output('modalId', 'children'),
   #       Input('buildId', 'n_clicks'),
   #       prevent_initial_call = True
         
   #    )
   #    def func(*args): return (self.modal).modal
   
   
   def callbackRefresh(self):
      '''  '''
      
      body = {
         
         **fileGet(pFile = 'source/data/form.json'),
         **fileGet(pFile = 'source/data/setup.json')
         
      }
      
      @application.callback(
         
         [Output(f'{k}Id', 'value') for k in body.keys()],
         Input('refreshId', 'n_clicks'),
         prevent_initial_call = True
         
      )
      def func(*args): return [v for v in body.values()]
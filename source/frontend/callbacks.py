# import <
from .modal import modal
from ..configuration import data

from ..configuration import application
from lxrbckl.local import (fileSet, fileGet)
from dash.dependencies import (Input, Output, State)

# >


class callbacks:
   
   
   def __init__(self):
      '''  '''
      
      self.data = data()
      self.modal = modal()
   
   
   def register(self):
      '''  '''
      
      self.callbackBuild()
      self.callbackRefresh()
   
   
   def callbackBuild(self):
      '''  '''
      
      pass
      
      # @application.callback(
         
      #    Output('modalId', 'children'),
      #    Input('buildId', 'n_clicks'),
      #    [State('{k}Id')]
      #    prevent_initial_call = True
         
      # )
      # def func(*args): return (self.modal).modal
   
   
   def callbackRefresh(self):
      '''  '''
      
      @application.callback(
         
         [Output(f'{k}Id', 'value') for k in (self.data.body).keys()],
         Input('refreshId', 'n_clicks')
         
      )
      def func(*args): return [v for v in self.data.body.values()]
      
      
   
# import <
from .modal import modal
from ..configuration import data
from ..backend.form_builder import form_builder
from ..backend.pdf_generator import pdf_generator

from ..configuration import application
from dash.dependencies import (Input, Output, State)

# >


class callbacks:
   
   
   def __init__(self):
      '''  '''
      
      self.data = data()
   
   
   def register(self):
      '''  '''
      
      self.callbackBuild()
      self.callbackRefresh()
   
   
   def callbackBuild(self):
      '''  '''
      
      @application.callback(
         
         output = [
            
            Output('modalId', 'is_open'),
            # Output('formId', 'children'),
            # Output('downloadId', 'href'),
            # Output('downloadId', 'download')
         
         ],
         inputs = [Input('buildId', 'n_clicks')],
         state = [State(f'{k}Id', 'value') for k in (self.data.body).keys()],
         prevent_initial_call = True
         
      )
      def func(*args):
         
         print('build', args) # remove
                  
         prop = (self.data.details + self.data.form)
         ref = {k : v for k, v in zip(prop, args[1:])}
         
         
         
         return [True]
   
   
   def callbackRefresh(self):
      '''  '''
      
      @application.callback(
         
         inputs = [Input('refreshId', 'n_clicks')],
         output = [Output(f'{k}Id', 'value') for k in (self.data.body).keys()]
         
      )
      def func(*args): 
         
         print('refresh', args) # remove
         return [v for v in (self.data.body).values()]

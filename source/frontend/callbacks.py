# import <
from ..configuration import data
from ..backend.build_letter import build_letter
from ..backend.generate_pdf import generate_pdf

from ..configuration import application
from dash.dependencies import (Input, Output, State)

# >


class callbacks:
   
   
   def __init__(self):
      '''  '''
      
      self.data = data()
      self.build_letter = build_letter()
      self.generate_pdf = generate_pdf()
   
   
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
         prevent_initial_call = True,
         inputs = [Input('buildId', 'n_clicks')],
         state = [State(f'{k}Id', 'value') for k in (self.data.body).keys()],
         
      )
      def func(*args):
         
         print('build', args) # remove
                  
         props = (self.data.details + self.data.form)
         ref = {k : v for k, v in zip(props, args[1:])}
         
         # save body.format <
         # build & get letter <
         # convert letter to pdf <
         self.data.body = ref
         
         
         # >
         
         return [True]
   
   
   def callbackRefresh(self):
      '''  '''
      
      @application.callback(
         
         inputs = [Input('refreshId', 'n_clicks')],
         output = [Output(f'{k}Id', 'value') for k in (self.data.body).keys()]
         
      )
      def func(*args): return [v for v in (self.data.body).values()]

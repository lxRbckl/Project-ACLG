# import <
from ..data.manage_data import manageData
from ..backend.build_letter import buildLetter
from ..backend.generate_pdf import generatePDF

from ..configuration import application
from dash.dependencies import (Input, Output, State)

# >


class callbacks:
   
   
   def __init__(self):
      '''  '''
      
      self.data = manageData()
      self.buildLetter = buildLetter()
      self.generatePDF = generatePDF()
   
   
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
                           
         props = (self.data.details + self.data.letter)
         ref = {k : v for k, v in zip(props, args[1:])}
         
         # save modifiables <
         # build & get letter <
         # convert to pdf & upload <
         self.data.body = ref
         
         self.buildLetter.build(ref)
         letter = self.buildLetter.letter
         
         # >
         
         return [True]
   
   
   def callbackRefresh(self):
      '''  '''
      
      @application.callback(
         
         inputs = [Input('refreshId', 'n_clicks')],
         output = [Output(f'{k}Id', 'value') for k in (self.data.body).keys()]
         
      )
      def func(*args): return [v for v in (self.data.body).values()]

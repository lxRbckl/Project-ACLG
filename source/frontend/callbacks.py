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
      
      self.manageData = manageData()
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
         state = [State(f'{k}Id', 'value') for k in (self.manageData.body).keys()],
         
      )
      def func(*args):
         
         print('build', args) # remove
                  
         props = (self.manageData.details + self.manageData.letter)
         ref = {k : v for k, v in zip(props, args[1:])}
         
         # save body.format <
         # build & get letter <
         # convert letter to pdf <
         self.manageData.body = ref
         letter = (self.build_letter.build(ref)).letter
         
         # >
         
         return [True]
   
   
   def callbackRefresh(self):
      '''  '''
      
      @application.callback(
         
         inputs = [Input('refreshId', 'n_clicks')],
         output = [Output(f'{k}Id', 'value') for k in (self.manageData.body).keys()]
         
      )
      def func(*args): return [v for v in (self.manageData.body).values()]

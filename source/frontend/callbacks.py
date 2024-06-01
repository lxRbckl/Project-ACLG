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
      
      self.callbackInput()
      self.callbackBuild()
      self.callbackRefresh()
      
      
   def callbackInput(self):
      '''  '''
   
      @application.callback(
         
         output = [Output('buildId', 'disabled')],
         inputs = [Input(f'{k}Id', 'value') for k in (self.data.body).keys()]
         
      )
      def func(*args): return [False if (args.count('') == 0) else True]
   
   
   def callbackBuild(self):
      '''  '''
      
      @application.callback(
         
         output = [
            
            Output('letterId', 'value'),
            Output('modalId', 'is_open'),
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
         
         self.generatePDF.generate(
            
            letter,
            ref['company'],
            ref['signature'],
            f'{self.data.projectpath}{self.data.uploadpath}'
         
         )
         
         # >
         
         return [
            
            letter, 
            True
         
         ]
   
   
   def callbackRefresh(self):
      '''  '''
      
      @application.callback(
         
         inputs = [Input('refreshId', 'n_clicks')],
         output = [Output(f'{k}Id', 'value') for k in (self.data.body).keys()]
         
      )
      def func(*args): return [v for v in (self.data.body).values()]

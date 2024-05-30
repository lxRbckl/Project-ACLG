# import <
from dash import (dcc, html)
from lxrbckl.local import fileGet
import dash_bootstrap_components as dbc

# >


class layout:
   
   
   def __init__(self):
      '''  '''
      
      self.form = fileGet(pFile = 'source/data/form.json')
      self.setup = fileGet(pFile = 'source/data/setup.json')
   
   
   @property
   def layout(self):
      '''  '''
      
      return dbc.Row(
         
         align = 'center',
         justify = 'center',
         style = {
            
            'margin' : 0,
            'padding' : '5%',
            'width' : '100vw',
            'height' : '100vh'
            
         },
         children = dbc.Col(
            
            width = 7,
            children = [
               
               # modal <
               html.Div(
                  
                  id = 'modalId', 
                  children = None
                  
               ),
               
               # >
               
               # header <
               html.H2(
                  
                  className = None,
                  children = 'Project ACLG'
               
               ),
               html.Small(
                  
                  className = None,
                  children = 'Automated Cover Letter Generator'
                  
               ),
               html.Hr(),
               
               # >
               
               # body <
               *[
                  
                  dbc.Input(
                     
                     value = None,
                     id = f'{k}Id',
                     placeholder = k.title(),
                     className = None
                     
                  )
                  
               for k in (self.setup).keys()],
               html.Hr(),
               
               *[
                                    
                  dbc.Textarea(
                     
                     value = None,
                     id = f'{k}Id',
                     placeholder = k.title(),
                     className = None
                     
                  )
                  
               for k in (self.form).keys()],
               html.Hr(),
               
               # >

               # footer <
               dbc.Stack(
                  
                  gap = 1,
                  direction = 'horizontal',
                  children = [
                     
                     # build <
                     # refresh <
                     dbc.Button(
                        
                        size = 'sm',
                        id = 'buildId',
                        children = 'Build',
                        className = None
                        
                     ),
                     dbc.Button(
                        
                        size = 'sm',
                        children = '⟳',
                        id = 'refreshId',
                        className = None
                        
                     )
                     
                     # >
                     
                  ]
                  
               )
               
               # >
               
            ]
            
         )
         
      )
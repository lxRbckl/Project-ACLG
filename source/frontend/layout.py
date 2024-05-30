# import <
from dash import (dcc, html)
from lxrbckl.local import fileGet
from dash_extensions import Download
import dash_bootstrap_components as dbc
from dash_extensions.snippets import send_file

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
               self.modal(),
               
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
                     className = None,
                     id = f'{k}InputId',
                     placeholder = k.title()
                     
                  )
                  
               for k, v in (self.setup).items()],
               html.Hr(),
               
               *[
                                    
                  dbc.Textarea(
                     
                     className = None,
                     id = f'{k}TextareaId',
                     placeholder = k.title()
                     
                  )
                  
               for k, v in (self.form).items()],
               html.Hr(),
               
               # >

               # footer <
               dbc.Stack(
                  
                  gap = 1,
                  direction = 'horizontal',
                  children = [
                     
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
                     
                  ]
                  
               )
               
               # >
               
            ]
            
         )
         
      )
      
   
   def modal(self):
      '''  '''
      
      return dbc.Modal(
         
         id = 'modalId',
         is_open = True,
         children = [
            
            dbc.ModalHeader(
               
               className = None,
               children = dbc.ModalTitle(children = 'Preview')
               
            ),
            dbc.ModalBody(
               

            
            ),
            dbc.ModalFooter(
               
               className = None,
               children = [
                  
                  dcc.Download(
                     
                     id = 'dccDownloadId'
                     
                  ),
                  dbc.Button(
                     
                     size = 'sm',
                     id = 'dbcDownloadId',
                     children = 'Download'
                     
                  )
                  
               ]
               
            )
            
         ]
         
      )
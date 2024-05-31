# import <
from dash import dcc
import dash_bootstrap_components as dbc

# >


class modal:
   
   
   def __init__(self):
      '''  '''
      
      pass
   
   
   @property
   def modal(self):
      '''  '''
      
      return dbc.Modal(
         
         size = 'lg',
         id = 'modalId',
         is_open = False,
         centered = True,
         children = [
            
            dbc.ModalHeader(
               
               className = None,
               close_button = False,
               children = dbc.ModalTitle('Preview')
               
            ),
            dbc.ModalBody(
               
               dbc.Textarea(
                  
                  value = None, # <-
                  id = 'formId',
                  disabled = True,
                  className = None
                  
               )
            
            ),
            dbc.ModalFooter(
               
               className = None,
               children = dbc.Row(
                  
                  justify = 'between',
                  children = [
                     
                     # download <
                     # clipboard <
                     dbc.Col(
                        
                        width = 'auto',
                        children = dbc.Button(
                           
                           size = 'sm',
                           href = None,
                           download = None,
                           id = 'downloadId',
                           external_link = True,
                           children = 'Download'
                           
                        )
                        
                     ),
                     dbc.Col(
                        
                        width = 'auto',
                        children = dcc.Clipboard(
                           
                           title = 'Copy',
                           target_id = 'formId'
                           
                        )
                        
                     )
                     
                     # >
                     
                  ]
                  
               )
               
            )
            
         ]
         
      )
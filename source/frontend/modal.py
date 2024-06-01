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
            
            # header <
            dbc.ModalHeader(
               
               close_button = False,
               className = 'modalHeader',
               children = dbc.ModalTitle('Preview')
               
            ),
            
            # >
            
            # body <
            dbc.ModalBody(
               
               className = 'modalBody',
               children = dbc.Textarea(
                  
                  value = None,
                  id = 'letterId',
                  disabled = True,
                  className = 'textarea'
                  
               )
            
            ),
            
            # >
            
            # footer <
            dbc.ModalFooter(
               
               className = 'modalFooter',
               children = dbc.Row(
                  
                  className = 'modalFooterRow',
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
                           target_id = 'letterId'
                           
                        )
                        
                     )
                     
                     # >
                     
                  ]
                  
               )
               
            )
            
            # >
            
         ]
         
      )
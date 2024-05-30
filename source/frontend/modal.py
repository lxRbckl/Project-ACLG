# import <
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
         is_open = True,
         centered = True,
         children = [
            
            dbc.ModalHeader(
               
               className = None,
               children = dbc.ModalTitle('Preview')
               
            ),
            dbc.ModalBody(
               
               dbc.Textarea(
                  
                  value = None,
                  disabled = True,
                  id = 'previewId',
                  className = None
                  
               )
            
            ),
            dbc.ModalFooter(
               
               className = None,
               children = [
                  
                  dbc.Button(
                     
                     size = 'sm',
                     href = None,
                     download = None,
                     id = 'downloadId',
                     external_link = True,
                     children = 'Download'
                     
                  )
                  
               ]
               
            )
            
         ]
         
      )
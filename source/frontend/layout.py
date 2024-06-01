# import <
from .modal import modal
from ..data.manage_data import manageData

from dash import html
import dash_bootstrap_components as dbc

# >


class layout:
   
   
   def __init__(self):
      '''  '''
      
      self.modal = modal()
      self.data = manageData()
      self.header = self.data.header
   
   
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
               self.modal.modal,
               
               # >
               
               # header <
               html.H2(
                  
                  className = 'title',
                  children = self.header['title']
               
               ),
               html.Small(
                  
                  className = 'description',
                  children = self.header['description']
                  
               ),
               html.Hr(className = 'divider'),
               
               # >
               
               # body <
               *[
                  
                  dbc.Input(
                     
                     value = None,
                     id = f'{i}Id',
                     required = None,
                     className = 'input',
                     placeholder = i.title()
                     
                  )
                  
               for i in self.data.details],               
               *[
                                    
                  dbc.Textarea(
                     
                     value = None,
                     id = f'{i}Id',
                     className = 'textarea',
                     placeholder = i.title()
                     
                  )
               
               for i in self.data.letter],
               html.Hr(className = 'divider'),
               
               # >

               # footer <
               dbc.Row(
                  
                  justify = 'between',
                  children = [
                     
                     # build <
                     # refresh <
                     dbc.Col(
                        
                        width = 'auto',
                        children = dbc.Button(
                           
                           size = 'sm',
                           id = 'buildId',
                           disabled = True,
                           children = 'Build',
                           className = None
                           
                        )
                        
                     ),
                     dbc.Col(
                        
                        width = 'auto',
                        children = dbc.Button(
                           
                           size = 'sm',
                           children = '⟳',
                           id = 'refreshId',
                           className = None
                           
                        )
                        
                     )
                     
                     # >
                     
                  ]
                  
               )
               
               # >

            ]
            
         )
         
      )
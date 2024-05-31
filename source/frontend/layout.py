# import <
from .modal import modal
from ..configuration import data

from dash import (dcc, html)
from lxrbckl.local import fileGet
import dash_bootstrap_components as dbc

# >


class layout:
   
   
   def __init__(self):
      '''  '''
      
      self.data = data()
      self.modal = modal()
      self.body = (self.data).body
      self.header = (self.data).header
   
   
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
                  
                  className = None,
                  children = self.header['title']
               
               ),
               html.Small(
                  
                  className = None,
                  children = self.header['description']
                  
               ),
               html.Hr(),
               
               # >
               
               # body <
               *[
                  
                  dbc.Input(
                     
                     value = None,
                     id = f'{i}Id',
                     placeholder = i.title(),
                     className = None
                     
                  )
                  
               for i in self.data.details],               
               *[
                                    
                  dbc.Textarea(
                     
                     value = None,
                     id = f'{i}Id',
                     placeholder = i.title(),
                     className = None
                     
                  )
               
               for i in self.data.letter],
               html.Hr(),
               
               # >

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

            ]
            
         )
         
      )
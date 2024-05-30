# import <
from dash import Dash
from dash_bootstrap_components import themes

# >


application = Dash(
   
   name = 'ACLG',
   title = 'ACLG',
   suppress_callback_exceptions = True,
   external_stylesheets = [
      
      themes.GRID,
      themes.BOOTSTRAP
      
   ]
   
)
server = application.server
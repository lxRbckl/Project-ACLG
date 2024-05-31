# import <
from source.frontend.layout import layout
from source.frontend.callbacks import callbacks
from source.configuration import (application, server)

# >


if (__name__ == '__main__'):
      
   objLayout = layout()
   objCallbacks = callbacks()
   
   objCallbacks.register()
   application.layout = objLayout.layout
   
   application.run(debug = True, port = 8059)
   
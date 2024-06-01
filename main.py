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
   
   application.run(host = '0.0.0.0', port = 8060)
   
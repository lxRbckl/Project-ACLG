# import <
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
   
   Image,
   Paragraph,
   SimpleDocTemplate
   
)

# >


class generatePDF:
   
   
   def __init__(self):
      '''  '''
      
      self._width = 171
      self._height = 65
   
   
   def generate(
      
      self,
      letter,
      company,
      signature,
      uploadpath
   
   ):
      '''  '''
      
      document = SimpleDocTemplate(f'{uploadpath}/{company}.pdf')
            
      styles = getSampleStyleSheet()
      style = styles['BodyText']
      style.alignment = 4
               
      convert = lambda i : Paragraph(i, style)
      output = [convert(i) for i in letter.split('\n')]
      output.append(Image(
         
         signature, 
         hAlign = 'LEFT',
         width = self._width,
         height = self._height,
      
      ))
      
      document.build(output)
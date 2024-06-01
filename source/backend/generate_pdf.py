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
      
      pass
   
   
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
      output.append(Image(signature, hAlign = 'LEFT'))
      
      document.build(output)
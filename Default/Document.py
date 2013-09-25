'''
Created on 23/09/2013

@author: igor
'''

class Document:
    '''
    classdocs
    '''
    
    # Caminho raiz 
    root_path = r"C:\IGOR_TRABALHO\AEB\PESQUISA_PLN"
    
   
    document2 = input("Please select the document in order to be indexed.")
    
    #print("the document is:" + document)
    
  

    def __init__(self, document):
        '''
        Constructor
        '''
        self.document = document
        
    def openDocument(self):
        #abrir PNAE
        import codecs
        root_path = r"C:\IGOR_TRABALHO\AEB\PESQUISA_PLN"
        fp_pnae_html = codecs.open(root_path + r"\PNAE\PNAE_otimo.txt",encoding="utf8")
        pnae = fp_pnae_html.readlines()
        pnae = [w.split() for w in pnae]
        fp_pnae_html.close()
        return pnae
        
        
        
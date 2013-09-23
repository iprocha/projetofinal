'''
Created on 23/09/2013

@author: igor
'''

class MyClass(object):
    '''
    classdocs
    '''
    import codecs
    # Caminho raiz 
    root_path = r"C:\IGOR_TRABALHO\AEB\PESQUISA_PLN"

    
    #abrir PNAE
    fp_pnae_html = codecs.open(root_path + r"\PNAE\PNAE_otimo.txt",encoding="utf8")
    pnae = fp_pnae_html.readlines()
    pnae = [w.split() for w in pnae]
    fp_pnae_html.close()

    def __init__(self):
        '''
        Constructor
        '''
        
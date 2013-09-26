'''
Created on 23/09/2013

@author: igor
'''
class Dictionary():
    dicionario = ["teste"]
    def __init__(self, dictionaryPath):
        self.dictionary = dictionaryPath
    
    def openDictionary(self):
        import codecs
        # Caminho raiz 
        root_path = r"C:\Users\igor.rocha\Documents\PESQUISA_PLN"
        #abrir dicionario
        fp_dicionario = codecs.open(root_path + r"\CORPUS\CORPUS_AEB\comuns_pnae_astronomia.txt",encoding="utf8")
        dicionario = fp_dicionario.readlines()
        dicionario = [w.strip() for w in dicionario]
        fp_dicionario.close()  
        return dicionario


    def structureDictionary(self):
        #Organizar palavras na matriz
        dicionario = self.openDictionary()
        self.dictionaryMatrix = []
        self.dictionaryList = []
        result = []
        for w in range(len(dicionario)):
            result.append([])
        z = 0
        for w in range(len(dicionario)):
            if(" " in dicionario[w] and dicionario[z] in dicionario[w]):
                result[z].append(dicionario[w])
            else:
                result[w] = [dicionario[w]]
                z = w
        result = [ w for w in result if w!=[]]
        
        result1 = []
        for w in range(len(result)):
            result1.append(result[w][0])
#         print("%%%%RESULT%%%%===")
#         print(result)
#         print("\n\n\n\n")
#         print("%%%%RESULT01%%%%===")
#         print(result1)
        self.dictionaryList = result
        self.dictionaryMatrix = result1
        
        
                
                
'''
Created on 23/09/2013

@author: igor
'''

class MyClass(object):
    '''
    classdocs
    '''
    # -*- coding: utf-8 -*-
"""
Created on Tue Nov 09 16:48:49 2010

@author: igor.pessoa
"""
# testing version control 
#ALGORITMO OTIMIZADO 03 (trocar o metodo de procura das palavras, mudando o sentido para "pnae para o dicionario"
#e )
import codecs

# Caminho raiz 
root_path = r"C:\IGOR_TRABALHO\AEB\PESQUISA_PLN"



#abrir PNAE
fp_pnae_html = codecs.open(root_path + r"\PNAE\PNAE_otimo.txt",encoding="utf8")
pnae = fp_pnae_html.readlines()
pnae = [w.split() for w in pnae]
fp_pnae_html.close()

#abrir dicionario
fp_dicionario = codecs.open(root_path + r"\CORPUS\CORPUS_AEB\comuns_pnae_astronomia.txt",encoding="utf8")
dicionario = fp_dicionario.readlines()
dicionario = [w.strip() for w in dicionario]
fp_dicionario.close()


#Organizar palavras na matriz
result = []
for w in range(len(dicionario)):
    result.append([])
z = 0
k = 0
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

#funcao que retorna o grau da maior expressao de uma lista

def grau_palavra1(palavra):
    grau = len(palavra.split())
    return grau
    
#Algoritmo principal
controlador = 0
comuns_expressoes = []
for y in range(len(pnae)):
    for x in range(len(pnae[y])):
        if pnae[y][x] in result1:
            w = result1.index(pnae[y][x])
            if len(result[w]) > 1:
                for k in reversed(range(len(result[w])-1)):
                    if (" ".join(pnae[y][x:x+(grau_palavra1(result[w][k+1]))])).lower() == (result[w][k+1]).lower():
                        fp_significado = codecs.open(root_path + r'\PNAE\PNAE_HTML'+'\\'+(result[w][k+1]).lower()+r'.txt',encoding="utf8")
                        significado = fp_significado.read()
                        fp_significado.close()
                        pnae[y][x] = '<a title="'+significado+'"><b><Font color="red">'+pnae[y][x]
                        pnae[y][x+((grau_palavra1(result[w][k+1]))-1)] = pnae[y][x+((grau_palavra1(result[w][k+1]))-1)]+'</font></b></a>'
                        controlador = 1
                        comuns_expressoes.append((result[w][k+1]).lower())
                        break
                if controlador == 1:
                    controlador = 0
                    break
                else:
                    fp_significado = codecs.open(root_path + r'\PNAE\PNAE_HTML'+'\\'+pnae[y][x].lower()+r'.txt',encoding="utf8")
                    significado = fp_significado.read()
                    fp_significado.close()
                    pnae[y][x] = '<a title="'+significado+'"><b><Font color="blue">'+pnae[y][x]+'</font></b></a>'
            else:
                fp_significado = codecs.open(root_path + r'\PNAE\PNAE_HTML'+'\\'+pnae[y][x].lower()+r'.txt',encoding="utf8")
                significado = fp_significado.read()
                fp_significado.close()
                pnae[y][x] = '<a title="'+significado+'"><b><Font color="blue">'+pnae[y][x]+'</font></b></a>'

#saida de dados
[w.append("\n") for w in pnae]
pnae = [" ".join(w) for w in pnae]
pnae_utf8 = [w.encode("utf-8") for w in pnae]
fp_saida = open(root_path + r"\TESTES\Teste_Expressoes12.txt","w")
[fp_saida.writelines(w.__str__()) for w in pnae_utf8]
fp_saida.close()


def __init__(self):
        '''
        Constructor
        '''
        
import math

def getNumDuplas(variavel: list[int]):
    return len(variavel)
    
def calcularMediaAritmetica(variavel: list[int], num_elementos: int) -> float:
    somatorio = 0
    for i in range(num_elementos):
        somatorio += variavel[i]
    
    return somatorio/num_elementos


def calcularMediaDoProduto(X:list[int], Y:list[int],num_elementos) -> float:  
    resultado = 0  
    for i in range(num_elementos):
        resultado += X[i]*Y[i]
    
    return resultado/num_elementos

def calcularCovariancia(mediaX:float, mediaY:float, mediaDoProduto:float) -> float:
    return  mediaDoProduto - mediaX*mediaY

def calcularMediaDosQuadrados(variavel: list[int], num_elementos: int) -> float:
    somatorio = 0
    for i in range(num_elementos):
        somatorio += variavel[i]**2
    return somatorio/num_elementos
 
def calcularDesvioPadrao(mediaDosQuadrados:float,mediaAritmetica:float) -> float:
    return math.sqrt(mediaDosQuadrados - (mediaAritmetica**2))

#TO-DO: com 8 casas decimais
def calcularCoeficienteDePearson(covariancia:float,desvioPadraoX:float, desvioPadraoY: float) -> float:
    return covariancia/(desvioPadraoY*desvioPadraoX)

#TO-DO:colocar o coeficiente em porcentagem e com duas decimais
def calcularCoeficienteDeDeterminacao(coeficienteDePearson: float) -> float:
    return coeficienteDePearson**2
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

def calcularCoeficienteDePearson(covariancia:float,desvioPadraoX:float, desvioPadraoY: float) -> float:
    return covariancia/(desvioPadraoY*desvioPadraoX)

def calcularCoeficienteDeDeterminacao(coeficienteDePearson: float) -> float:
    return coeficienteDePearson**2

def calcularSomas(X: list[float], Y: list[float], num_elementos: int):
    somaX = sum(X)
    somaY = sum(Y)
    somaXY = sum(X[i]*Y[i] for i in range(num_elementos))
    somaX2 = sum(x**2 for x in X)
    somaY2 = sum(y**2 for y in Y)
    return somaX, somaY, somaXY, somaX2, somaY2


def calcularRetaRegressao(X:list[float], Y:list[float], num_elementos: int) -> tuple:
    somaX, somaY, somaXY, somaX2, _ = calcularSomas(X, Y, num_elementos)
    b = (num_elementos * somaXY - somaX * somaY) / (num_elementos * somaX2 - somaX**2)
    a = (somaY - b * somaX) / num_elementos
    return a, b

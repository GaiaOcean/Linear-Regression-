import math

def getNumDuplas(dados: list[int]):
    return len(dados)
    
def calcularMediaAritmetica(dados: list[int], num_elementos: int) -> float:
    soma_elementos = 0
    for i in range(num_elementos):
        soma_elementos += dados[i]
    return soma_elementos/num_elementos

def calcularMediaDoProduto(X:list[int], Y:list[int],num_elementos) -> float:  
    soma_produtos = 0  
    for i in range(num_elementos):
        soma_produtos += X[i]*Y[i]
    return soma_produtos/num_elementos

def calcularCovariancia(media_variavel_X:float, media_variavel_Y:float, media_produto_xy:float) -> float:
    return  media_produto_xy - media_variavel_X*media_variavel_Y

def calcularMediaDosQuadrados(dados: list[int], num_elementos: int) -> float:
    soma_quadrados = 0
    for i in range(num_elementos):
        soma_quadrados += dados[i]**2
    return soma_quadrados/num_elementos
 
def calcularDesvioPadrao(media_quadrados:float,media_aritmetica:float) -> float:
    return math.sqrt(media_quadrados - (media_aritmetica**2))

def calcularCoeficienteDePearson(covariancia:float,desvio_padrao_X:float, desvio_padrao_Y: float) -> float:
    return covariancia/(desvio_padrao_Y*desvio_padrao_X)

def calcularCoeficienteDeDeterminacao(coeficiente_pearson: float) -> float:
    return coeficiente_pearson**2

def calcularSomas(X: list[float], Y: list[float], num_elementos: int):
    soma_variavel_X = sum(X)
    soma_variavel_Y = sum(Y)
    soma_produto_xy = sum(X[i]*Y[i] for i in range(num_elementos))
    soma_quadrados_x = sum(x**2 for x in X)
    soma_quadrados_y= sum(y**2 for y in Y)
    return soma_variavel_X, soma_variavel_Y, soma_produto_xy, soma_quadrados_x, soma_quadrados_y


def calcularRetaRegressao(X:list[float], Y:list[float], num_elementos: int) -> tuple:
    soma_variavel_X, soma_variavel_Y, soma_produto_xy, soma_quadrados_x, _ = calcularSomas(X, Y, num_elementos)
    b = (num_elementos * soma_produto_xy - soma_variavel_X * soma_variavel_Y) / (num_elementos * soma_quadrados_x - soma_variavel_X**2)
    a = (soma_variavel_Y - b * soma_variavel_X) / num_elementos
    return a, b

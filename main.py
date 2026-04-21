import methods

if __name__ == "__main__":
    x = [6,5,8,8,7,6,10,4,9,7]
    y = [8 ,7 ,7 ,10 ,5 ,8 ,10 ,6 ,8, 6]
    mediaX = methods.calcularMediaAritmetica(x,10)
    mediaY = methods.calcularMediaAritmetica(y,10)
    mediaDoProduto = methods.calcularMediaDoProduto(x,y,10)
    covariancia = methods.calcularCovariancia(mediaX,mediaY,mediaDoProduto)
    print(mediaX)
    print(mediaY)
    print(mediaDoProduto)
    print(covariancia)
    
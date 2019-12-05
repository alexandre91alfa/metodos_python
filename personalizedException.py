class MaiorMenorErro(Exception):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('insira um valor de 0 a 10.'))
        print(x)
        if x > 10 or x < 0:
            raise MaiorMenorErro('Erro da merda')
        break
    except ValueError:
        print('Valor invalido.')
    except MaiorMenorErro as e:
        print(e)

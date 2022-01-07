import sys

from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível da dificuldade desejada [1, 2. 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado desejado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos +=1

    else:
        if pontos > 0:
            pontos -= 1
        else:

            print('Você não tem mais vidas')
            sys.exit()

    print(f'Voce tem {pontos} ponto(s).')

    continuar : int = int(input('Deseja continuar no jogo? [1 - sim, 0 - não]: '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Voce finalizou com {pontos} ponto(s).')
        print('Até a próxima!')


if __name__ == '__main__':
    main()
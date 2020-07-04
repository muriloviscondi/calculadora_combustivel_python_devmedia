from calculo import Calculo

def main ():
    print(
        """
        Esta aplicação tem como finalidade demonstrar os valores que serão gastos 
        com combustível durante uma viagem, com base no consumo do seu veículo, e 
        com a distância determinada por você!
        """
    )

    print('Os Combiustíveis disponíveis para este cálculo são: ')
    print('  ° Álcool')
    print('  ° Gasolina')
    print('  ° Diesel')

    print(' ')

    try:
        distancia: float = float(input(
            'Distância em quilometros a ser percorrida: ')
        )
        consumo: float = float(input(
            'Consumo de combustível de veiculo (Km/l): ')
        )

        calculo = Calculo()
        print(
            calculo.calcular_gasto(distancia, calculo)
        )

    except ValueError as erro:
        print('O valor recebido não é valido')


if __name__ == '__main__':
    main()

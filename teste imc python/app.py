# Função que calcula o IMC
def calcular_imc(peso, altura):
    # A fórmula do IMC é: peso dividido pela altura elevada ao quadrado
    imc = peso / (altura ** 2)
    return imc

# Função que classifica o resultado do IMC com base nos padrões da OMS
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Bloco principal do programa
try:
    # Solicitando os dados do usuário e convertendo para float (número decimal)
    # Dica: use ponto (.) em vez de vírgula (,) ao digitar
    peso = float(input("Digite seu peso em kg (ex: 75.5): "))
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))

    # Executa o cálculo chamando a função criada acima
    resultado_imc = calcular_imc(peso, altura)
    
    # Obtém a classificação do peso
    classificacao = classificar_imc(resultado_imc)

    # Exibe os resultados na tela
    # O ':.2f' serve para arredondar o resultado para 2 casas decimais
    print("\n--- Resultado ---")
    print(f"Seu IMC é: {resultado_imc:.2f}")
    print(f"Classificação: {classificacao}")

except ValueError:
    # Caso o usuário digite texto ou use vírgula incorretamente, o programa não quebra
    print("\nErro: Por favor, insira valores numéricos válidos. Use ponto (.) para decimais.")
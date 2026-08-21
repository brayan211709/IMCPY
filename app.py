# Define a função para calcular o IMC recebendo peso e altura
def calcular_imc(peso, altura):
    # Calcula o IMC dividindo o peso pela altura elevada ao quadrado
    imc = peso / (altura**2)
    # Retorna o valor calculado do IMC para quem chamou a função
    return imc


# Define a função para classificar o IMC com base no resultado obtido
def classificar_imc(imc):
    # Verifica se o IMC é menor que 18.5 (abaixo do peso)
    if imc < 18.5:
        # Retorna o texto correspondente a esta faixa de peso
        return "Abaixo do peso"
    # Verifica se o IMC está entre 18.5 e 24.9 (peso normal)
    elif 18.5 <= imc < 25:
        # Retorna o texto correspondente a esta faixa de peso
        return "Peso normal"
    # Verifica se o IMC está entre 25.0 e 29.9 (sobrepeso)
    elif 25 <= imc < 30:
        # Retorna o texto correspondente a esta faixa de peso
        return "Sobrepeso"
    # Se não entrar em nenhuma das condições anteriores, é maior ou igual a 30
    else:
        # Retorna o texto correspondente à obesidade
        return "Obesidade"


# Inicia um bloco de tratamento de erros para evitar que o programa feche sozinho
try:
    # Solicita o peso ao usuário, lê o texto digitado e o converte em número decimal (float)
    peso = float(input("Digite seu peso em kg (ex: 75.5): "))
    # Solicita a altura ao usuário, lê o texto digitado e o converte em número decimal (float)
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))

    # Chama a função calcular_imc passando o peso e altura e guarda o retorno na variável resultado_imc
    resultado_imc = calcular_imc(peso, altura)

    # Chama a função classificar_imc passando o resultado do IMC e guarda o texto na variável classificacao
    classificacao = classificar_imc(resultado_imc)

    # Imprime uma linha em branco e um cabeçalho estético no terminal
    print("\n--- Resultado ---")
    # Imprime o IMC formatado com apenas duas casas decimais após o ponto
    print(f"Seu IMC é: {resultado_imc:.2f}")
    # Imprime a classificação final do peso do usuário
    print(f"Classificação: {classificacao}")

# Caso ocorra um erro de valor (como digitar letras ou usar vírgula em vez de ponto)
except ValueError:
    # Imprime uma mensagem de erro amigável explicando o que deu errado
    print(
        "\nErro: Por favor, insira valores numéricos válidos. Use ponto (.) para decimais."
    )
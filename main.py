# Dev. Lucas Fraga - 100 Days of Code: The Complete Python Pro Bootcamp - IMCFit 1.0
# PT-BR: Calculadora que determina o índice de massa corporal com base na altura e peso, auxiliando na avaliação do estado de saúde e forma física.
# EN-US: Calculator that determines body mass index based on height and weight, helping to assess health and fitness.

# Constantes para classificação do IMC // Constants for BMI classification
UNDERWEIGHT_SEVERE = 16
UNDERWEIGHT_MODERATE = 17
UNDERWEIGHT_MILD = 18.5
NORMAL_WEIGHT = 24.9
OVERWEIGHT = 29.9
OBESE_I = 34.9
OBESE_II = 39.9

# Mensagem de boas vindas e citação // Welcome message and quote
welcome_message_pt = "\nPT-BR: Bem vindo(a) à calculadora de IMC - Índice de Massa Corpórea"
welcome_message_en = "EN-US: Welcome to the BMI - Body Mass Index calculator\n"
quote_pt = '"Você é o que você come." (Alan Levinovitz)'
quote_en = '"You are what you eat." (Alan Levinovitz)\n'

# Mostra mensagens de boas vindas // Show welcome messages
print(welcome_message_pt)
print(welcome_message_en)
print()
print(quote_pt)
print(quote_en)

# Solicita peso e altura do usuário // Requests user's weight and height
weight = float(input("Qual o seu peso? (kg) / What is your weight (kg)? "))
height_cm = int(input("Qual é sua altura em centímetros (cm)? / What is your height in centimeters (cm)? "))
height_meter = height_cm / 100.00

# Calcula o IMC // Calculates BMI
bmi = weight / height_meter ** 2

# Classifica o IMC e exibe o resultado // Classifies BMI and displays the result
if bmi < UNDERWEIGHT_SEVERE:
    print(f"\nSeu IMC é {bmi:.1f}. Isso é classificado como: Gravemente abaixo do peso.")
    print(f"Your BMI is {bmi:.1f}. This is classified as: Severe Thinness.\n")
    print("É importante procurar ajuda médica para tratar sua saúde. / It is important to seek medical help to address your health.\n")
elif UNDERWEIGHT_SEVERE <= bmi <= UNDERWEIGHT_MODERATE:
    print(f"\nSeu IMC é {bmi:.1f}. Isso é classificado como: Moderadamente abaixo do peso.")
    print(f"Your BMI is {bmi:.1f}. This is classified as: Moderate Thinness.\n")
    print("Considere revisar sua alimentação e hábitos de vida. / Consider reviewing your diet and lifestyle habits.\n")
elif UNDERWEIGHT_MODERATE < bmi <= UNDERWEIGHT_MILD:
    print(f"\nSeu IMC é {bmi:.1f}. Isso é classificado como: Ligeiramente abaixo do peso.")
    print(f"Your BMI is {bmi:.1f}. This is classified as: Mild Thinness.\n")
    print("Uma leve atenção à sua alimentação pode ajudar. / Paying a little attention to your diet can help.\n")
elif UNDERWEIGHT_MILD < bmi <= NORMAL_WEIGHT:
    print(f"\nSeu IMC é {bmi:.1f}. Isso é classificado como: Peso normal.")
    print(f"Your BMI is {bmi:.1f}. This is classified as: Normal weight.\n")
    print("Parabéns, você está dentro da faixa de peso saudável! / Congratulations, you are within the healthy weight range!\n")
elif NORMAL_WEIGHT < bmi <= OVERWEIGHT:
    print(f"\nSeu IMC é {bmi:.1f}. Isso é classificado como: Sobrepeso.")
    print(f"Your BMI is {bmi:.1f}. This is classified as: Overweight.\n")
    print("Considere rever sua dieta e praticar exercícios físicos regularmente. / Consider reviewing your diet and exercising regularly.\n")
elif OVERWEIGHT < bmi <= OBESE_I:
    print(f"\nSeu IMC é {bmi:.1f}. Isso é classificado como: Obesidade grau I.")
    print(f"Your BMI is {bmi:.1f}. This is classified as: Obesity class I.\n")
    print("Atenção! É importante procurar orientação médica para melhorar sua saúde. / Attention! It is important to seek medical guidance to improve your health.\n")
elif OBESE_I < bmi <= OBESE_II:
    print(f"\nSeu IMC é {bmi:.1f}. Isso é classificado como: Obesidade grau II.")
    print(f"Your BMI is {bmi:.1f}. This is classified as: Obesity class II.\n")
    print("Procure ajuda médica para um plano de saúde adequado. / Seek medical help for an appropriate health plan.\n")
else:
    print(f"\nSeu IMC é {bmi:.1f}. Isso é classificado como: Obesidade grau III / Obesity class III.")
    print(f"Your BMI is {bmi:.1f}. This is classified as: Obesity class III.\n")
    print("É crucial buscar acompanhamento médico imediatamente para melhorar sua saúde. / It is crucial to seek medical follow-up immediately to improve your health.\n")
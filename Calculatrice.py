def calcul(operande_1,operateur_,operande_2):
    if operateur_ == '+' :
        result = operande_1+operande_2

    if operateur_ == '-' :
        result = operande_1-operande_2

    if operateur_ == '*' :
        result = operande_1*operande_2

    if operateur_ == '/' :
        result = operande_1/operande_2
    return result

def read_value():
    value = input("Choissez un calcul : ").strip()
    return value
value = read_value()
while value != "exit" :

    elements = value.split(' ')
    if len(elements) == 3 :
        operande1 = int(elements[0])
        operande2 = int(elements[2])
        operateur = elements[1]
        resultat = calcul(operande1,operateur,operande2)        
        print(resultat)

    elif len(elements) == 5 :
        operande1 = int(elements[0])
        operande2 = int(elements[2])
        operande3 = int(elements[4])
        operateur1 = elements[1]
        operateur2 = elements[3]
        resultat = calcul(operande1,operateur1,operande2)
        resultat = calcul(resultat,operateur2,operande3)        
        print(resultat)
    value = read_value()
def sudoku():   
    # Aqui está sendo criada a grade do jogo, onde estarão os números
    grade = [[0 for _ in range(9)] for _ in range(9)]
    return grade
 
def imprimir_grade(grade):
    for i in range(9):
        for j in range(9):
            print(grade[i][j], end=" ")
            if (j + 1) % 3 == 0 and j != 8:
                print("|", end=" ")
        print()
        if (i + 1) % 3 == 0 and i != 8:
            print("- - - - - - - - - -")
 
def verificar_numero_repetido(grade, linha, coluna, numero): # Aqui está sendo feita a verificação de numeros na linha
    if numero in grade[linha]:  # se a variavel numero estiver em grade, retornará verdadeiro
        return True
 
    for i in range(9):  # Aqui verifica os números da coluna
        if grade[i][coluna] == numero:
            return True
 
    bloco_linha = linha // 3   # Aqui esta sendo verificado se onúmero ja existe no bloco
    bloco_coluna = coluna // 3
    for i in range(bloco_linha * 3, (bloco_linha + 1) * 3):
        for j in range(bloco_coluna * 3, (bloco_coluna + 1) * 3):
            if grade[i][j] == numero:
                return True
    return False
 
def verificar_solucao_valida(grade): # Está verificando se nas LINHAS, os números de 1 a 9 não estão se repetindo

    for i in range(9):
        linha = [grade[i][j] for j in range(9)]
        if len(set(linha)) != 9:
            return False
 

    for j in range(9):  # Está verificando se nas COLUNAS, os números de 1 a 9 não estão se repetindo
        coluna = [grade[i][j] for i in range(9)]
        if len(set(coluna)) != 9:
            return False
 
    # Verifica se cada bloco 3x3 tem os números de 1 a 9 sem repetição
    for i in range(0, 9, 3): # Está verificando se nos BLOCOS, os números de 1 a 9 não estão se repetindo
        for j in range(0, 9, 3):
            bloco = [grade[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if len(set(bloco)) != 9:
                return False
 
    return True
 
 # APRESENTAÇÃO DO CÓDIGO - RESULTADO:

def main():
    grade = sudoku()
 
    while True:
        imprimir_grade(grade)
        linha = - 1 # AQUI SERÁ SELECIONADA A LINHA QUE DESEJA ADICIONAR UM VALOR
        coluna = int(input("Digite a coluna (1-9): ")) - 1 # AQUI SERÁ SELECIONADA A COLUNA EM QUE DESEJA ADICIONAR UM VALOR
        numero = int(input("Digite o número (1-9): ")) # AQUI SERÁ ESCOLHIDO O NÚMERO A SER ADICIONADO PARA COMPARAÇÃO

        if verificar_numero_repetido(grade, linha, coluna, numero):
            print("Número repetido! Tente novamente.")
        else:
            grade[linha][coluna] = numero
 
        if verificar_solucao_valida(grade):
            print("Solução válida! Parabéns!")
            break
 
if __name__ == "__main__":
    main()
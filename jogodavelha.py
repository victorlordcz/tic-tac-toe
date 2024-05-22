def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 10)

def verificar_vencedor(tabuleiro, jogador):
    for linha in tabuleiro:
        if all([celula == jogador for celula in linha]):
            return True
    for col in range(3):
        if all([tabuleiro[linha][col] == jogador for linha in range(3)]):
            return True
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True
    return False

def tabuleiro_cheio(tabuleiro):
    return all([celula in ['X', 'O'] for linha in tabuleiro for celula in linha])

def main():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    
    while True:
        imprimir_tabuleiro(tabuleiro)
        try:
            jogada = int(input(f"Jogador {jogador_atual}, insira sua jogada (1-9): ")) - 1
            if jogada < 0 or jogada >= 9:
                raise ValueError("Jogada inválida. Insira um número entre 1 e 9.")
            linha, coluna = divmod(jogada, 3)
            if tabuleiro[linha][coluna] != " ":
                raise ValueError("Celula já ocupada. Escolha outra.")
        except ValueError as e:
            print(e)
            continue
        
        tabuleiro[linha][coluna] = jogador_atual
        
        if verificar_vencedor(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break
        
        if tabuleiro_cheio(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break
        
        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    main()

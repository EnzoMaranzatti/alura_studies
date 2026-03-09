import random

OPCOES = ("pedra", "papel", "tesoura")

def menu():
    print("\nPEDRA, PAPEL E TESOURA")
    print("======================")
    print("1) Iniciar jogo (2 jogadores)")
    print("2) Iniciar jogo (vs computador)")
    print("3) Sair")
    while True:
        try:
            op = int(input("Escolha uma opção: "))
            if op in (1, 2, 3):
                return op
            print("Opção inválida. Digite 1, 2 ou 3.")
        except ValueError:
            print("Digite um número válido.")

def ler_jogada(nome):
    while True:
        jogada = input(f"{nome}, escolha [pedra/papel/tesoura]: ").strip().lower()
        if jogada in OPCOES:
            return jogada
        print("Jogada inválida. Tente novamente.")

def checar_resultado(jogada1, jogada2):
    """
    Retorna:
    0 = empate
    1 = jogador 1 vence
    2 = jogador 2 vence
    """
    if jogada1 == jogada2:
        return 0

    vence = {
        "pedra": "tesoura",
        "tesoura": "papel",
        "papel": "pedra",
    }

    if vence[jogada1] == jogada2:
        return 1
    return 2

def iniciar_jogo_2jogadores():
    qtd_rounds = int(input("Quantos rounds terá o jogo? "))
    j1 = input("Nome do jogador 1: ").strip() or "Jogador 1"
    j2 = input("Nome do jogador 2: ").strip() or "Jogador 2"

    placar = {j1: 0, j2: 0, "empates": 0}

    for r in range(1, qtd_rounds + 1):
        print(f"\nROUND {r}")
        jogada1 = ler_jogada(j1)
        jogada2 = ler_jogada(j2)

        res = checar_resultado(jogada1, jogada2)

        print(f"{j1} jogou: {jogada1} | {j2} jogou: {jogada2}")

        if res == 0:
            print("Empate!")
            placar["empates"] += 1
        elif res == 1:
            print(f"{j1} venceu o round!")
            placar[j1] += 1
        else:
            print(f"{j2} venceu o round!")
            placar[j2] += 1

    print("\n===== PLACAR FINAL =====")
    print(f"{j1}: {placar[j1]}")
    print(f"{j2}: {placar[j2]}")
    print(f"Empates: {placar['empates']}")

    if placar[j1] > placar[j2]:
        print(f"🏆 Vencedor do jogo: {j1}")
    elif placar[j2] > placar[j1]:
        print(f"🏆 Vencedor do jogo: {j2}")
    else:
        print("🏁 Jogo empatado!")

def iniciar_jogo_vs_pc():
    qtd_rounds = int(input("Quantos rounds terá o jogo? "))
    j1 = input("Seu nome: ").strip() or "Você"
    pc = "Computador"

    placar = {j1: 0, pc: 0, "empates": 0}

    for r in range(1, qtd_rounds + 1):
        print(f"\nROUND {r}")
        jogada1 = ler_jogada(j1)
        jogada2 = random.choice(OPCOES)

        res = checar_resultado(jogada1, jogada2)

        print(f"{j1} jogou: {jogada1} | {pc} jogou: {jogada2}")

        if res == 0:
            print("Empate!")
            placar["empates"] += 1
        elif res == 1:
            print(f"{j1} venceu o round!")
            placar[j1] += 1
        else:
            print(f"{pc} venceu o round!")
            placar[pc] += 1

    print("\n===== PLACAR FINAL =====")
    print(f"{j1}: {placar[j1]}")
    print(f"{pc}: {placar[pc]}")
    print(f"Empates: {placar['empates']}")

    if placar[j1] > placar[pc]:
        print(f"🏆 Vencedor do jogo: {j1}")
    elif placar[pc] > placar[j1]:
        print("🏆 Vencedor do jogo: Computador")
    else:
        print("🏁 Jogo empatado!")

def main():
    while True:
        op = menu()
        if op == 1:
            iniciar_jogo_2jogadores()
        elif op == 2:
            iniciar_jogo_vs_pc()
        else:
            print("Saindo do jogo...")
            break

main()


import random

def main():
    sign = presentation()

    if sign == "YES":

        while True:
            # Reinicia las manos para la nueva partida
            PC_hand.clear()
            PL_hand.clear()

            pc_play1()
            loop_gamexd()

            if sum(PL_hand) <= 21:
                pc_play2()

                if sum(PC_hand) <= 21:
                    total_player = sum(PL_hand)
                    total_house = sum(PC_hand)

                    if total_player > total_house:
                        print("CONGRATULATIONS YOU WIN")
                    elif total_player == total_house:
                        print("DRAW GAME")
                    else:
                        print("YOU LOSE")
                else:
                    print("CONGRATULATIONS YOU WIN")

            answer = input(
                "Do you want to play again? Write YES to continue: "
            ).strip().upper()

            if answer != "YES":
                break

def presentation():
    """
    Muestra la presentación del juego y pregunta al usuario si desea jugar.

    Returns:
        str: Respuesta del usuario convertida a mayúsculas.
    """
    print("|| Welcome to Blackjack in Place 2026 ||")

    answer = input(
        "Do you want to play? (Write YES to play): "
    ).strip().upper()

    return answer


# Mano de la computadora.
PC_hand = []

# Mano del jugador.
PL_hand = []


# Valores de las cartas especiales.
J = 10
Q = 10
K = 10

# Lista de posibles valores de las cartas.
# El número 1 representa inicialmente al as.
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, 1]


def value_ace(total_actual):
    """
    Determina el valor más conveniente para un as.

    El as vale 11 cuando el total actual es menor o igual a 10.
    En caso contrario, vale 1 para reducir el riesgo de superar 21.

    Args:
        total_actual (int): Suma de las cartas antes de añadir el as.

    Returns:
        int: Valor del as, que puede ser 11 o 1.
    """
    if total_actual <= 10:
        return 11
    else:
        return 1


def pc_play1():
    """
    Reparte la primera carta de la computadora.

    La carta se selecciona aleatoriamente y se añade a PC_hand.
    """
    global PC_hand

    pc_card = random.choice(cards)
    PC_hand.append(pc_card)

    print("House hand:", PC_hand)


def pc_play2():
    """
    Ejecuta el turno completo de la computadora.

    La computadora continúa pidiendo cartas mientras tenga menos de
    17 puntos. Si recibe un as, se calcula si debe valer 1 u 11.
    """
    global PC_hand

    while sum(PC_hand) < 17:
        pc_card = random.choice(cards)

        if pc_card == 1:
            # Se calcula el valor más conveniente para el as.
            total_actual = sum(PC_hand)
            ace = value_ace(total_actual)
            PC_hand.append(ace)

        else:
            PC_hand.append(pc_card)

    print(
        "House hand:",
        PC_hand,
        "-> Total:",
        sum(PC_hand)
    )


def user_play():
    """
    Reparte una carta al jugador.

    Si la carta es un as, se determina si debe valer 1 u 11.
    Después, se comprueba si el jugador superó los 21 puntos.

    Returns:
        str:
            "ok" si el jugador tiene 21 puntos o menos.
            "not good" si el jugador supera los 21 puntos.
    """
    global PL_hand

    user_card = random.choice(cards)

    if user_card == 1:
        # Se calcula el valor más conveniente para el as.
        total_actual = sum(PL_hand)
        ace = value_ace(total_actual)
        PL_hand.append(ace)

    else:
        PL_hand.append(user_card)

    total_player = sum(PL_hand)

    print(
        "Your hand:",
        PL_hand,
        "-> Total:",
        total_player
    )

    # El jugador pierde inmediatamente si supera 21.
    if total_player > 21:
        print("You're higher than 21. You Lose")
        return "not good"

    return "ok"


def loop_gamexd():
    """
    Controla el turno del jugador.

    El jugador puede escribir:

    HIT:
        Solicita una nueva carta.

    STAND:
        Conserva su mano y termina su turno.

    El ciclo también termina si el jugador supera los 21 puntos.
    """
    global PL_hand

    mood = "ok"

    while mood != "not good":
        election = input(
            "Write HIT or STAND: "
        ).strip().upper()

        if election == "HIT":
            mood = user_play()

            # Termina el turno si el jugador supera 21.
            if mood == "not good":
                break

        elif election == "STAND":
            print(
                "Your hand:",
                PL_hand,
                "Total:",
                sum(PL_hand)
            )
            break

        else:
            # Se informa que la entrada no es válida.
            print("Please write HIT or STAND.")


# Este bloque ejecuta main() solamente cuando el archivo
# se abre directamente, no cuando se importa desde otro archivo.
if __name__ == "__main__":
    main()

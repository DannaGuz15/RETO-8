A = [2, 4, 5, 6, 7, 8, 9]
B = [10, 11, 12, 13, 14, 15, 16]


def mostrar_proceso(func):
    def wrapper(*args, **kwargs):
        print(f"\nEjecutando {func.__name__}...")
        resultado = func(*args, **kwargs)
        print(f"Finalizó {func.__name__}\n")
        return resultado
    return wrapper

def validar_listas(func):
    def wrapper(A, B, *args, **kwargs):
        if not A or not B:
            raise ValueError("Las listas A y B no pueden estar vacías.")
        return func(A, B, *args, **kwargs)
    return wrapper

@mostrar_proceso
@validar_listas
def suma_termino_a_termino(A, B):
    """Calcula la suma término a término de dos listas.

    Args:
        A: La primera lista.
        B: La segunda lista.

    Returns:
        Una tupla con las sumas de cada lista.
    """
    suma_A = sum(A)
    suma_B = sum(B)
    print(f"La suma de A es: {suma_A}")
    print(f"La suma de B es: {suma_B}")
    return suma_A, suma_B

@mostrar_proceso
@validar_listas
def suma_termino_a_termino_reverse(A, B):
    """Calcula la suma término a término de dos listas en orden inverso.

    Args:
        A: La primera lista.
        B: La segunda lista.

    Returns:
        Una tupla con las sumas de cada lista en orden inverso.
    """
    suma_A_reverse = sum(reversed(A))
    suma_B_reverse = sum(reversed(B))
    print(f"La suma de A en reversa es: {suma_A_reverse}")
    print(f"La suma de B en reversa es: {suma_B_reverse}")
    return suma_A_reverse, suma_B_reverse

@mostrar_proceso
@validar_listas
def multiplicar_por_escalar(A, B, n):
    """Multiplica cada elemento de dos listas por un escalar.

    Args:
        A: La primera lista.
        B: La segunda lista.
        n: El escalar.

    Returns:
        Dos nuevas listas con los resultados de la multiplicación.
    """
    C = [x * n for x in A]
    D = [x * n for x in B]
    print(f"A multiplicado por {n} es: {C}")
    print(f"B multiplicado por {n} es: {D}")
    return C, D

@mostrar_proceso
@validar_listas
def suma_matrices(A, B):
    """Suma dos listas elemento a elemento.

    Args:
        A: La primera lista.
        B: La segunda lista.

    Returns:
        Una nueva lista con la suma de los elementos correspondientes.
    """
    suma_AB = [x + y for x, y in zip(A, B)]
    print(f"La suma de A y B término a término es: {suma_AB}")
    return suma_AB

resultado_suma = suma_termino_a_termino(A, B)
print(resultado_suma)  # Imprime una tupla con las sumas

resultado_multiplicacion = multiplicar_por_escalar(A, B, 2)
print(resultado_multiplicacion)


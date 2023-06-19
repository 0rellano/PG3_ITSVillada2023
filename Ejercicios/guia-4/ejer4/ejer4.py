
def calculate_statistics(numbers: list) -> tuple[float, float]:
    n = len(numbers)
    media = sum(numbers) / n

    suma_diferencias_cuadrado = sum((x - media) ** 2 for x in numbers)
    desviacion_estandar = (suma_diferencias_cuadrado / n) ** 0.5

    return media, desviacion_estandar
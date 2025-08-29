import numpy as np
from sympy import primerange

# Geração de primos e gaps
N = 800000000
primes = list(primerange(2, N))
gap_sequence = [primes[i+1] - primes[i] for i in range(len(primes)-1)]

seen_gaps = set()
new_gap_indices = []
inconsistencies = set()  # o uso do set é para evitar duplicatas

# Derivadas discretas
diff = np.diff(gap_sequence)
second_diff = np.diff(diff)

# Pontos de estabilidade e inflexão
stable_points = set(np.where(diff == 0)[0])
inflection_points = set(np.where(second_diff < 0)[0] + 1)
inconsistence_points = set(np.where(second_diff >= 0)[0] + 1)

# Verificação dos novos gaps
for i in range(1, len(gap_sequence)-1):
    is_new_gap = gap_sequence[i] not in seen_gaps
    seen_gaps.add(gap_sequence[i])

    if is_new_gap:
        # Se estiver nos pontos válidos
        if i in stable_points or i in inflection_points:
            new_gap_indices.append(i)
        # Se estiver fora da regra
        if i in inconsistence_points:
            inconsistencies.add(i)

# Resultados
print("Quantidade de valores gerados:", N)
print("Quantidade total de primos gerados:", len(primes))
print("Novos gaps verificados:", len(new_gap_indices))
print("Inconsistências encontradas:", len(inconsistencies))

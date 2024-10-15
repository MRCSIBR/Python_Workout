import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definir la lista de números
numbers = [10, 25, 18, 7, 32]

# Funciones para data science

# 1. Encontrar el valor mínimo
def find_min_value(numbers):
    return min(numbers)

# 2. Encontrar el valor máximo
def find_max_value(numbers):
    return max(numbers)

# 3. Calcular la media
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# 4. Calcular la mediana
def calculate_median(numbers):
    numbers_sorted = sorted(numbers)
    n = len(numbers_sorted)
    if n % 2 == 0:
        median = (numbers_sorted[n//2 - 1] + numbers_sorted[n//2]) / 2
    else:
        median = numbers_sorted[n//2]
    return median

# 5. Calcular la mediana intercuartil
def calculate_interquartile(numbers):
    numbers_sorted = sorted(numbers)
    q1 = numbers_sorted[len(numbers_sorted)//4]
    q3 = numbers_sorted[3*len(numbers_sorted)//4]
    iqr = q3 - q1
    return q1, q3, iqr

# 6. Calcular la varianza
def calculate_variance(numbers):
    mean = calculate_average(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

# 7. Calcular la desviación estándar
def calculate_standard_deviation(numbers):
    return calculate_variance(numbers) ** 0.5

# 8. Crear un DataFrame
def create_dataframe(numbers):
    df = pd.DataFrame({'Numbers': numbers})
    return df

# 9. Graficar los números
def plot_numbers(numbers):
    plt.plot(numbers)
    plt.title('Números')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.show()

# 10. Mostrar información del DataFrame
def show_df_info(df):
    print(df.info())
    print(df.describe())

# Ejecutar las funciones
numbers = [10, 25, 18, 7, 32]

# 1. Encontrar el valor mínimo
min_value = find_min_value(numbers)
print(f"Minimum: {min_value}")

# 2. Encontrar el valor máximo
max_value = find_max_value(numbers)
print(f"Maximum: {max_value}")

# 3. Calcular la media
average = calculate_average(numbers)
print(f"Average: {average:.2f}")

# 4. Calcular la mediana
median = calculate_median(numbers)
print(f"Median: {median}")

# 5. Calcular la mediana intercuartil
q1, q3, iqr = calculate_interquartile(numbers)
print(f"Q1: {q1}, Q3: {q3}, IQR: {iqr}")

# 6. Calcular la varianza
variance = calculate_variance(numbers)
print(f"Varianza: {variance:.2f}")

# 7. Calcular la desviación estándar
std_dev = calculate_standard_deviation(numbers)
print(f"Desviación estándar: {std_dev:.2f}")

# 8. Crear un DataFrame
df = create_dataframe(numbers)
print(df)

# 9. Graficar los números
plot_numbers(numbers)

# 10. Mostrar información del DataFrame
show_df_info(df)

''' Output:
Minimum: 7
Maximum: 32
Average: 18.40
Median: 18
Q1: 10, Q3: 25, IQR: 15
Varianza: 85.84
Desviación estándar: 9.26
   Numbers
0       10
1       25
2       18
3        7
4       32
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 1 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   Numbers  5 non-null      int64
dtypes: int64(1)
memory usage: 172.0 bytes
None
         Numbers
count   5.000000
mean   18.400000
std    10.358571
min     7.000000
25%    10.000000
50%    18.000000
75%    25.000000
max    32.000000
'''


import pandas as pd
import matplotlib.pyplot as plt

## Oscar Flores NC 1389

# 1. Crear diccionario con datos de profesores
profesores_facultad = {
    'id_profesor': [301, 302, 303, 304, 305, 306],
    'nombre': ['Dr. Ramirez', 'Mtra. Sanchez', 'Dr. Flores', 'Mtro. Vargas', 'Dra. Mendoza', 'Mtro. Castro'],
    'departamento': ['Matematicas', 'Humanidades', 'Ciencias', 'Ingenieria', 'Ciencias', 'Humanidades'],
    'grado_academico': ['Doctorado', 'Maestria', 'Doctorado', 'Maestria', 'Doctorado', 'Maestria'],
    'anos_antiguedad': [15, 8, 20, 5, 12, 3],
    'materias_asignadas': [3, 2, 4, 2, 3, 2],
    'alumnos_totales': [120, 80, 150, 60, 110, 70],
    'salario_mensual': [35000, 25000, 40000, 22000, 32000, 20000],
    'publicaciones_ano': [2, 1, 4, 0, 3, 1],
    'tipo_contrato': ['Definitivo', 'Definitivo', 'Definitivo', 'Interino', 'Definitivo', 'Interino']
}

print("Analisis exploratorio de Datos EDA")
print("Exploratory Data Analysis por Oscar Flores NC 1389")
print("Crear un diccionario con 10 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(profesores_facultad)

print("\n--- TABLA ORIGINAL DE PROFESORES 1389 ---")
print(df)

# 3. Exportar los datos a CSV
print("-+-+-+- Convertir el DataFrame en archivo CSV 1389 -+-+-+-")

df.to_csv(
    'profesores_facultad_1389.csv',
    index=False,
    encoding='utf-8-sig'
)

print("\nArchivo CSV creado correctamente")

print("-+-+-+- Datos leidos desde csv 1389 -+-+-+-")

# 4. Leer el archivo CSV
df = pd.read_csv('profesores_facultad_1389.csv')

print("\n--- DATOS LEÍDOS DESDE CSV NC 1389 ---")
print(df)

print("-+-+-+- Análisis Exploratorio de Datos NC 1389 -+-+-+-")

# 5. Primeros y últimos registros
print("\n1. PRIMEROS REGISTROS (Head) 1389:")
print(df.head(3))

print("\n2. ÚLTIMOS REGISTROS (Tail) 1389:")
print(df.tail(2))

# 6. Dimensiones y estructura
print("-+-+-+- 6. Dimensiones y estructuras NC 1389 -+-+-+-")

print(df)

print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)

print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)

print("\n5. TIPOS DE DATOS:\n", df.dtypes)

print("\n6. INFORMACIÓN GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("\n7. ESTADÍSTICAS DESCRIPTIVAS:")
print(df.describe())

print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())

print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())

print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())

print("Departamentos únicos:", df['departamento'].unique())

# 8. Análisis específico
print(df)
print("------------------------------------------------------------")
print("Análisis específico")

print("\n11. PROFESORES POR DEPARTAMENTO:")
print(df['departamento'].value_counts())

print("\n12. PROMEDIO DE SALARIO: $", df['salario_mensual'].mean())

print("13. SALARIO MÁXIMO: $", df['salario_mensual'].max())

print("14. SALARIO MÍNIMO: $", df['salario_mensual'].min())

# 9. Ordenamiento, filtrado y agrupación
print("Ordenamiento, filtrado y agrupación")

print("\n15. PROFESORES ORDENADOS POR SALARIO (Mayor a menor):")
print(df.sort_values(by='salario_mensual', ascending=False))

print("\n16. PROFESORES CON SALARIO MAYOR A $25,000:")
filtro = df[df['salario_mensual'] > 25000]
print(filtro)

print("\n17. RESUMEN POR DEPARTAMENTO:")
resumen = df.groupby('departamento').agg(
    profesores=('id_profesor', 'count'),
    salario_promedio=('salario_mensual', 'mean'),
    salario_maximo=('salario_mensual', 'max')
)

print(resumen)

# 10. Gráfica de barras: Profesores por departamento
print("10. Gráfica de barras: Profesores por departamento")

conteo = df['departamento'].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Profesores por departamento Oscar Flores 1389')
plt.xlabel('Departamento')
plt.ylabel('Cantidad de profesores')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 11. Gráfica de barras: Salarios por profesor
print("11. Gráfica de barras: Salarios por profesor")

plt.figure(figsize=(8, 5))
plt.bar(df['nombre'], df['salario_mensual'], color='lightgreen')
plt.title('Salario mensual por profesor EDA Oscar 1389')
plt.xlabel('Profesor')
plt.ylabel('Salario en pesos')
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 12. Histograma: Distribución de antigüedad
print("12. Histograma: Distribución de antigüedad")

plt.figure(figsize=(8, 5))
plt.hist(df['anos_antiguedad'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de antigüedad de profesores EDA Oscar 1389')
plt.xlabel('Años de antigüedad')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 13. Gráfica de dispersión: Antigüedad vs Salario
plt.figure(figsize=(8, 5))
plt.scatter(df['anos_antiguedad'], df['salario_mensual'], color='red', s=100)
plt.title('Relación entre antigüedad y salario EDA Oscar 1389')
plt.xlabel('Años de antigüedad')
plt.ylabel('Salario mensual')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 14. Diagrama de caja: Distribución de salarios
plt.figure(figsize=(7, 5))
plt.boxplot(df['salario_mensual'], patch_artist=True,
            boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de salarios (Boxplot) EDA Oscar 1389')
plt.ylabel('Salario mensual')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 15. Matriz de correlación
correlacion = df.corr(numeric_only=True)

print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)),
           correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)),
           correlacion.columns)
plt.title('Matriz de correlación de variables numéricas EDA Oscar 1389')
plt.tight_layout()
plt.show()

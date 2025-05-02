# 1. Creación de Arrays
# np.array(): Crea un array a partir de una lista o secuencia.
# np.zeros(): Crea un array lleno de ceros.
# np.ones(): Crea un array lleno de unos.
# np.empty(): Crea un array sin inicializar (contiene valores aleatorios).
# np.full(): Crea un array lleno de un valor especificado.
# np.arange(): Crea un array con valores dentro de un rango especificado, similar a range.
# np.linspace(): Crea un array con un número específico de elementos igualmente espaciados entre dos valores.
# np.eye(): Crea una matriz identidad.
# np.random.rand(): Genera un array de números aleatorios entre 0 y 1.
# np.random.randint(): Genera un array de enteros aleatorios en un rango especificado.
# np.random.randn(): Genera un array de números aleatorios con distribución normal.


# 2. Operaciones Matemáticas y Estadísticas
# np.sum(): Suma los elementos de un array.
# np.mean(): Calcula la media de los elementos de un array.
# np.median(): Calcula la mediana de los elementos de un array.
# np.std(): Calcula la desviación estándar.
# np.var(): Calcula la varianza.
# np.min(): Encuentra el valor mínimo en un array.
# np.max(): Encuentra el valor máximo en un array.
# np.argmin(): Encuentra el índice del valor mínimo.
# np.argmax(): Encuentra el índice del valor máximo.
# np.prod(): Calcula el producto de los elementos de un array.
# np.cumsum(): Calcula la suma acumulada de los elementos.
# np.cumprod(): Calcula el producto acumulado de los elementos.
# np.dot(): Calcula el producto punto de dos arrays.
# np.cross(): Calcula el producto cruzado de dos arrays.
# np.sqrt(): Calcula la raíz cuadrada de cada elemento de un array.
# np.exp(): Calcula la exponencial de cada elemento de un array.
# np.log(): Calcula el logaritmo natural de cada elemento de un array.


# 3. Manipulación de Arrays
# np.reshape(): Cambia la forma de un array.
# np.transpose(): Transpone un array (invierte sus dimensiones).
# np.flatten(): Aplana un array multidimensional en un array unidimensional.
# np.concatenate(): Une dos o más arrays.
# np.hstack(): Apila arrays horizontalmente.
# np.vstack(): Apila arrays verticalmente.
# np.split(): Divide un array en varios sub-arrays.
# np.tile(): Repite un array.
# np.repeat(): Repite elementos de un array.
# np.flip(): Invierte el orden de los elementos en un array.
# np.roll(): Desplaza los elementos de un array a lo largo de un eje.


# 4. Indexación y Selección
# np.where(): Devuelve los índices que cumplen una condición.
# np.argwhere(): Devuelve las coordenadas de los elementos que cumplen una condición.
# np.take(): Toma elementos en posiciones específicas a lo largo de un eje.
# np.choose(): Construye un array desde varios arrays de acuerdo con índices dados.
# np.nonzero(): Devuelve los índices de los elementos distintos de cero.
# np.extract(): Extrae los elementos de un array que cumplen una condición.


# 5. Atributos de Arrays
# np.shape: Devuelve la forma (dimensiones) de un array.
# np.size: Devuelve el número total de elementos en un array.
# np.ndim: Devuelve el número de dimensiones de un array.
# np.dtype: Devuelve el tipo de datos de los elementos de un array.
# np.itemsize: Devuelve el tamaño (en bytes) de un solo elemento en el array.


# 6. Funciones Universales (ufuncs)
# np.add(): Suma elemento a elemento.
# np.subtract(): Resta elemento a elemento.
# np.multiply(): Multiplica elemento a elemento.
# np.divide(): Divide elemento a elemento.
# np.sin(), np.cos(), np.tan(): Funciones trigonométricas.
# np.power(): Eleva cada elemento de un array a la potencia de otro array o valor.


# 7. Álgebra Lineal
# np.linalg.inv(): Calcula la inversa de una matriz.
# np.linalg.det(): Calcula el determinante de una matriz.
# np.linalg.eig(): Calcula los valores y vectores propios de una matriz.
# np.linalg.svd(): Descomposición en valores singulares.
# np.linalg.norm(): Calcula la norma (magnitud) de un vector o matriz.
# np.linalg.solve(): Resuelve un sistema de ecuaciones lineales.


# 8. Manipulación de Matrices
# np.matmul(): Multiplicación de matrices.
# np.dot(): Producto punto o multiplicación de matrices.
# np.outer(): Producto exterior.
# np.inner(): Producto interior.
# np.kron(): Producto de Kronecker.

# 9. Aleatoriedad
# np.random.seed(): Establece la semilla para el generador de números aleatorios.
# np.random.shuffle(): Mezcla los elementos de un array en su lugar.
# np.random.choice(): Genera una muestra aleatoria de un array.


# 10. Funciones de Carga y Guardado de Datos
# np.save(): Guarda un array en un archivo binario .npy.
# np.load(): Carga un array desde un archivo .npy.
# np.savetxt(): Guarda un array en un archivo de texto.
# np.loadtxt(): Carga datos desde un archivo de texto.


# 1. Manipulación de Arrays
# np.diagonal(): Similar a np.diag, pero más flexible. Permite extraer diagonales no solo de la matriz principal, sino también de cualquier otra diagonal desplazada.
# np.tril(): Devuelve la parte triangular inferior de una matriz, poniendo a cero los elementos por encima de la diagonal.
# np.triu(): Devuelve la parte triangular superior de una matriz, poniendo a cero los elementos por debajo de la diagonal.
# np.flipud(): Invierte un array a lo largo del eje vertical (de arriba a abajo).
# np.fliplr(): Invierte un array a lo largo del eje horizontal (de izquierda a derecha).
# np.rot90(): Rota un array 90 grados en sentido antihorario.
# np.rollaxis(): Mueve el eje especificado a una nueva posición, y reordena los ejes de forma correspondiente.
# np.expand_dims(): Añade una nueva dimensión a un array en una posición especificada.
# np.squeeze(): Elimina dimensiones de tamaño 1 de un array.


# 2. Álgebra Lineal
# np.trace(): Calcula la suma de los elementos de la diagonal principal de una matriz.
# np.linalg.matrix_rank(): Calcula el rango de una matriz.
# np.linalg.qr(): Descomposición QR de una matriz.
# np.linalg.cholesky(): Descomposición de Cholesky de una matriz.
# np.linalg.solve(): Resuelve un sistema de ecuaciones lineales.
# np.linalg.lstsq(): Resuelve un sistema de ecuaciones lineales usando la aproximación de mínimos cuadrados.


# 3. Estadística y Funciones Probabilísticas
# np.percentile(): Calcula el percentil de los datos en un array.
# np.quantile(): Generalización de percentil que permite calcular cualquier cuantil.
# np.histogram(): Calcula el histograma de un conjunto de datos.
# np.bincount(): Cuenta la cantidad de veces que aparecen los números enteros en un array.


# 4. Manipulación de Tipos de Datos
# np.astype(): Cambia el tipo de datos de un array.
# np.view(): Crea una nueva vista del array con un tipo de datos diferente.
# np.copy(): Hace una copia del array.
# np.broadcast_to(): Transmite un array a una nueva forma según las reglas de transmisión de NumPy.


# 5. Funciones de Set y Ordenación
# np.unique(): Devuelve los elementos únicos de un array.
# np.sort(): Ordena un array.
# np.argsort(): Devuelve los índices que ordenarían un array.
# np.lexsort(): Realiza una ordenación indirecta utilizando una secuencia de claves.
# np.intersect1d(): Devuelve los elementos comunes en dos arrays.
# np.union1d(): Devuelve la unión de dos arrays.
# np.setdiff1d(): Devuelve la diferencia de conjuntos entre dos arrays.
# np.isin(): Comprueba si los elementos de un array están en otro array.


# 6. Funciones de Reducción
# np.all(): Comprueba si todos los elementos del array son verdaderos.
# np.any(): Comprueba si al menos un elemento del array es verdadero.
# np.count_nonzero(): Cuenta la cantidad de elementos no nulos en un array.


# 7. Funciones de Broadcast y Shape
# np.meshgrid(): Crea matrices de coordenadas a partir de coordenadas de vectores.
# np.ogrid: Crea matrices abiertas para el uso eficiente de las funciones de np.meshgrid.
# np.mgrid: Crea matrices llenas para el uso eficiente de las funciones de np.meshgrid.


# 8. Funciones Especiales
# np.logspace(): Crea un array con números espaciados logarítmicamente.
# np.geomspace(): Genera un array de números espaciados geométricamente.
# np.clip(): Limita los valores de un array a un rango especificado.
# np.piecewise(): Define un array basado en una función de piezas.


# 9. Entrada/Salida de Datos
# np.genfromtxt(): Carga datos desde un archivo de texto, con opciones para manejar datos faltantes y otros formatos de datos.
# np.recfromcsv(): Carga datos desde un archivo CSV en una matriz de registros (record array).
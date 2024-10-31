#lista de medidas y precios
#largo [1,2,3,4,5,6,7,8,9,10]
#precio [1,5,8,9,10,17,17,20,24,30]

#recurrencia = donde vamos a realizar los cortes

# r(n) = max(P(i) + r(n-i)) donde (1 <= i <= n)
# pasando la recurrencia a codigo

#--------PYTHON------------------------------------------------------
def cortar_var(tam_var, lista_p):
    if tam_var == 0:
        return 0
        
    mejor_valor = 0
    for i in range(1, tam_var + 1):
        valor = lista_p[i] + cortar_var(tam_var - i, lista_p)
        if valor > mejor_valor:
            mejor_valor = valor

    return mejor_valor
#--------PYTHON------------------------------------------------------

#--------JS------------------------------------------------------
function cortarVar(tamVar, listaP) {
  if (tamVar === 0) {
    return 0;
  }

  let mejorValor = 0;
  for (let i = 1; i <= tamVar; i++) {
    const valor = listaP[i] + cortarVar(tamVar - i, listaP);
    if (valor > mejorValor) {
      mejorValor = valor;
    }
  }

  return mejorValor;
}
#--------js------------------------------------------------------

    #calcula valor optimo con recursividad, pero el codigo no es muy optimo

# vamos a aplicar la memoizacion para acelerar el tiempo de ejecucion

#--------PYTHON------------------------------------------------------
def cortar_var(tam_var, lista_p, memory):
    if tam_var == 0:
        return 0
    if memory[tam_var] != -1:
        return memory[tam_var]

    mejor_valor = 0
    for i in range(1, tam_var + 1):
        valor = lista_p[i] + cortar_var(tam_var - i, lista_p)
        if valor > mejor_valor:
            mejor_valor = valor

    memory[tam_var] = mejor_valor
    return mejor_valor

if __name__ == "__main__":
    lista_p = [0,1,5,8,9,10,17,17,20,24,30]
    n = int(input())
    memo = [-1] * (n+1)
    print(cortar_var(n, lista_p, memo))
#--------PYTHON------------------------------------------------------

#--------js------------------------------------------------------
function cortarVar(tamVar, listaP, memory) {
  if (tamVar === 0) {
    return 0;
  }

  if (memory[tamVar] !== -1) {
    return memory[tamVar];
  }

  let mejorValor = 0;
  for (let i = 1; i <= tamVar; i++) {
    const valor = listaP[i] + cortarVar(tamVar - i, listaP, memory);
    mejorValor = Math.max(mejorValor, valor);
  }

  memory[tamVar] = mejorValor;
  return mejorValor;
}

// Ejemplo de uso:
const listaP = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30];
const n = parseInt(prompt("Ingrese el tamaño: "));
const memo = new Array(n + 1).fill(-1);
console.log(cortarVar(n, listaP, memo));
#--------js------------------------------------------------------

    #calcula cortes con el valor optimo, pero falta calcular cuales fueron los cortes

#entonces agregamos otra memoria 

#--------PYTHON------------------------------------------------------
def cortar_var(tam_var, lista_p, memory, camino):
    if tam_var == 0:
        return 0
    if memory[tam_var] != -1:
        return memory[tam_var]
    
    mejor_valor = 0
    mejor_corte = 0
    for i in range(1, tam_var + 1):
        precio = 0 if len(lista_p) <= i else lista_p[i]
        valor = precio + cortar_var(tam_var - i, lista_p, memory, camino)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_corte = i
    
    memory[tam_var] = mejor_valor
    camino[tam_var] = mejor_corte
    return mejor_valor
#--------PYTHON------------------------------------------------------

#--------js------------------------------------------------------
function cortarVar(tamVar, listaP, memory, camino) {
  if (tamVar === 0) {
    return 0;
  }

  if (memory[tamVar] !== -1) {
    return memory[tamVar];
  }

  let mejorValor = 0;
  let mejorCorte = 0;
  for (let i = 1; i <= tamVar; i++) {
    const precio = listaP[i] || 0; // Si i está fuera de rango, precio es 0
    const valor = precio + cortarVar(tamVar - i, listaP, memory, camino);
    if (valor > mejorValor) {
      mejorValor = valor;
      mejorCorte = i;
    }
  }

  memory[tamVar] = mejorValor;
  camino[tamVar] = mejorCorte;
  return mejorValor;
}
#--------js------------------------------------------------------

#creamos el arreglo y lo podriamos recorre de la siguiente manera

#--------PYTHON------------------------------------------------------
def print_solution(tam_var, camino):
    print("tamaño de varilla:")
    while tam_var > 0:
        print(camino[tam_var])
        tam_var = tam_var - camino[tam_var]

if __name__ == "__main__":
    lista_p = [0,1,5,8,9,10,17,17,20,24,30]
    n = int(input())
    memo = [-1] * (n+1)
    camino = [0] * (n+1)
    print (cortar_var(n, lista_p, memo, camino))
    print_solution(n, camino)
#--------PYTHON------------------------------------------------------

#--------js------------------------------------------------------
function printSolution(tamVar, camino) {
  console.log("Tamaño de varilla:");
  while (tamVar > 0) {
    console.log(camino[tamVar]);
    tamVar -= camino[tamVar];
  }
}

# Suponiendo que cortar_var ya está definida y funciona correctamente

# ... resto del código (lista_p, n, memo, etc.)

print(cortar_var(n, lista_p, memo, camino));
printSolution(n, camino);
#--------js------------------------------------------------------

// Datos de entrada
const numeros = [12, 5, 88, 3, 29];

// Funciones utilitarias
const obtenerMayor = arr => Math.max(...arr);
const obtenerMenor = arr => Math.min(...arr);

// Resultados
const mayor = obtenerMayor(numeros);
const menor = obtenerMenor(numeros);

// Mostrar resultados de forma elegante
console.log(`🔢 Números: [${numeros.join(', ')}]`);
console.log(`🔼 Mayor valor : ${mayor}`);
console.log(`🔽 Menor valor : ${menor}`);
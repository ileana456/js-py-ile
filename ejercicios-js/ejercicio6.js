// Genera un número aleatorio entre 1 y 10
const n = Math.floor(Math.random() * 10) + 1;

// Calcula el factorial de n
let factorial = 1;
for (let i = 2; i <= n; i++) {
  factorial *= i;
}

// Muestra el resultado con mejor formato
console.log(`🔢 El factorial de ${n} es: ${n}! = ${factorial}`);
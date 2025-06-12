const secreto = Math.floor(Math.random() * 100) + 1;
let intento;
let contador = 0;

console.log("🎯 ¡Adivina el número secreto entre 1 y 100!");

do {
  intento = Math.floor(Math.random() * 100) + 1;
  contador++;

  if (intento < secreto) {
    console.log(`🔻 ${intento} es menor que el número secreto ❌`);
  } else if (intento > secreto) {
    console.log(`🔺 ${intento} es mayor que el número secreto ❌`);
  }
} while (intento !== secreto);

console.log(`✅ ¡Correcto! El número era ${secreto}`);
console.log(`🔢 Total de intentos: ${contador}`);
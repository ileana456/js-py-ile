const palabras = [
  "Aceituna", "Murciélago", "Educación", "Aeropuerto", "Otorrinolaringólogo",
  "Euforia", "Aceite", "Paleontólogo", "Arquitectura", "Hipopótamo"
];

// Elegir una palabra aleatoria
const palabraAleatoria = palabras[Math.floor(Math.random() * palabras.length)];

// Definir conjunto de vocales (con tildes incluidas)
const vocalesValidas = new Set("aeiouáéíóú");

// Extraer vocales de la palabra (ignorando mayúsculas)
const vocalesEncontradas = Array.from(palabraAleatoria.toLowerCase())
  .filter(letra => vocalesValidas.has(letra));

// Mostrar resultados
console.log("🔤 Palabra seleccionada:", palabraAleatoria);
console.log("🟠 Vocales encontradas:", vocalesEncontradas.join(", "));
console.log("🔢 Total de vocales:", vocalesEncontradas.length);
// Lista de palabras
const palabras = ["Hola", "Python", "Javascript", "OpenAI", "Inteligencia"];

// Elige una palabra al azar
const palabra = palabras[Math.floor(Math.random() * palabras.length)];

// Invierte la palabra seleccionada
const invertir = (texto) => texto.split("").reverse().join("");
const inversa = invertir(palabra);

// Muestra el resultado con mejor formato
console.log(`🔄 ${palabra} → ${inversa}`);
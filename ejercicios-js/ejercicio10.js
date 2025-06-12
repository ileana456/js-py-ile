// Función para generar una contraseña segura
function generarContraseña(longitud = 16) {
  const caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  let resultado = "";
  for (let i = 0; i < longitud; i++) {
    const indice = Math.floor(Math.random() * caracteres.length);
    resultado += caracteres.charAt(indice);
  }
  return resultado;
}

// Longitud aleatoria entre 16 y 40
const longitud = Math.floor(Math.random() * (40 - 16 + 1)) + 16;
const contraseña = generarContraseña(longitud);

// Mostrar resultado con mejor formato
console.log("🔐 Contraseña generada:");
console.log(`📏 Longitud: ${longitud}`);
console.log(`🔑 Valor   : ${contraseña}`);
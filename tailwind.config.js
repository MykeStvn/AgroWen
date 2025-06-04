/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      './templates/**/*.html', // Escanea todos los archivos .html en tu carpeta de plantillas
      './**/templates/**/*.html', // Si tienes plantillas dentro de carpetas de apps
      // Agrega aquí cualquier otra ruta a archivos que contengan clases de Tailwind (ej. JavaScript)
    ],
    safelist: [
      "bg-[url('/static/img/banner-agro.jpg')]",
    ],
    theme: {
      extend: {},
    },
    plugins: [],
  }
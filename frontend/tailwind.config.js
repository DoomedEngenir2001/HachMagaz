// tailwind.config.js
module.exports = {
  content: ["./src/**/*.{vue,html,js}"],
    purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
    darkMode: false, // or 'media' or 'class'
    theme: {
      extend: {
        colors:{
          "phone-pastel": '#F3F3F7'
        }
      },
    },
    variants: {
      extend: {},
    },
    plugins: [],
  }
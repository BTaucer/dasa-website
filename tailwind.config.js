/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        merri: ["Merriweather", "serif"],
        cinzel: ["Cinzel", "serif"],
      },
      colors: {
        bg: "#f4f4f3",
        primary: "#000c23", // Dark blue
        primary_h: "#001437",
        secondary: "#9c8321", // zuta
        secondary_h: "#72621d", // tamno zuta
        green: "#1f8b4c",
        red: "rgb(255, 102, 102)",
        // Add more custom colors as needed
      },
      fontSize: {
        "4xl": "4rem", // Class name: 'text-7xl', Font size: 5rem
        "5xl": "5rem", // Class name: 'text-8xl', Font size: 6rem
        "6xl": "6rem", // Class name: 'text-8xl', Font size: 6rem
      },
    },
  },
  plugins: [],
};

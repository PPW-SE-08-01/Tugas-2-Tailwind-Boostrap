// Konfigurasi Tailwind (CDN). Dimuat setelah script cdn.tailwindcss.com
tailwind.config = {
  theme: {
    extend: {
      colors: {
        forest: "#2c3b2e",
        "forest-deep": "#1e2a20",
        paper: "#f1ead9",
        "paper-warm": "#eae1cb",
        clay: "#8b5e3c",
        rust: "#b4522f",
        olive: "#6b7a4f",
        ink: "#2a2420",
        "ink-soft": "#5b5348",
        line: "rgba(42, 36, 32, 0.14)",
      },
      fontFamily: {
        sans: ['"Work Sans"', "sans-serif"],
        display: ["Fraunces", "serif"],
        mono: ['"IBM Plex Mono"', "monospace"],
      },
    },
  },
};

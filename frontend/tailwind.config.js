/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f0f7ff',
          100: '#e0effe',
          500: '#0284c7',
          600: '#0369a1',
          700: '#075985',
          900: '#0c4a6e',
        },
        safety: {
          low: '#22c55e',      // Green - Low Risk
          medium: '#f59e0b',   // Amber - Medium Risk
          high: '#ef4444',     // Red - High Risk
          critical: '#991b1b', // Dark Red - Critical Alert
        },
      },
    },
  },
  plugins: [],
};

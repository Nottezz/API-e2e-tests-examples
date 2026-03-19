import { defineConfig } from 'allure';

export default defineConfig({
  name: 'API-e2e-tests',
  output: './allure-report',
  historyPath: './allure-history.jsonl',
  plugins: {
    timeline: true,
  },
});
import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    port: 53573,
    open: true
  },
  build: {
    outDir: 'build',
    assetsDir: 'assets'
  }
});
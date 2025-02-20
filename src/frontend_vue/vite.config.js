import { fileURLToPath, URL } from 'node:url'

import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

const isDevelopment = process.env.NODE_ENV === 'development'
const apiUrl = 'http://127.0.0.1:8000/'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueJsx(),
  ],
  base: './',
  server:{
    port: 3030,
    proxy:{
      '/api':{
        target: apiUrl,
        changeOrigin: true,
        rewrite: (path)=> path.replace(/^\/api/,''),
      },
    }
  }, 
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
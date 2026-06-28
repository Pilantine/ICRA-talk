import { defineConfig } from 'vite'
import path from 'path'

export default defineConfig({
  server: {
    fs: {
      allow: [
        path.resolve(__dirname, '.'),
        path.resolve(__dirname, 'public'),
        path.resolve(__dirname, 'components'),
      ]
    }
  }
})

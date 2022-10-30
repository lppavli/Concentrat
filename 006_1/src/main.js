import { createApp } from 'vue'
import App from './App.vue'
import TheHeader from './TheHeader'

const app = createApp(App)

// global
app.component('the-header', TheHeader)

app.mount('#app')

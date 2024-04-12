import {createApp} from "vue";
import App from './App'
import axios from "axios";
import router from './router'

axios.defaults.baseURL = 'http://localhost:8000' //http://127.0.0.1:8000

// createApp(App).mount('#app')
const app = createApp(App)

// app.use(createPinia())
app.use(router, axios)

app.mount('#app')
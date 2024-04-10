import { createRouter, createWebHistory } from 'vue-router'
import App from '../App.vue'
import Home from '@/views/Home.vue'
import AboutPage from '@/views/AboutPage.vue'


const router = createRouter({
  history: createWebHistory(), //import.meta.env.BASE_URL
  routes: [
    /* {
      path: '',
      name: 'App',
      component: App
    }, */
    {
      path: '',
      name: 'Home',
      component: Home
    },
    {
      path: '/about',
      name: 'About',
      component: AboutPage
    },
    
  ]
})

export default router
import { createRouter, createWebHistory } from 'vue-router'
import App from '../App.vue'
import Home from '@/views/Home.vue'
import AboutPage from '@/views/AboutPage.vue'
import All from '@/views/All.vue'
import Registration from '@/views/Registration.vue'



const router = createRouter({
  history: createWebHistory(), //import.meta.env.BASE_URL
  routes: [

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
    {
      path: '/all',
      name: 'All',
      component: All
    },
    {
      path: '/registration',
      name: 'Registration',
      component: Registration
    },
    
  ]
})

export default router
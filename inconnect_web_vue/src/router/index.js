import { createRouter, createWebHistory } from 'vue-router'

import Home from '@/views/Home.vue'
import AboutPage from '@/views/AboutPage.vue'
import Registration from '@/views/Registration.vue'
import LogIn from '@/views/LogIn.vue'
import All from '@/views/All.vue'
import CreateEvent from '@/views/CreateEvent.vue'

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
      path: '/register',
      name: 'Registration',
      component: Registration
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogIn
    },
    {
      path: '/createevent',
      name: 'CreateEvent',
      component: CreateEvent
    },

  ]
})

export default router
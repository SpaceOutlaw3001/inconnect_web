<!-- <template>
    <div>
        <p>
            Нет аккаунта? <RouterLink :to="{'name': 'Registration'}" >Нажмите здесь</RouterLink> для регистрации!
        </p>
        <form v-on:submit.prevent="submitForm">
            <div>
                <label>Логин</label><br>
                <input type="text" v-model="form.username" placeholder="логин">
            </div>

            <div>
                <label>Password</label><br>
                <input type="password" v-model="form.password" placeholder="введите пароль" >
            </div>

            <template v-if="errors.length > 0">
                <div>
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>
            </template>

            <div>
                <button>
                Log in
                </button>
            </div>
        </form>
    </div>
</template> -->

<template>
    <div class="registration">
      <div class="registration-container">
        <h2>Вход</h2>
        <form v-on:submit.prevent="submitForm">

        
        <div>
          <label>Введите логин</label>
          <input class="mail" type="text" v-model="form.username" placeholder="логин">
            
          <label>Введите пароль</label>
          <input class="password" type="password" v-model="form.password" placeholder="введите пароль" >
        </div>

        <div>
            <template v-if="errors.length > 0">
                <div>
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>
            </template>
        </div>
        

        <button class="register-button">Войти</button>

        </form>

        <hr>

        <!-- <Router-link to="/registration">
          <a class="register-back">Регистрация</a>
        </Router-link> -->
        <RouterLink :to="{'name': 'Registration'}" >
            <a class="register-back">Регистрация</a>
        </RouterLink> 

      </div>
    </div>
  </template>

<script>
import axios from 'axios'
/* axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.withCredentials = true */

import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    data() {
        return {
            form: {
                username: '',
                password: ''
            },
            errors: [],
        }
    },

    methods: {
        async submitForm() {
            this.errors = []
            console.log('submit')

            if (this.form.username === '') {
                this.errors.push('Укажите логин.')
            }

            if (this.form.password === '') {
                this.errors.push('Укажите пароль.')
            }

            if (this.errors.length === 0) {
                await axios
                    .post('/users/login/', this.form)
                    .then(response => {
                        this.userStore.setToken(response.data)

                        axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    })
                    .catch(error => {
                        console.log('error', error)

                        this.errors.push("Логин или пароль неверные! Или что-то другое пошло не так ¯|_(ツ)_/¯ ")
                    })
            }
            
            if (this.errors.length === 0) {
                await axios
                    .get('/users/me/')
                    .then(response => {
                        this.userStore.setUserInfo(response.data)
                        console.log('response.data:',response.data)

                        this.$router.push('/about')// /feed
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>

<style >
.register-back{
  text-decoration: none;
}
a{
  text-decoration: none;
}
</style>
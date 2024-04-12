<!-- <template>
    <div>
        <p>
            Already have an account? <RouterLink :to="{'name': 'LogIn'}" >Click here</RouterLink> to log in!
        </p>
        <form v-on:submit.prevent="submitForm">
            <div>
                <label>Логин</label><br>
                <input type="text" v-model="form.username" placeholder="логин">
            </div>

            <div>
                <label>E-mail</label><br>
                <input type="email" v-model="form.email" placeholder="e-mail">
            </div>

            <div>
                <label>Password</label><br>
                <input type="password" v-model="form.password1" placeholder="введите пароль" >
            </div>

            <div>
                <label>Repeat password</label><br>
                <input type="password" v-model="form.password2" placeholder="повторите пароль">
            </div>

            <div>
                <label>Имя</label><br>
                <input type="text" v-model="form.first_name" placeholder="имя">
            </div>

            <div>
                <label>Фамилия</label><br>
                <input type="text" v-model="form.last_name" placeholder="фамилия">
            </div>

            <template v-if="errors.length > 0">
                <div>
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>
            </template>

            <div>
                <button>
                Sign up
                </button>
            </div>
        </form>
    </div>
</template> -->

<template>
    <div class="registration">
      <div class="registration-container">
        <h2>Регистрация</h2>
        <form v-on:submit.prevent="submitForm">
            <div>
            <label>Введите почту</label>
            <input class="mail" type="email" v-model="form.email" placeholder="e-mail">

            <label>Введите логин</label>
            <input class="login" type="text" v-model="form.username" placeholder="логин">

            <label>Имя</label>
            <input class="name" type="text" v-model="form.first_name" placeholder="имя">

            <label>Фамилия</label>
            <input class="name" type="text" v-model="form.last_name" placeholder="фамилия">

            <div class="container-password">

                <div>
                <label>Введите пароль</label>
                <input class="password" 
                        type="password" 
                        v-model="form.password1" 
                        placeholder="введите пароль" >
                </div>

                <div>
                <label>Повторите пароль</label>
                <input class="password-verification" 
                        type="password" 
                        v-model="form.password2" 
                        placeholder="повторите пароль">
                </div>

            </div>
            </div>

            <div>
                <template v-if="errors.length > 0">
                    <div>
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
                </template>
            </div>
            <button class="register-button">Зарегистрироваться</button>
        </form>
        <hr>
        <Router-link :to="{'name': 'LogIn'}">
          <a class="register-back">Я уже зарегистрирован</a>
        </Router-link>
      </div>
    </div>
</template>

<script>
import axios from 'axios'
/* axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.withCredentials = true */

import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const toastStore = useToastStore()

        return {
            toastStore
        }
    },

    data() {
        return {
            form: {
                username: '',
                email: '',
                password1: '',
                password2: '',
                first_name: '',
                last_name: '',
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []
            console.log('submit')

            if (this.form.email === '') {
                this.errors.push('Укажите почту.')
            }

            if (this.form.first_name === '') {
                this.errors.push('Укажите имя.')
            }

            if (this.form.last_name === '') {
                this.errors.push('Укажите фамилию.')
            }

            if (this.form.password1 === '') {
                this.errors.push('Укажите имя.')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('Пароли не совпадают.')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/users/register/', this.form)
                    .then(response => {
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'Пользователь зарегистрирован. Войдите в аккаунт.')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            const data = JSON.parse(response.data.message)
                            for (const key in data){
                                this.errors.push(data[key][0].message)
                            }

                            this.toastStore.showToast(5000, 'Что-то пошло не так ¯|_(ツ)_/¯')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@100..900&family=Russo+One&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;

}
.registration{
  background: linear-gradient(139deg, #129bff 15.9%, #0702ff 100%);
  padding-top: 24px;
  padding-bottom: 24px;
}
h2 {
  color: #129bff;
  font-weight: 800;
  font-size: 36px;
  margin-bottom: 24px;
}
input {
  width: 100%;
  border:1px solid #129bff;
  padding: 12px 24px;
  border-radius: 20px;
  margin-top: 8px;
  margin-bottom: 24px;
  display: block;
  font: 500 20px "Raleway", sans-serif;
  text-align-all: center;
}
.registration-container {
  background-color: white;
  max-width: 540px;
  display: block;
  margin: auto;
  padding: 24px 60px;
  border-radius: 24px;
  font: 500 20px "Raleway", sans-serif;
}
.register-button {
  background-color: #129bff;
  color: white;
  padding: 17px 51px;
  border: none;
  border-radius: 24px;
  display: block;
  margin: auto;
  font: 500 20px "Raleway", sans-serif;
  cursor: pointer;
}
hr {
  margin-bottom: 24px;
  margin-top: 24px;
  border: 1px solid #129bff;
}
a.register-back:active,
a.register-back:hover,
a.register-back {
  display: block;
  text-align:center;
  text-decoration: none;
  color: black;
}
h2{
  display: block;
  text-align:center;
}
.container-password {
  display: flex;
  gap: 8px;
}
.container-password label {
  display: block;

}
label {
  margin-left: 10px;
}
.container-password input {
  width: 204px;
}

</style>
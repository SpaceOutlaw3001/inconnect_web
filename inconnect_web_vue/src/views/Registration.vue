<script>

</script>

<template>
<div class="registration">
  <div class="registration-container">
    <h2>Регистрация</h2>
    <div>
      <label>Введите почту</label>
      <input class="mail">
      <label>Введите логин</label>
      <input class="login">
      <label>Имя</label>
      <input class="name">
      <label>Фамилия</label>
      <input class="name">
      <div class="container-password">
        <div>
          <label>Введите пароль</label>
          <input class="password">
        </div>
        <div>
          <label>Повторите пароль</label>
          <input class="password-verification">
        </div>
      </div>
    </div>
    <button class="register-button">Зарегестрироваться</button>
    <hr>
    <a class="register-back" href="Login.vue">Я уже зарегистрирован</a>
  </div>
</div>
</template>

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
  //border-color: #129bff;
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
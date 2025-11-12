<script>
import mafia from '../img/mafia.jpg';
import { Icon } from "vue3-google-icon";
import image from '../img/bowling.jpg';

import axios from 'axios'
export default {
    name: 'EventView',

    components: {
    },

    data() {
        return {
            events: []
        }
    },

    mounted() {
        this.getEvents()
    },

    methods: {
      getEvents() {
            axios
                .get('/api/events')
                .then(response => {
                    console.log('data', response.data)

                    this.events = response.data.events //this.events = response.data
                    console.log('this.events', this.events)
                })
                .catch(error => {
                    console.log('error', error)
                })
        },
    }
}
</script>

<template>
  <head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet">
  </head>
  <body>
  <header id="header-section">
    <div class="container">
      <div class="header">
        <h1 class="header-logo">Inconect</h1>
        <div class="header-action">
          <button class="header-action__chat material-symbols-outlined md-32 nav-main__link_selected"><Icon type="chat"/></button>
          <button class="header-action__account_circle material-symbols-outlined md-32"><Icon type="account_circle"/></button>
        </div>
      </div>
    </div>
  </header>
  <main>
    
    <section id="profile-section">
      <div class ="container">
        <div class="container-profile">
          <div class="profile-avatar">
            <img src="@/img/avatar.jpg" alt="#">
          </div>
          <div class="about-me-info">
            <h3 class="name-info" style="font: 400 32px Raleway, sans-serif;">Саша</h3>
            <p class="about-me">Приятно, граждане, наблюдать, как представители современных социальных резервов и по сей день остаются уделом либералов, которые жаждут быть смешаны с не уникальными данными до степени совершенной неузнаваемости, из-за чего возрастает их статус бесполезности. Безусловно, реализация </p>
          </div>
        </div>
      </div>
    </section>

    <section id="active-events">
      <div class ="container">
        <h2>Активные события</h2>
        <ul class="active-events-list">
          <li class="active-event" v-for="event in events" :key="event.id">
            <div class="card-top">
              <a class="active-event-img" href="#">
                <img :src="event.img_url" alt="боулинг">
              </a>
              <div class="card-label-price">{{ event.price}}₽</div>
            </div>
            <div class="card-bottom">
              <h5 class="name-event">{{event.title}}</h5>
              <p class="tegs" v-for="tag in event.tags"> {{tag}}</p>
              <div class="date-place-time">
                <p class="date">{{event.date}}</p>
                <p class="time">{{event.time}}</p>
                <p class="place">{{event.place}}</p>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </section>

    <section id="favourites-events">
      <div class ="container">
        <h2>Избранное</h2>
        <ul class="active-events-list">
          <li class="active-event" v-for="event in events" :key="event.id">
            <div class="card-top">
              <a class="active-event-img" href="#">
                <img :src="event.img_url" alt="боулинг">
              </a>
              <div class="card-label-price">{{ event.price}}₽</div>
            </div>
            <div class="card-bottom">
              <h5 class="name-event">{{event.title}}</h5>
              <p class="tegs" v-for="tag in event.tags">{{tag}}</p>
              <div class="date-place-time">
                <p class="date">{{event.date}}</p>
                <p class="time">{{event.time}}</p>
                <p class="place">{{event.place}}</p>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </section>
  </main>
  </body> 
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@100..900&family=Russo+One&display=swap');

*{
  margin: 0;
  padding: 0;
  /*box-sizing: border-box;*/
}
body{
  color: #000000;
  font: 400 24px "Raleway", sans-serif;
  background-color: #ffffff;
}
.header-logo{
  color: #129BFF;
  font: 400 48px "Russo One", sans-serif;
}
ul li,
ol li{
  list-style-type: none;

}
button{
  display: block;
  border: none;
  color: inherit;
  font: inherit;
  background-color: transparent;
  transition: .4s;
  cursor: pointer;

}
.container{
  max-width: 1260px;
  margin: 0 auto;
  padding: 0 10px;
}
section{
  margin-top: 24px;
}
/* header*/
#header-section {
  padding: 16px 0;
}
.header,
.header-action {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.md-32 {
  font-size: 32px !important;
}
.nav-main__link_selected {
  color: #129BFF;
  cursor: default;
}
.header-action__account_circle:hover,
.header-action__chat:hover {
  color: #129BFF;
}

.header-action {
  gap: 24px;
}
/*about me*/
.profile-avatar {
  display: block;
  float: left;
  width: 200px;
  height: 200px;
  border-radius: 20px;
  background-color: #000000;
  overflow: hidden;
}
.profile-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.container-profile {
  display: block;

}
.about-me-info{
  display: grid;
  gap: 8px;
  /*margin-left: 640px;*/
  padding: 24px;
}
/*Активные события */
.card-top{
  position: relative;
  border-radius:20px ;
}

.active-event-img{
  display: block;
  width: 400px;
  height: 224px;
}
.active-event-img > img{
  width: 100%;
  height: 100%;
  /*object-fit: contain; !* Встраиваем картинку в контейнер card__image *!*/
  transition: 0.2s;
  border-radius:20px ;
}
.card-top:hover{
  box-shadow: 4px 8px 16px #A9DBFF;
}
.card-label-price {
  background-color: #129BFF;
  width: 99px;
  height: 38px;
  position: absolute;
  inset: auto auto 10px 279px;
  border-radius:20px ;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0;
  font-size:24px;
  font-weight: 600;
  color: white;
}

.card-bottom{
  display: grid;
  row-gap: 4px;
  margin-top:4px;
  margin-left: 4px;
}
.date-place-time{
  display: flex;
}

h2{
  font: 400 36px "Russo One", sans-serif;
}
.active-events-list{
  margin-top: 24px;
  display: block;
  gap: 30px;
  font: 400 18px "Raleway", sans-serif;
}
.active-event{
  display: inline-block;
  margin-left:7px;
  margin-bottom: 20px
}

section{
  margin-top: 24px;
}

.tegs {
  color: #585858;
}

h5{
  font: 600 24px "Raleway", sans-serif;
}

/*.circul{*/
/*    display: inline-block;*/
/*    width: 300px;*/
/*    height: 300px;*/
/*    border-radius: 50%;*/
/*    background-color: #000000;*/
/*    overflow: hidden;*/

/*}*/
/*.circul  img{*/
/*    width: 100%;*/
/*    height: 100%;*/
/*    object-fit: cover;*/
/*}*/
</style>
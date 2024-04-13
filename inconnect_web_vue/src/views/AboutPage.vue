<script>
import mafia from "../img/mafia.jpg";
import { Icon } from "vue3-google-icon";
import image from "../img/bowling.jpg";

import axios from "axios";
export default {
  name: "AboutPage",
  props: { event: Object },
  components: {Icon},

  data() {
    return {
      event: {
         id:1,
          title:'Мафия',
          tags:['#Тлен','#Всё','#Ура'],
          date:'22 апреля',
          time:'20:00',
          place:'Мира 5',
          price:'200',
          img_url:mafia,
          text:"xwertyhjbvcxa ertghjmnbvdsaer",
       },



    };
  },

  created() {
    // this.event.price = this.$route.params.data//.img_url
    // console.log('this.$route.params.data',this.$route.params.data)
  },

  mounted() {
    console.log('this.$route.params.event_id', this.$route.params.event_id)
    console.log('this.$route.params', this.$route.params)
    this.getEvents(this.$route.params.event_id);
  },

  methods: {
    getEvents(id) {
      axios
        .get("/api/event/"+id)
        .then((response) => {
          console.log("data", response.data);

          this.event = response.data//.event; //this.events = response.data
          console.log("this.event", this.event);
        })
        .catch((error) => {
          console.log("error", error);
        });
    },

  },
};
</script>

<template>
  <div>
    <head>
      <meta charset="UTF-8" />
      <title>Title</title>
      <link
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined"
        rel="stylesheet"
      />
    </head>
    <body>
      <main>
        <section id="event">
          <h1>{{ $route.params.event_price }}</h1>
          <div class="about-event-container">
            <div class="card-top">
              <a class="active-event-img" href="#">
                <img :src="event.img_url" alt="боулинг" />
              </a>
              
              <div class="conteiner-about-event">
                <div class="about-event">
                  <div class="price-name">
                    <h5 class="name-event">{{ event.title }}</h5>
                    <div class="price">
                      {{ event.price }}₽
                    </div>
                  </div>
                  <div class="tegs-list">
                    <div class="tegs" v-for="tag in event.tags" :key="tag.id"> {{tag}}</div>
                  </div>
                  <div class="date-place-time">
                    <p class="date">{{ event.date }}•</p>
                    <p class="time">{{ event.time }}•</p>
                    <p class="place">{{ event.place }}</p>
                  </div>
                  <button class="button-participate">
                    Участвовать
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div class="description">
            <label>
              О событии
            </label>
            <p class="description-text">Банальные, но неопровержимые выводы, а также базовые сценарии поведения пользователей неоднозначны и будут ассоциативно распределены по отраслям. Как принято считать, многие известные личности неоднозначны и будут в равной степени предоставлены сами себе. С другой стороны, начало повседневной работы по формированию позиции в значительной степени обусловливает важность вывода текущих активов. В своём стремлении улучшить пользовательский опыт мы упускаем, что сделанные на базе интернет-аналитики выводы смешаны с не уникальными .</p>
          </div>
        </section>
      </main>
    </body>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@100..900&family=Russo+One&display=swap");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.card-top {
  position: relative;
}

.active-event-img {
  display: block;
  width: 100%;
  height: 660px;
}
.active-event-img > img {
  width: 100%;
  height: 100%;
  transition: 0.2s;
  object-fit: cover;
}
.card-top:hover {
  box-shadow: 4px 8px 16px #a9dbff;
}
.conteiner-about-event {
  background: rgba(255, 255, 255, 0.29);
  backdrop-filter: blur(5px);
  width: 100%;
  height: 300px;
  position: absolute;
  inset: auto auto 0px auto;
  margin: 0;
  color: white;
  font: 400 24px "Raleway", sans-serif;
}
.about-event{
  margin-left: 330px;
  margin-top: 32px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.date-place-time {
  display: flex;
}

section {
/*  margin-top: 24px;*/
}

.tegs {
  color: #b8b8b8;
}

h5 {
  font: 400 48px "Russo One", sans-serif;
}
.price-name {
  display: flex;
  gap: 64px;
}
.tegs-list{
  display: flex;
}
.price {
  font: 600 24px "Raleway", sans-serif;
  background-color: #129bff;
  width: 99px;
  height: 38px;
  padding: 5px 19px;
  border-radius: 24px;
  margin-top: 10px;
}
.button-participate{
  background-color: #129bff;
  color: white;
  border: none;
  border-radius: 24px;
  display: block;
  width: 194px;
  padding: 16px 32px;
  margin-top: 16px;
  font: 500 20px "Raleway", sans-serif;
  cursor: pointer;
}
.description {
  font: 400 48px "Russo One", sans-serif;
  margin: 24px 330px;
}
.description-text{
  font: 500 20px "Raleway", sans-serif;
  margin-top: 24px;
  margin-right: 660px;
}
</style>

<script>
import mafia from "../img/mafia.jpg";
import { Icon } from "vue3-google-icon";
import image from "../img/bowling.jpg";
import AboutPage from '@/views/AboutPage.vue'
import Event from '@/components/Event.vue'
import axios from "axios";
import {useUserStore} from "@/stores/user";
export default {
  setup() {
        const userStore = useUserStore()

        return {
            userStore
          }
        },
  beforeCreate() {
        this.userStore.initStore()
    },
  name: "EventView",
  components: {Icon},

  data() {
    return {
      events: [{ id:1,
          name:'Мафия',
          tags:['#Развлечения','#18+'],
          date:'22 апреля',
          time:'20:00',
          place:'Мира 5',
          price:'200',
          img_url:mafia
        },],
      tags_person: [
        "Мемы", "Коты", "PS", "Dota", "Собаки", "Игры", "Один дома", "Еда", "Зал", "Одежда", "Животные", "Зал", "Dota", "Собаки",
      ],
      myevents: [{ id:1,
          name:'Мафия',
          tags:['#Развлечения','#18+'],
          date:'22 апреля',
          time:'20:00',
          place:'Мира 5',
          price:'200',
          img_url:mafia
        },],
    };
  },

  mounted() {
    this.getEvents();
    this.getMyEvents();
  },

  methods: {
    getEvents() {
      axios
        .get("/api/events/?users="+this.userStore.user.id)
        .then((response) => {
          console.log("data", response.data);
          console.log(JSON.stringify(this.userStore));
          this.events = response.data//.events; //this.events = response.data
          console.log("this.events", this.events);
        })
        .catch((error) => {
          console.log("error", error);
        });
    },
    getMyEvents() {
      axios
        .get("/api/events/?created_by="+this.userStore.user.id)
        .then((response) => {
          console.log("data", response.data);
          console.log(JSON.stringify(this.userStore));
          this.myevents = response.data//.events; //this.events = response.data
          console.log("this.events", this.myevents);
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
        <section id="profile-section">
          <div class ="container">
            <div class="container-profile">
              <div class="container-profile-avatar">
<!--                <div class="profile-avatar">-->
<!--                  <img src="@/img/avatar.jpg" alt="#">-->
<!--                </div>-->
                <div class="container-tags">
                  <div class="person-tag-list-container">
                    {{ this.userStore.user.username }}
                    <!--                    Саша, 24-->
                  </div>
                </div>
              </div>
              <RouterLink to="/createevent">
                <div class="button-create">
                  <a>Создать событие</a>
                </div>
              </RouterLink>
<!--              <div class="about-me-info">-->
<!--                <div class = "about-me-container">-->
<!--                  <div class= "my-tags" style="">#Мои#Теги</div>-->
<!--                  <div style="top: 77.50px;  border: 2px white solid"></div>-->
<!--                  <ul class="person-tags-list">-->
<!--                    <li class="tag-list" v-for="tag in tags_person">-->
<!--                      <div class = "person-tag-list-container">-->
<!--                        <div style="justify-content: center; align-items: center; gap: 40px; display: inline-flex">-->
<!--                          <div style="color: #129BFF; font-size: 20px;  font-weight: 400; word-wrap: break-word">{{tag}}</div>-->
<!--                        </div>-->
<!--                      </div>-->
<!--                    </li>-->
<!--                  </ul>-->
<!--                </div>-->
<!--              </div>-->
            </div>
          </div>
        </section>
        <section id="active-events">
          <div class="container">
            <h2>Мои подписки</h2>
            <ul class="active-events-list">
              <li class="active-event" v-for="event in events" :key="event.id">
                <div class="card-top">
                  <!-- <RouterLink to="/about">
                    <a class="active-event-img" href="#">
                      <img :src="event.img_url" alt="боулинг" />
                    </a>
                  </RouterLink> -->
                  <RouterLink :to="{name:'About', params: {event_id: event.id}}">
                    <a class="active-event-img" href="#">
                      <img :src="event.img_url" alt="боулинг" />
                    </a>
                  </RouterLink>
                 <!--  <div >
                    <a class="active-event-img" href="#">
                        <img :src="event.img_url" @click="shareData(event.price)" alt="боулинг" />
                    </a>
                  </div> -->
                  <div class="card-label-price">{{ event.price }}₽</div>
                </div>
                <div class="card-bottom">
                  <h5 class="name-event">{{ event.title }}</h5>
                  <div class="tegs-list">
                    <div class="tegs" v-for="tag in event.tags" :key="tag.id"> #{{tag}}</div>
                  </div>
                  <div class="date-place-time">
                    <p class="date">{{ event.date }}•</p>
                    <p class="time">{{ event.time }}•</p>
                    <p class="place">{{ event.place }}</p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </section>

        <section id="active-events">
          <div class="container">
            <h2>Созданные мной события</h2>
            <ul class="active-events-list">
              <li class="active-event" v-for="event in myevents" :key="event.id">
                <div class="card-top">
                  <RouterLink :to="{name:'About', params: {event_id: event.id}}">
                    <a class="active-event-img" href="#">
                      <img :src="event.img_url" alt="боулинг" />
                    </a>
                  </RouterLink>
                  <div class="card-label-price">{{ event.price }}₽</div>
                </div>
                <div class="card-bottom">
                  <h5 class="name-event">{{ event.title }}</h5>
                  <div class="tegs-list">
                    <div class="tegs" v-for="tag in event.tags" :key="tag.id"> #{{tag}}</div>
                  </div>
                  <div class="date-place-time">
                    <p class="date">{{ event.date }}•</p>
                    <p class="time">{{ event.time }}•</p>
                    <p class="place">{{ event.place }}</p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </section>

        <!-- <section id="active-events">
          <div class="container">
            <h2>Созданные мной события</h2>
            <ul class="active-events-list">
              <li class="active-event" v-for="event in myevents" :key="event.id">
                <div class="card-top">
                  <RouterLink to="/aboutpage">
                    <a class="active-event-img" href="#">
                      <img :src="event.img_url" alt="боулинг" />
                    </a>
                  </RouterLink>
                  <div class="card-label-price">{{ event.price }}₽</div>
                </div>
                <div class="card-bottom">
                  <h5 class="name-event">{{ event.title }}</h5>
                  <div class="tegs-list">
                    <div class="tegs" v-for="tag in event.tags" :key="tag.id"> #{{tag}}</div>
                  </div>
                  <div class="date-place-time">
                    <p class="date">{{ event.date }}•</p>
                    <p class="time">{{ event.time }}•</p>
                    <p class="place">{{ event.place }}</p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </section> -->
      </main>
    </body>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@100..900&family=Russo+One&display=swap");

* {
  margin: 0;
  padding: 0;
  /*box-sizing: border-box;*/
}
body {
  color: #000000;
  font: 400 24px "Raleway", sans-serif;
  background-color: #ffffff;
}

ul li,
ol li {
  list-style-type: none;
}
button {
  display: block;
  border: none;
  color: inherit;
  font: inherit;
  background-color: transparent;
  transition: 0.4s;
  cursor: pointer;
}
.container {
  max-width: 1260px;
  margin: 0 auto;
  padding: 0 10px;
}
section {
  margin-top: 24px;
}

/*about me*/
.container-profile-avatar {
  display: flex;
  flex-direction: column;
  width: 200px;
  height: 100px;
  //height: 432px;
  background-color: #129BFF;
  border-radius: 20px;
  align-items: center;
  padding-top: 16px;
  gap: 24px;
  color: #129BFF;
  font: 600 32px Raleway;

}
.profile-avatar {
  display: flex;
  /* float: left;*/
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
  display: flex;
  gap: 26px;
}

.my-tags {
  left: 409px;
  top: 30px;
  color: white;
  font: 400 32px Russo One;
  word-wrap: break-word;
  display: flex;
  justify-content: center;
  margin-bottom: 8px;
}
.about-me-container {
  max-width: 996px;
  background: #129BFF;
  border-radius: 24px;
  padding: 30px 26px;

}
.person-tags-list {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 26px;
}
.person-tag-list-container {
  height: 54px;
  padding: 2px 24px;
  background: white;
  box-shadow: 0px 9px 17px rgba(0, 0, 0, 0.10);
  border-radius: 36px;
  overflow: hidden;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 10px;
  display: inline-flex
}

/*Активные события */
.card-top {
  position: relative;
  border-radius: 20px;
}

.active-event-img {
  display: block;
  width: 400px;
  height: 224px;
}
.active-event-img > img {
  width: 100%;
  height: 100%;
  /*object-fit: contain; !* Встраиваем картинку в контейнер card__image *!*/
  transition: 0.2s;
  border-radius: 20px;
}
.card-top:hover {
  box-shadow: 4px 8px 16px #a9dbff;
}
.card-label-price {
  background-color: #129bff;
  width: 99px;
  height: 38px;
  position: absolute;
  inset: auto auto 10px 279px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0;
  font-size: 24px;
  font-weight: 600;
  color: white;
}

.card-bottom {
  display: grid;
  row-gap: 4px;
  margin-top: 4px;
  margin-left: 4px;
}
.date-place-time {
  display: flex;
}

h2 {
  font: 400 36px "Russo One", sans-serif;
}
.active-events-list {
  margin-top: 24px;
  display: block;
  gap: 30px;
  font: 400 18px "Raleway", sans-serif;
}
.active-event {
  display: inline-block;
  margin-left: 7px;
  margin-bottom: 20px;
}

section {
  margin-top: 24px;
}

.tegs {
  color: #585858;
}

h5 {
  font: 600 24px "Raleway", sans-serif;
}
.tegs-list{
  display: flex;
}
.button-create{
  background-color: #129bff;
  color: white;
  border: none;
  border-radius: 24px;
  display: block;
  width: 250px;
  padding: 16px 32px;
  margin: auto;
  font: 500 20px "Raleway", sans-serif;
  cursor: pointer;
}
</style>

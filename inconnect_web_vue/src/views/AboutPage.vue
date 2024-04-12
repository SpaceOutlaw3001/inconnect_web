<script>
import mafia from "../img/mafia.jpg";
import { Icon } from "vue3-google-icon";
import image from "../img/bowling.jpg";

import axios from "axios";
export default {
  name: "EventView",
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

  mounted() {
    this.getEvents();
  },

  methods: {
    getEvents() {
      axios
        .get("/api/event")
        .then((response) => {
          console.log("data", response.data);

          this.event = response.data;//.event; //this.events = response.data
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
          <div class ="container">


        <div style="width: 100%; height: 100%; position: relative; background: white">

            <div style="width: 1300px; height: 660px; left: 0px; top: 88px; background: #D7D7D7">
                <div style="left: 332px; top: 264px; position: absolute; color: black; font-size: 48px; font-family: Russo One; font-weight: 400; word-wrap: break-word">{{ event.title }}</div>
                <div style="left: 332px; top: 330px; position: absolute">
                  <p class="tegs" v-for="tag in event.tags" :key="tag.id">
                    {{ tag }}
                  </p>
                  <div style=" justify-content: center; align-items: center; gap: 8px; display: inline-flex">
                    <div style="color: black; font-size: 20px; font-family: Raleway; font-weight: 400; word-wrap: break-word">{{ event.date }}, {{ event.time }}</div>
                    <div style="width: 14px; height: 14px; position: relative">
                        <div style="width: 5.83px; height: 5.83px; left: 4.08px; top: 4.08px; position: absolute; background: black"></div>
                    </div>
                    <div style="color: black; font-size: 20px; font-family: Raleway; font-weight: 400; word-wrap: break-word">{{ event.place }}</div>

                </div>
                  <div style="padding-left: 19px; padding-right: 19px; padding-top: 5px; padding-bottom: 5px; background: #129BFF; border-radius: 24px ">
                    <div style="color: white; font-size: 24px; font-family: Raleway; font-weight: 600; word-wrap: break-word">Участвовать</div>
                  </div>
                </div>


                <div style="padding-left: 19px; padding-right: 19px; padding-top: 5px; padding-bottom: 5px; left: 566px; top: 271px; position: absolute; background: #129BFF; border-radius: 24px; overflow: hidden; flex-direction: column; justify-content: flex-start; align-items: flex-start; gap: 10px; display: inline-flex">
                    <div style="justify-content: flex-start; align-items: flex-start; gap: 7px; display: inline-flex">
                        <div style="color: white; font-size: 24px; font-family: Raleway; font-weight: 600; word-wrap: break-word">{{ event.price }}</div>
                        <div style="justify-content: flex-start; align-items: flex-start; gap: 6px; display: flex">
                            <div style="color: white; font-size: 24px; font-family: Raleway; font-weight: 600; word-wrap: break-word">₽</div>
                        </div>
                    </div>
                </div>
            </div>
            <div style="left: 330px; top: 865px; position: absolute; color: black; font-size: 48px; font-family: Russo One; font-weight: 400; word-wrap: break-word">О событии</div>
            <div style="width: 747px; left: 330px; top: 988px; position: absolute; color: black; font-size: 24px; font-family: Raleway; font-weight: 400; word-wrap: break-word">{{ event.text }}</div>
            <div style="width: 100px; height: 100px; left: 454px; top: 836px; position: absolute"></div>
        </div>
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


h2 {
  font: 400 36px "Russo One", sans-serif;
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


</style>

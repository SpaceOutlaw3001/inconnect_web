<script>
import axios from "axios";
import {useUserStore} from "@/stores/user";
export default {
  name: "CreateEvent",
  setup() {
        const userStore = useUserStore()

        return {
            userStore
          }
        },
  beforeCreate() {
        this.userStore.initStore()
    },

  data() {
    return {
      body: {
          title:'',
          text:'',
          place:'',
          date:'',
          time:'',
          price:0,
          image:1,
          chat_link: '',
          tags: ['nature'],
          created_by: parseInt(this.userStore.user.id)
       },
    };
  },


  mounted() {
  },

  methods: {
    CreateEvent() {
      console.log('this.body.created_by', this.body.created_by)
      console.log('type of created_by', typeof this.body.created_by)
      console.log('CreateEvent', this.body)

      axios
        .post("/api/events/", this.body
        /* {
          'body': this.body
        } */
      )
        .then(response => {
            console.log('data', response.data)

            this.$router.push('/about')
            this.body = ''
        })
        .catch(error => {
            console.log('error', error)
        })

    },

  },
};
</script>

<template>
  <div class="registration">
    <div class="registration-container">

      <form  v-on:submit.prevent="CreateEvent" method="post">
      <h2>Создать событие</h2>
      <div class="create-event-cont">
        
        <div class="create-event">
          <label>Название</label>
          <input class="mail" v-model="body.title">

          <label>Описание</label>
          <input class="mail" v-model="body.text">

          <label>Место</label>
          <textarea class="address" 
                    v-model="body.place"
                    name="address" 
                    rows="2" 
                    required>
          </textarea>

          <div class="data-time">
            <div>
              <label>Дата</label>
              <input type="date" 
                    v-model="body.date"
                    id="date" 
                    name="date" 
                    value="2024-12-12">
            </div>

            <div>
              <label>Время</label>
              <input type="time" 
                    v-model="body.time"
                    name="time" 
                    class="time">
            </div>
          </div>

          <!-- <label>Место</label>
          <input class="place"> -->
          <label>Цена</label>
          <input class="mail" v-model="body.price">

          <label>Чат</label>
          <input class="mail" v-model="body.chat_link">

          <label>Сылка на изображение</label>
          <input class="img-link" v-model="body.image">
        </div>
        <div class="create-tags">
          <!-- <div>
            <label>Теги</label>
            <input class="tags" v-model="body.tags">
          </div> -->
        </div>
      </div>

      <hr>
      <button class="register-button">Создать событие</button>
    </form>
    
    </div>
  </div>
</template>

<style scoped>
.create-event{
  display: block;
}
.registration-container {
  background-color: white;
  max-width: 860px;
  display: block;
  margin: auto;
  padding: 24px 60px;
  border-radius: 24px;
  font: 500 20px "Raleway", sans-serif;

}
label{
  display: block;
}
input{
  width: 408px;
}
textarea{
  width: 408px;
  border-radius: 24px;
  padding: 8px 24px;
  font: 500 20px "Raleway", sans-serif;
  border:1px solid #129bff;

}
.data-time{
  margin-top:30px;
  display: flex;
  gap:8px
}
.data-time input{
  width: 200px;
}

.create-event-cont{
  display: flex;
  gap: 64px;
}
</style>
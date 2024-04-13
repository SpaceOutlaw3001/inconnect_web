<script setup>

</script>

<template>
  <div class="registration">
    <div class="registration-container">
      <h2>Создать событие</h2>
      <div class="create-event-cont">
        <div class="create-event">
          <label>Название</label>
          <input class="mail">
          <label>Описание</label>
          <textarea class="address" name="address" rows="2" required>ул. Хвостенко, д. 1</textarea>
          <div class="data-time">
            <div>
              <label>Дата</label>
              <input type="date" id="date" name="date" value="2024-12-12">
            </div>
            <div>
              <label>Время</label>
              <input type="time" name="time" class="time">
            </div>
          </div>
          <label>Место</label>
          <input class="place">
          <label>Сылка на изображение</label>
          <input class="img-link">
        </div>
        <div class="create-tags">
          <div>
            <label>Теги</label>
            <input class="tags">
          </div>
        </div>
      </div>

      <hr>
      <button class="register-button">Создать событие</button>

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
  width: 320px;
}
textarea{
  width: 320px;
  border-radius: 24px;
  padding: 8px 24px;
  font: 500 20px "Raleway", sans-serif;
  border:1px solid #129bff;

}
.data-time{
  margin-top: 16px;
  display: flex;
  gap:8px
}
.data-time input{
  width: 150px;
}

.create-event-cont{
  display: flex;
  gap: 64px;
}
</style>
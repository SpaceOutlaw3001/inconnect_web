<script>
import { Icon } from "vue3-google-icon";
export default {
  components: {Icon},
};
</script>
<template>
      <header id="header-section">
        <div class="container">
          <div class="header">

            <RouterLink class="header-logo" to="/all">Inconnect</RouterLink>
            <div class="header-action">
              <RouterLink class="header-action__login material-symbols-outlined md-32"
                          to="/registration">
                <Icon type="login" />
              </RouterLink>
              <RouterLink class="header-action__account_circle material-symbols-outlined md-32"
                          to="/"
              ><Icon type="account_circle"  />
              </RouterLink>
            </div>
          </div>
        </div>
      </header>
<RouterView />
</template>
<script setup>
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@100..900&family=Russo+One&display=swap");


body {
  color: #000000;
  font: 400 24px "Raleway", sans-serif;
  background-color: #ffffff;
}
/* header*/
#header-section {
  padding: 16px 0;
}
.container {
  max-width: 1260px;
  margin: 0 auto;
  padding: 0 10px;
}
.header,
.header-action {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 24px;
}
.header-logo {
  color: #129bff;
  font: 400 48px "Russo One", sans-serif;
}


/* иконки*/
.header-action__login,
.header-action__account_circle
{
  color: #030303;
}
.header-action__account_circle:hover,
.header-action__login:hover {
  color: #129bff;
}


</style>

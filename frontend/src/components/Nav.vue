<template>
  <header>
    <nav class="navbar navbar-light bg-light">
        <h1>Показатели железорудного концентрата</h1>

      <p v-if="user" :key="user">
            <a class="btn btn-success" href="/add">Добавить показатель</a>
        </p>
      <p v-if="user" :key="user">
            <a class="btn btn-success" href="/report">Отчет по показателям</a>
        </p>
              <p v-if="!user" :key="user">
            <a class="btn btn-success" href="/login">Войти</a>
        </p>
      <p v-if="user" :key="user">
            <a class="btn btn-success" href="/logout">Выйти</a>
        </p>


    </nav>
</header>
<!--<materials></materials>-->
</template>

<script>

export default {
  name: 'Nav',
  data() {
    let isLoggedIn = localStorage.getItem('token') || ""
    if (isLoggedIn) {
    return {
      user: true,
    } } else return {user: false};
  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
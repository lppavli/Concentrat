<template>
  <header>
    <nav class="navbar navbar-light bg-light">
        <h1>Показатели железорудного концентрата</h1>
        <p v-if="!user">
            <a class="btn btn-success" href="/login">Войти</a>
        </p>
      <p v-if="user">
            <a class="btn btn-success" href="/logout">Выйти</a>
        </p>

        <a class="navbar-brand" href="#">Username</a>
    </nav>
</header>
<!--<materials></materials>-->
</template>

<script>

export default {
  name: 'Nav',
  data() {
    return {
      user: '',
    };
  },
  mounted() {
    if (localStorage.jwtToken) {
      this.user = localStorage.jwtToken
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
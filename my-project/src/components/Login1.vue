<template>
    <div class="container">
    <div class="row">
      <h5 class="display-5">Войти в личный кабинет</h5>
      <div class="text-danger font-weight-bold">

      </div>
      <div class="text-success font-weight-bold">

        </div>

    </div>


    <div class="row my-5">
      <form>
        <div class="mb-3">
          <label>Логин</label>
          <input v-model="login" type="text" required placeholder="Логин" class="form-control">
        </div>
        <div class="mb-3">
          <label>Пароль</label>
          <input v-model="password" type="password" required placeholder="Пароль" class="form-control">
        </div>
        <button @click="setLogin" type="submit" class="btn btn-primary">Войти</button>
      </form>
    </div>
      </div>

</template>


<script>
import $ from 'jquery'

export default {
  name: "Login",
  data() {
    return {
      login: '',
      password: ''
    }
  },
  methods: {
    setLogin() {
      $.ajax({
        type: "POST",
        url: 'http://localhost:8000/api/v1/login',
        crossDomain: true,
        dataType: 'jsonp',

        data: {
          username: this.login,
          password: this.password
        },
        success: (response) => {
          console.log(response)
        },
        error: (response) => {
          console.log(response)
        }
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

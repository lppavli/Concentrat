<template>
  <div>
  <div class="container text-dark mt-4">
    <div class="row justify-content-md-center">
      <div class="col-md-5 p-3 login justify-content-md-center">
        <h1 class="h3 mb-3 font-weight-normal text-center">Войти в аккаунт</h1>

        <p v-if="incorrectAuth" class="text-danger">Неправильный логин или пароль</p>
        <form v-on:submit.prevent="login">
          <div class="form-group">
            <label for="user">Логин</label>
            <input type="text" name="username" id="user" v-model="username" class="form-control">
          </div>
          <div class="form-group">
            <label for="pass">Пароль</label>
            <input type="password" name="password" id="pass" v-model="password" class="form-control">
          </div>
          <button type="submit" class="btn btn-lg btn-primary btn-block mt-2">Login</button>
        </form>

      </div>
    </div>
  </div>
  </div>
</template>

<script>
  export default {
    name: 'login',
    data () {
      let isLoggedIn = localStorage.getItem('token') || ""
      if (isLoggedIn)
        this.$router.push({ name: 'Materials' })
      return {
        username: '',
        password: '',
        incorrectAuth: false
      }
    },
    methods: {
      login () {
        this.$store.dispatch('userLogin', {
          username: this.username,
          password: this.password
        })
        .then(() => {
          localStorage.setItem('token', this.$store.state.accessToken)
          this.$router.push({ name: 'Materials' })
        })
        .catch(err => {
          console.log(err)
          this.incorrectAuth = true
        })
        }
      },
  }
</script>

<style scope>
  /*body {*/
  /*  background-color:#1f1f1f !important;*/
  /*}*/
  /*.login{*/
  /*  background-color:#2f2f2f;*/
  /*  margin-top:10%;*/
  /*  border-radius: 1% !important;*/
  /*}*/
  /*input {*/
  /*  padding: 25px 10px;*/
  /*}*/
  /*h1, label {*/
  /*  color: #fff;*/
  /*}*/
</style>
<template>
  <div>

    <form @submit.prevent="setLogin">
        <div class="form-group">
          <label>Логин</label>
          <input v-model="login" type="text" required placeholder="Логин" class="form-control">
        </div>
        <div class="form-group">
          <label>Пароль</label>
          <input v-model="password" type="password" required placeholder="Пароль" class="form-control">
        </div>
        <button type="submit" class="btn btn-primary">Войти</button>
      </form>
    </div>
</template>


<script>
import $ from 'jquery'
import axios from "axios";
import setAuthHeader from "@/utils/setAuthHeader";
export default {
  name: "Login",
  data() {
    return {
      login: '',
      password: '',
      isSuccess: false
    }
  },
  methods: {
    setLogin() {
      axios.post('http://localhost:8000/api/v1/login',
          {
            username: this.login,
            password: this.password
          },
      ).then(response => {
        localStorage.setItem('jwtToken', response.data.access_token)
        localStorage.setItem('activeUser', this.login)
        setAuthHeader(response.data.access_token)
        // this.isSuccess = true;
        console.log(response);
      });
    },

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

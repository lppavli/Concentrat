<template>
  <div>
    <div class="container text-dark mt-4">
      <div class="row justify-content-md-center">
        <div class="col-md-5 p-3 login justify-content-md-center">
          <h1 class="h3 mb-3 font-weight-normal text-center">Добавить
            показатель</h1>

          <p v-if="incorrectInp" class="text-danger">Войдите в систему</p>
          <form v-on:submit.prevent="add">
            <div class="form-group">
              <label >Название</label>
              <input type="text" name="name" v-model.trim="name"
                     class="form-control">
            </div>
            <div class="form-group">
              <label >Содержание железа</label>
              <input type="text" name="iron_amount" v-model="iron_amount"
                     class="form-control">
            </div>
            <div class="form-group">
              <label >Содержание Кремния</label>
              <input type="text" name="silicon_amount" v-model="silicon_amount"
                     class="form-control">
            </div>
            <div class="form-group">
              <label >Содержание Алюминия</label>
              <input type="text" name="aluminum_amount"
                     v-model="aluminum_amount" class="form-control">
            </div>
            <div class="form-group">
              <label >Содержание Натрия</label>
              <input type="text" name="sodium_amount" v-model="sodium_amount"
                     class="form-control">
            </div>
            <div class="form-group">
              <label>Содержание Серы</label>
              <input type="text" name="sulfur_amount" v-model="sulfur_amount"
                     class="form-control">
            </div>
            <div class="form-group">
            <select name="month" v-model="month">
              <option value="January">Январь</option>
              <option value="February">Февраль</option>
              <option value="March">Март</option>
              <option value="April">Апрель</option>
              <option value="May">Май</option>
              <option value="June">Июнь</option>
              <option value="July">Июль</option>
              <option value="August">Август</option>
              <option value="September">Сентябрь</option>
              <option value="October">Октябрь</option>
              <option value="November">Ноябрь</option>
              <option value="December">Декабрь</option>
            </select>
              </div>
            <button type="submit" class="btn btn-lg btn-primary btn-block mt-2">
              Добавить
            </button>
          </form>
<!--          <p v-if="incorrectInp" class="text-danger" v-if="addcorrect">Войдите в систему</p>-->
<a href="/" align="center">На главную</a>
        </div>
      </div>
    </div>

  </div>

</template>
<script>
import axios from 'axios';
export default {
  name: 'add',

  props: {
    name: {type: String, default: ''},
    iron_amount: {type: Number, default: 0},
    silicon_amount: {type: Number, default: 0},
    aluminum_amount: {type: Number, default: 0},
    sodium_amount: {type: Number, default: 0},
    sulfur_amount: {type: Number, default: 0},
    month: {type: String, default: 'January'},

  },
  data() {
    return {
      incorrectInp: false,
      addcorrect: false
    }
  },
  methods: {
    add() {
      let token = localStorage.getItem('token')

      const config = {
       headers: { Authorization: `Bearer ${token}` }
     };
    const bodyParameters = {
      "name": this.name,
      "iron_amount": Number(this.iron_amount),
      "silicon_amount": Number(this.silicon_amount),
      "aluminum_amount": Number(this.aluminum_amount),
      "sodium_amount": Number(this.sodium_amount),
      "sulfur_amount": Number(this.sulfur_amount),
      "month": this.month,
    };
    console.log(bodyParameters)
  axios.post(
  'http://localhost:8000/api/v1/materials',
  bodyParameters,
  config
).then(this.incorrectInp=false, this.addcorrect=true).catch(err => {
          console.log(err)
          this.incorrectInp = true
    this.addcorrect = false
        });
        }

      // let localStorageToken = localStorage.getItem('token')
      // console.log(localStorageToken)
      // console.log(axios)
      // const material = {
      //     name: this.name,
      //     iron_amount: this.iron_amount,
      //     silicon_amount: this.silicon_amount,
      //     aluminum_amount: this.aluminum_amount,
      //     sodium_amount: this.sodium_amount,
      //     sulfur_amount: this.sulfur_amount,
      //     month: this.month,
      //   }
      // const headers = {
      //   "Authorization": "Bearer " + localStorageToken,
      // }
      // axios.post("http://localhost:8000/api/v1/materials",
      //     material,
      //     headers).then(response => {
      //       console.log(response);
      // })

        }

}
</script>
<style scope></style>
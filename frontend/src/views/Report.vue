<template>
  <div>
    <div class="container text-dark mt-4">
      <div class="row justify-content-md-center">
        <div class="col-md-5 p-3 login justify-content-md-center">
          <form v-on:submit.prevent="get_report">
            <div class="form-group">
            <label>Выберите месяц</label>

            <select class="form-control" v-model="month">
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
        <div>
        <button type="submit" class="btn btn-lg btn-primary btn-block mt-2">
          Сформировать отчет
        </button>
        </div>
              </div>
        </form>
      </div>
    </div>
  </div>
  </div>
<main role="main" class="container" align="center">
 <div class="table_container" v-if="rep">
      <table class="my_table">
        <tr class="my_row">
          <td class="title" width="400px" bgcolor="#dddddd">Показатель</td>
          <td class="title" width="400px" bgcolor="#dddddd">Минимальное значение
          </td>
          <td class="title" width="400px" bgcolor="#dddddd" align="center">
            Максимальное значение
          </td>

        </tr>
        <tr v-for="row in row_data">
          <td class="ordinary" bgcolor="#eeeeff">{{ this.pok[row.value] }}</td>
    <td class="ordinary" bgcolor="#eeeeff">{{ row.min_value}}</td>
    <td class="ordinary" bgcolor="#eeeeff" align="center">{{row.max_value }}</td>
        </tr>
      </table>
 </div>
  <a href="/">На главную</a>
</main>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Report',

  props: {
    report_data: {
      type: Array,
      default: () => {
        return []
      }
    }
  },
  data() {
    return {
      month: '',
      row_data: [],
      rep: false,
      pok: {
        'iron_amount': 'Количество железа',
        'silicon_amount': 'Количество кремния',
        'aluminum_amount': 'Количество алюминия',
        'sodium_amount': 'Количество натрия',
        'sulfur_amount': 'Количество серы',
      }
    }
  },
  methods: {
    get_report() {
      axios.get(`http://localhost:8000/api/v1/materials/report?filter=${this.month}`
      ).then(response => {
        console.log("fetchAllPosts.response.data--->", this.row_data = response.data["Materials"])
        this.rep = true
      }).catch(err => {
        console.log(err)

      })
    }
  }
}
</script>
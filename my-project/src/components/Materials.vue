<template>
<v-table
  :materials_data="MATERIALS"
/>
</template>


<!--<template>-->
<!--  <main role="main" class="container">-->

<!--    <div class="table_container">-->
<!--      <table class="my_table">-->
<!--        <tr class="my_row">-->
<!--          <td class="title" width="400px" bgcolor="#dddddd">Название</td>-->
<!--          <td class="title" width="150px" bgcolor="#dddddd">Количество железа-->
<!--          </td>-->
<!--          <td class="title" width="100px" bgcolor="#dddddd" align="center">-->
<!--            Количество кремния-->
<!--          </td>-->
<!--          <td class="title" width="200px" bgcolor="#dddddd" align="center">-->
<!--            Количество алюминия-->
<!--          </td>-->
<!--          <td class="title" width="200px" bgcolor="#dddddd" align="center">-->
<!--            Количество натрия-->
<!--          </td>-->
<!--          <td class="title" width="100px" bgcolor="#dddddd" align="center">-->
<!--            Количество серы-->
<!--          </td>-->
<!--          <td class="title" width="100px" bgcolor="#dddddd" align="center">-->
<!--            Месяц-->
<!--          </td>-->
<!--        </tr>-->
        <!--        {% for mat in material_list %}-->
        <!--        <tr class="my_row">-->
        <!--            <td class="ordinary" bgcolor="#eeeeff">{{ mat.name }}</td>-->
        <!--            <td class="ordinary" bgcolor="#eeeeff">{{ mat.iron_amount }}</td>-->
        <!--            <td class="ordinary" bgcolor="#eeeeff" align="center">{{ mat.silicon_amount }}</td>-->
        <!--            <td class="ordinary" bgcolor="#eeeeff" align="center">{{ mat.aluminium_amount }}</td>-->
        <!--            <td class="ordinary" bgcolor="#eeeeff" align="center">{{ mat.sodium_amount }}</td>-->
        <!--            <td class="ordinary" bgcolor="#eeeeff" align="center">{{ mat.sulfur_amount}}</td>-->
        <!--            <td class="ordinary" bgcolor="#eeeeff" align="center">{{ mat.month }}</td>-->


        <!--        </tr>-->
        <!--        {% endfor %}-->
<!--      </table>-->
<!--    </div>-->
<!--    <br>-->
<!--    <div>{{info}}</div>-->
<!--  </main>-->
<!--</template>-->

<script>
import {mapActions, mapGetters} from 'vuex'
import axios from "axios";
import vTable from '@/components/vTable.vue'
export default {
  name: 'Materials',
  components: {
    vTable
  },
  data: () => {
    return {

    }
  },
  computed: {
    ...mapGetters([
        'MATERIALS'
    ])
  },
  methods: {
    ...mapActions([
        'GET_MATERIALS'
    ])
  },
  mounted() {
    this.GET_MATERIALS()
  }
//   data () {
//     return {
//       info: null
//     };
//   },
//   mounted() {
//     axios.get("http://localhost:8000/api/v1/materials").then(response => (this.info = response));
//   }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

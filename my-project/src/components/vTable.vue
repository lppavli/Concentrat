<template>
  <main role="main" class="container">

    <div class="table_container">
      <table class="my_table">
        <tr class="my_row">
          <td class="title" width="400px" bgcolor="#dddddd">Название</td>
          <td class="title" width="150px" bgcolor="#dddddd">Количество железа
          </td>
          <td class="title" width="100px" bgcolor="#dddddd" align="center">
            Количество кремния
          </td>
          <td class="title" width="200px" bgcolor="#dddddd" align="center">
            Количество алюминия
          </td>
          <td class="title" width="200px" bgcolor="#dddddd" align="center">
            Количество натрия
          </td>
          <td class="title" width="100px" bgcolor="#dddddd" align="center">
            Количество серы
          </td>
          <td class="title" width="100px" bgcolor="#dddddd" align="center">
            Месяц
          </td>
        </tr>
        <v-table-row
          v-for="row in paginatedMaterials"
          :key="row.id"
          :row_data="row"
        />
<!--                {% for mat in material_list %}-->

<!--                {% endfor %}-->
      </table>
    </div>
    <br>
    <div class="v-table__pagination">
    <div class="page" v-for="page in pages"
         :key="page"
         @click="pageClick(page)"
    >{{page}}</div>
    </div>
  </main>

</template>

<script>
import vTableRow from '@/components/vTableRow.vue'
export default {
  name: "v-table",
  components: {
    vTableRow
  },
  props: {
    materials_data: {
      type: Array,
      default: () => {
        return []
      }
    }
  },
  data() {
    return {
      materialsPerPage: 2,
      pageNumber: 1,
    }
  },
  computed: {
    pages() {
      return Math.ceil(this.materials_data.length / 2)
    },
    paginatedMaterials() {
      let from= (this.pageNumber - 1) * this.materialsPerPage;
      let to= from + this.materialsPerPage;
      return this.materials_data.slice(from, to);
    }
  },
  methods: {
    pageClick(page) {
      this.pageNumber = page;
    }
  }
}
</script>

<style scoped>
.v-table__pagination {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 30px;
}
.page {
  padding: 8px;
  border: 1px;
}
.page:hover {
  background: #9fcdff;
  cursor: pointer;
  color: #FFFFFF;
}
</style>
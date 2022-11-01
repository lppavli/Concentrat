<template>
  <tr class="my_row">
    <td class="ordinary" bgcolor="#eeeeff">{{ row_data.name }}</td>
    <td class="ordinary" bgcolor="#eeeeff">{{ row_data.iron_amount }}</td>
    <td class="ordinary" bgcolor="#eeeeff" align="center">{{
        row_data.silicon_amount
      }}
    </td>
    <td class="ordinary" bgcolor="#eeeeff" align="center">
      {{ row_data.aluminum_amount }}
    </td>
    <td class="ordinary" bgcolor="#eeeeff" align="center">{{
        row_data.sodium_amount
      }}
    </td>
    <td class="ordinary" bgcolor="#eeeeff" align="center">
      {{ row_data.sulfur_amount }}
    </td>
    <td class="ordinary" bgcolor="#eeeeff" align="center">{{ row_data.month }}</td>


  </tr>
</template>

<script>
export default {
  name: "v-table-row",
  props: {
    row_data: {
      type: Object,
      default: () => {
        return []
      }
    }
  },
  data() {
    return {}
  },
  computed: {}
}
</script>

<style scoped>

</style>
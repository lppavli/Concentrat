<template>

<main role="main" class="container">
  <select>
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
</main>
</template>

<script>

export default {
  name: 'Month',
  components: {
  },
  data: () => {
    return {}
  }}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
select {
  float: right;
}
</style>

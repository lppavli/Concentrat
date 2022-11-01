<template>
<v-table
  :materials_data="MATERIALS"
/>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import axios from "axios";
import vTable from '@/components/vTable.vue'
export default {
  name: 'Materials',
  components: {
    vTable
  },
  onIdle () {
      this.$store.dispatch('userLogout')
        .then(() => {
          this.$router.push({ name: 'Login' })
        })
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
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

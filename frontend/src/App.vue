<template>
  <Nav />
  <router-view/>
<!--  <materials></materials>-->
</template>

<style>
@import "assets/css/bootstrap.css";
</style>
<script>
import Nav from '@/components/Nav.vue'

export default {
  components: {Nav}
}
</script>

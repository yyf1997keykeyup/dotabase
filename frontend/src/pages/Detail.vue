<template>
  <main-layout>
    <p>detail</p>
    <div>{{$route.params.id}}</div>
    <div>{{ info }}</div>
  </main-layout>
</template>

<script>
  import MainLayout from '../layouts/Main.vue'
  import axios from 'axios';

  export default {
    data: function() {
      return {
        info: 'nothing'
      }
    },
    beforeCreate() {
      axios.get(`https://api.coindesk.com/v1/bpi/currentprice.json`)
      .then(response => {
        // JSON responses are automatically parsed.
        this.info = response.data
      })
      .catch(e => {
        this.errors.push(e)
      })
    },
    components: {
      MainLayout
    }
  }
</script>
<template>
  <main-layout>
    <h2>{{hero.name}}</h2>
    <img :src="hero.image_url" :alt="hero.name">
    <div>param: {{$route.params.id}}</div>
    <div>id: {{ hero.hero_id }}</div>
    <div>health: {{ hero.health }}</div>
    <div>damage: {{ hero.damage }}</div>
    <div>mana: {{ hero.mana }}</div>
    <div>bio: {{ hero.bio }}</div>
  </main-layout>
</template>

<script>
  import MainLayout from '../layouts/Main.vue'
  import axios from 'axios';

  const mockHeroData = require("../mock/hero_detail.json");

  export default {
    data: function() {
      return {
        hero: 'nothing'
      }
    },
    created() {
      this.hero = mockHeroData.data;
      console.log(this.hero);
      // axios.get(`https://api.coindesk.com/v1/bpi/currentprice.json`)
      // .then(response => {
      //   // JSON responses are automatically parsed.
      //   this.hero = response.data
      // })
      // .catch(e => {
      //   this.errors.push(e)
      // })
    },
    components: {
      MainLayout
    }
  }
</script>
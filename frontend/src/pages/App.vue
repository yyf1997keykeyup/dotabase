<template>
<main-layout>
  <div id="app" class="container my-5">
    <div class="row mb-3">
      <div class="col-md-9">
        <h1>Dotabase</h1>
      </div>
    </div>

    <div class="row">
      <Hero
        v-for="hero in heros"
        :key="hero.id"
        :id="hero.id"
        :name="hero.name"
        :image="hero.image"></Hero>
    </div>
  </div>
</main-layout>
</template>

<script>
import Hero from '../components/Hero';
import { mapState } from 'vuex'
import MainLayout from '../layouts/Main.vue'


export default {
  name: 'app',
  computed: mapState({
    heros: state => state.heros.all
  }),
  components: {
    Hero,
    MainLayout,
  },
};
</script>

<template>
  <main-layout>
    <div id="app" class="container my-5">
      <!-- <div class="row">
        <Hero
          v-for="hero in heros"
          :key="hero.hero_id"
          :id="hero.hero_id"
          :name="hero.name"
          :image="hero.image_url"></Hero>
      </div> -->
      <section id="portfolio" class="section portfolio-section">
            <div class="section-area">
                <div class="section-content">
                    <div class="container">
                        <div class="title-block mx-auto">
                            <div class="section_title mb-4 text-center">
                                <h2><span>All Heros!!!</span></h2>
                            </div>
                        </div>
                        <div class="portfolio-items row">
                          <Hero
                          v-for="hero in heros"
                          :key="hero.hero_id"
                          :id="hero.hero_id"
                          :name="hero.name"
                          :image="hero.image_url"></Hero>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
  </main-layout>
</template>

<script>
import Hero from '../components/Hero';
import { mapState } from 'vuex'
import MainLayout from '../layouts/Main.vue'
import axios from "axios";

const mockHerosData = require("../mock/heros.json");

export default {
    name: 'app',
      computed: mapState({
          // heros: state => state.heros.all
      }),
    data() {
      return {
        heros: [],
      };
    },
    created() {
        this.heros = mockHerosData.data;
        // axios.get(`https://api.coindesk.com/v1/bpi/currentprice.json`)
        // .then(response => {
        //     // JSON responses are automatically parsed.
        //     this.heros = response.data
        // })
        // .catch(e => {
        //     this.errors.push(e)
        // })
    },
    components: {
        Hero,
        MainLayout,
    },
};
</script>

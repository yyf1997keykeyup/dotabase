<template>
  <main-layout>
    <div id="app" class="container my-5">
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
                          :key="hero.heroid"
                          :id="hero.heroid"
                          :name="hero.name"
                          :image="hero.imageurl"></Hero>
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
      mock: state => state.debug.config.mock,
      getAllHeroApi: state => state.api.host + state.api.backend.operateHero,
    }),
    data() {
      return {
        heros: [],
        errors: [],
      };
    },
    created() {
      if (this.mock) {
        this.heros = mockHerosData.data;
      } else {
        var config = {
            useCredentails: true
        };
        axios.get(this.getAllHeroApi, config)
        .then(response => {
            // JSON responses are automatically parsed.
            this.heros = response
        })
        .catch(e => {
            this.errors.push(e)
        })
      } 
    },
    components: {
        Hero,
        MainLayout,
    },
};
</script>

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
                        <div class="position-relative">
                            <label> Hero Search... </label>
                            <input v-model="searchName" name="searchName" id="searchName" type="text" placeholder="Search for your hero..." required>
                        </div>
                        <div class="row">
                            <ul id="portfolio-filter" class="portfolio-filter filters">
                              <router-link :to="{name: 'hero_logs'}"> 
                                <li class="button-border list-inline-item">
                                    <a class="pill-button">All Hero Logs</a>
                                </li>
                                </router-link>
                                <li class="button-border list-inline-item">
                                    <a @click="exportAllHerosRequest" class="pill-button">Export All Heros</a>
                                </li>
                                <router-link :to="{name: 'hero_create'}"> 
                                    <li class="button-border list-inline-item">
                                        <a class="pill-button">Create a New Hero</a>
                                    </li>
                                </router-link>
                                <router-link :to="{name: 'hero_good_against'}"> 
                                    <li class="button-border list-inline-item">
                                        <a class="pill-button">Good Against List</a>
                                    </li>
                                </router-link>
                            </ul>
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
import Hero from '../../components/Hero';
import { mapState } from 'vuex'
import MainLayout from '../../layouts/Main.vue'
import axios from "axios";
import FileSaver from 'file-saver'


const mockHerosData = require("../../mock/heros.json");

export default {
    name: 'app',
    computed: mapState({
      mock: state => state.debug.config.mock,
      token: state => state.login.user.token,
      getAllHeroApi: state => state.api.host + state.api.backend.operateHero,
    }),
    data() {
      return {
        searchName: "",
        heros: [],
        errors: [],
        allHeros: []
      };
    },
    watch: {
      searchName: function (val) {
        if (val === "") {
          this.heros = this.allHeros
        } else {
          this.heros = []
          for (var i=0; i<this.allHeros.length; i++) {
            var name = this.allItems[i].itemname.toLowerCase()
            if (name.indexOf(val) > -1) {
              this.heros.push(this.allHeros[i])
            }
          }
        }
      }
    },
    created() {
      if (this.mock) {
        this.heros = mockHerosData.data;
        this.allHeros = mockHerosData.data;
      } else {
        var config = {
            useCredentails: true
        };
        // axios.get(this.getAllHeroApi, config)
        axios({  
          method: 'GET', 
          url: this.getAllHeroApi, 
          headers: {Authorization: this.token},
          data: { config } 
        })
        .then(response => {
          this.heros = response.data
          this.allHeros = response.data
        }, error => {
            if (error.response.status === 401) {
              if (error.response.data.detail != "Authentication credentials were not provided.") {
                alert("Timeout! Please Login!")
                this.$store.commit('login/logoutRequest')
                this.$router.push({name: "login"})
              } else {
                // alert("You don't have the authorization!")
                // this.$router.push({name: "homepage"})
              }
            }
        })
      } 
    },
    methods: {
        exportAllHerosRequest(evt) {
            const data = JSON.stringify(this.heros)
            const blob = new Blob([data], {type: ''})
            FileSaver.saveAs(blob, 'AllHeros.json')
        }
    },
    components: {
        Hero,
        MainLayout,
    },
};
</script>

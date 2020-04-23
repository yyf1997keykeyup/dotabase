<template>
  <main-layout>
    <div id="app" class="container my-5">
      <section id="portfolio" class="section portfolio-section">
            <div class="section-area">
                <div class="section-content">
                    <div class="container">
                        <div class="title-block mx-auto">
                            <div class="section_title mb-4 text-center">
                                <h2><span>All BestAgainst!!!</span></h2>
                            </div>
                        </div>
                        <div class="position-relative">
                            <label> GoodAgainst Search... </label>
                            <input v-model="searchName" name="searchName" id="searchName" type="text" placeholder="Search for your hero..." required>
                        </div>
                        <div class="row">
                            <ul id="portfolio-filter" class="portfolio-filter filters">
                                <li class="button-border list-inline-item">
                                    <a @click="exportAllRelationsRequest" class="pill-button">Export All Good Against Relationship</a >
                                </li>
                                <router-link :to="{name: 'hero_create'}"> 
                                    <li class="button-border list-inline-item">
                                        <a class="pill-button">Create a New Hero Good Against</a >
                                    </li>
                                </router-link>
                            </ul>
                        </div>
                        <div class="portfolio-items row">
                          <Hero
                          v-for="hero in herosLeft"
                          :key="hero.heroid"
                          :id="hero.heroid"
                          :name="hero.name"
                          :image="hero.imageurl"></Hero>
                          <Hero
                          v-for="hero in herosRight"
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


export default {
    name: 'hero_good_against',
    computed: mapState({
      mock: state => state.debug.config.mock,
      token: state => state.login.user.token,
      getAllHeroApi: state => state.api.host + state.api.backend.operateHero,
      getAllGoodAgainstApi: state => state.api.host + state.api.backend.operateHeroGoodAgainst
    }),
    data() {
      return {
        searchName: "",
        relations: [],
        errors: [],
        herosLeft: [],
        herosRight: [],
        allHeros: [],
        allRelations: [],
      };
    },
    watch: {
      searchName: function (val) {
        if (val === "") {
          this.relations = this.allRelations
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
        var config = {
            useCredentails: true
        };
        axios.all([
          axios({  
          method: 'GET', 
          url: this.getAllHeroApi, 
          headers: {Authorization: this.token},
          data: { config } 
        }),axios({  
            method: 'GET', 
            url: this.getAllGoodAgainstApi, 
            headers: {Authorization: this.token},
            data: { config } 
          })
        ]).then(axios.spread((heroRes,relationRes) => {
          this.allHeros = heroRes.data
          this.relations = relationRes.data
          this.allRelations = relationRes.data
          for(var i = 0; i < this.relations.length; i++) {
            this.herosLeft.push(this.allHeros[parseInt(this.relations[i].heroid_1)-1])
            this.herosRight.push(this.allHeros[parseInt(this.relations[i].heroid_2)-1])
            // alert(JSON.stringify(this.herosLeft))
            // alert(JSON.stringify(this.herosRight))
          }
        })).catch((error) => {
          if (error.response.status === 401) {
              if (error.response.data.detail === "Authentication credentials were not provided.") {
                alert("Timeout! Please Login!")
                this.$store.commit('login/logoutRequest')
                this.$router.push({name: "login"})
              } else {
                alert("You don't have the authorization!")
                this.$router.push({name: "homepage"})
              }
            }
        })
    },
    methods: {
        exportAllRelationsRequest(evt) {
            const data = JSON.stringify(this.allRelations)
            const blob = new Blob([data], {type: ''})
            FileSaver.saveAs(blob, 'AllGoodAgainst.json')
        }
    },
    components: {
        Hero,
        MainLayout,
    },
};
</script>
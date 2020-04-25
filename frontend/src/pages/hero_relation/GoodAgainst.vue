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
                        <table>
                          <tr>
                            <th>Hero</th>
                            <th>Good Against</th>
                          </tr>
                          <tr v-for="(goodAgainstIds, sourseId, index) in goodAgainstList" :key="index">
                            <th style="width:200px">
                              <div class="portfolio-items row">
                                <Hero
                                  class="col-lg-12"
                                  :key="sourseId"
                                  :id="sourseId"
                                  :name="id2heros[sourseId].name"
                                  :image="id2heros[sourseId].imageurl"/>
                                  <!-- <router-link :to="{name: 'hero_detail', params: {'heroid': sourseId}}">
                                    <a style="font-size:35px">{{id2heros[sourseId].name}}</a>
                                  </router-link> -->
                              </div>
                            </th>
                            <th>
                              <div  class="portfolio-items row">
                                <Hero 
                                  class="col-lg-3"
                                  v-for="gaId in goodAgainstIds"
                                  :key="gaId"
                                  :id="gaId"
                                  :name="id2heros[gaId].name"
                                  :image="id2heros[gaId].imageurl"/>
                              </div>
                            </th>
                          </tr>
                        </table>
                        <!-- <div class="portfolio-items row"> -->
                          <!-- <Hero
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
                          :image="hero.imageurl"></Hero> -->
                        <!-- </div> -->
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
        id2heros: {},
        // allRelations: [],
        goodAgainstList: {},
        allGoodAgainstList: {},
      };
    },
    watch: {
      searchName: function (val) {
        if (val === "") {
          this.goodAgainstList = this.allGoodAgainstList
        } else {
          this.goodAgainstList = {}
          for (var gaKey in this.allGoodAgainstList) {
            var name = this.id2heros[parseInt(gaKey)].name.toLowerCase()
            if (name.indexOf(val) > -1) {
              this.goodAgainstList[gaKey] = this.allGoodAgainstList[gaKey]
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
          var tempId2heros = {}
          for (var i = 0; i < this.allHeros.length; i++) {
            tempId2heros[this.allHeros[i].heroid] = JSON.parse(JSON.stringify(this.allHeros[i]))
          }
          this.id2heros = tempId2heros

          this.relations = relationRes.data
          // this.allRelations = relationRes.data
          var VarGoodAgainstList = {}
          for(var i = 0; i < this.relations.length; i++) {
            // this.herosLeft.push(this.allHeros[parseInt(this.relations[i].heroid_1)-1])
            // this.herosRight.push(this.allHeros[parseInt(this.relations[i].heroid_2)-1])
            // alert(JSON.stringify(this.herosLeft))
            // alert(JSON.stringify(this.herosRight))
            // var herosLeft = this.allHeros[parseInt(this.relations[i].heroid_1)-1]
            // var herosRight = this.allHeros[parseInt(this.relations[i].heroid_2)-1]
            if (!VarGoodAgainstList.hasOwnProperty(this.relations[i].heroid_1)) {
              VarGoodAgainstList[this.relations[i].heroid_1] = []
            }
            VarGoodAgainstList[this.relations[i].heroid_1].push(this.relations[i].heroid_2)
          }
          this.goodAgainstList = VarGoodAgainstList
          this.allGoodAgainstList = VarGoodAgainstList
        })).catch((error) => {
          if (error.response.status === 401) {
              if (error.response.data.detail != "Authentication credentials were not provided.") {
                alert("Timeout! Please Login!")
                this.$store.commit('login/logoutRequest')
                this.$router.push({name: "login"})
              } else {
                alert("You don't have the authorization!")
                // this.$router.push({name: "homepage"})
              }
            }
        })
    },
    methods: {
        exportAllRelationsRequest(evt) {
            const data = JSON.stringify(this.goodAgainstList)
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

<style>
    table {
        border-collapse: collapse;
        width: 100%;
    }

    td, th {
        border: 1px solid #dddddd;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #dddddd;
    }
</style>
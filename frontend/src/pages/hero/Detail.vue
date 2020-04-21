<template>
  <main-layout>
    <section class="section bg-light line-vector" id="aboutus">
            <div class="section-area">
                <div class="section-content">
                    <div class="container">
                        <div class="title-block mx-auto">
                            <div class="section_title mb-4 text-center">
                                <h2><span>{{hero.name}}</span></h2>
                                <p class="section_subtitle mx-auto">{{hero.type}}</p>
                            </div>
                        </div>
                        <div class="row">
                            <ul id="portfolio-filter" class="portfolio-filter filters">
                                <li class="button-border list-inline-item">
                                    <a @click="exportRequest" class="pill-button">Export</a>
                                </li>
                                <router-link :to="{name: 'hero_update', params: {'heroid': hero.heroid}}"> 
                                    <li class="button-border list-inline-item">
                                        <a class="pill-button">Update</a>
                                    </li>
                                </router-link>
                                <li class="button-border list-inline-item">
                                    <a @click="deleteRequest" class="pill-button">Delete</a>
                                </li>
                            </ul>
                        </div>
                        <div class="row align-items-center">
                                <div class="about-img-box">
                                    <div class="image">
                                        <img :src="hero.imageurl" class="img-fluid" alt="">
                                    </div>
                                </div>
                                <div class="col-md-2 col-sm-12">
                                  <div class="about-img-box">
                                    <div class="image">
                                        <img src="https://www.dotafire.com/images/skill/abaddon-mist-coil.png" class="img-fluid" alt="">
                                        example skill 1
                                    </div>
                                  </div>
                                </div>
                                <div class="col-md-2 col-sm-12">
                                  <div class="about-img-box">
                                    <div class="image">
                                        <img src="https://www.dotafire.com/images/skill/abaddon-aphotic-shield.png" class="img-fluid" alt="">
                                        example skill 2
                                    </div>
                                  </div>
                                </div>
                                <div class="col-md-2 col-sm-12">
                                  <div class="about-img-box">
                                    <div class="image">
                                        <img src="https://www.dotafire.com/images/skill/abaddon-curse-of-avernus.png" class="img-fluid" alt="">
                                        example skill 3
                                    </div>
                                  </div>
                                </div>
                                <div class="col-md-2 col-sm-12">
                                  <div class="about-img-box">
                                    <div class="image">
                                        <img src="https://www.dotafire.com/images/skill/abaddon-borrowed-time.png" class="img-fluid" alt="">
                                        example skill 4
                                    </div>
                                  </div>
                                </div>
                        </div>

                        <div class="row">
                            <div class="col-lg-4 col-6">
                                <div class="counter-block">
                                    <span class="mdi mdi-fire"></span>
                                    <div class="details">
                                        <h3 class="mb-0 mt-0 number"><em class="count">{{ hero.attr_health }}</em></h3>
                                        <p class="mb-0">health</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-6">
                                <div class="counter-block">
                                    <span class="mdi mdi-coffee-outline"></span>
                                    <div class="details">
                                        <h3 class="mb-0 mt-0 number"><em class="count">{{ hero.attr_mana }}</em></h3>
                                        <p class="mb-0">mana</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-6">
                                <div class="counter-block">
                                    <span class="mdi mdi-account-multiple-outline"></span>
                                    <div class="details">
                                        <h3 class="mb-0 mt-0 number"><em class="count">{{ hero.attr_damage }}</em></h3>
                                        <p class="mb-0">damage</p>
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                            <div class="col-lg-4 col-md-6">
                                <div class="expert-box text-center">
                                    <img src="http://www.peis.in/templates/halman/images/aboutus/01.svg" class="img-fluid" alt="" />
                                    <h3>Best Against</h3>
                                    <p class="mb-0">hahahaha hahah hahahhaa hahahha hahhaha</p>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6">
                                <div class="expert-box text-center">
                                    <img src="http://www.peis.in/templates/halman/images/aboutus/02.svg" class="img-fluid" alt="" />
                                    <h3>Bad Against</h3>
                                    <p class="mb-0">hahahaha hahah hahahh ahahah haha hhaha</p>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6">
                                <div class="expert-box text-center">
                                    <img src="http://www.peis.in/templates/halman/images/aboutus/03.svg" class="img-fluid" alt="" />
                                    <h3>Best Combo</h3>
                                    <p class="mb-0">haha hahahahah hahahha ahah ahh ahah haha</p>
                                </div>
                            </div>
                        </div>
                            <div class="col-md-12 col-sm-12">
                                <div class="about-text-block">
                                    <div class="about-content">
                                        <h4>
                                            Bio
                                        </h4>
                                        <div class="text">{{ hero.bio }} </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-12 col-sm-12">
                                <div class="about-text-block">
                                    <div class="about-content">
                                        <h4>
                                            Modify Logging
                                        </h4>
                                        <ul>
                                            <li v-for="log in logs" :key="log.logid">
                                                Health: {{ log.attr_heath }}; Mana: {{ log.attr_mana }}; Damage: {{ log.attr_damage }}; Create Time: {{ log.create_time }}
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
  </main-layout>
</template>

<script>
  import MainLayout from '../../layouts/Main.vue'
  import { mapState } from 'vuex'
  import axios from 'axios'
  import FileSaver from 'file-saver'

  const mockHeroData = require("../../mock/hero_detail.json");
  const mockHeroLogData = require("../../mock/hero_log.json");

  export default {
    computed: mapState({
      mock: state => state.debug.config.mock,
      operateHeroApi: state => state.api.host + state.api.backend.operateHero,
      getLogByHeroIdApi: state => state.api.host + state.api.backend.getLogByHeroId
    }),
    data: function() {
      return {
        hero: {},
        logs: [],
        errors: [],
      }
    },
    created() {
        if (this.mock) {
            this.hero = mockHeroData.data;
            this.logs = mockHeroLogData.data;
        } else {
            var config = {
                useCredentails: true
            };
            // get hero info
            axios.get(this.operateHeroApi + this.$route.params.heroid + "/", config)
            .then(response => {
                this.hero = response.data
            })
            .catch(e => {
                this.errors.push(e)
            })
            // get hero log info
            axios.get(this.getLogByHeroIdApi + "/" + this.$route.params.heroid + "/", config)
            .then(response => {
                this.logs = response.data
            })
            .catch(e => {
                this.errors.push(e)
            })
        }
    },
    methods: {
        deleteRequest(evt) {
            var r=confirm("Are you sure to delete the hero?");
            if (r==true)
            {
                if (!this.mock) {
                    var config = {
                        useCredentails: true
                    };
                    axios.delete(this.operateHeroApi + this.hero.heroid + "/", config)
                    .then(response => {
                        this.hero = response.data
                        this.$router.push({name: "homepage"})
                    })
                    .catch(e => {
                        this.errors.push(e)
                    })
                } else {
                    this.$router.push({name: "homepage"})
                }
                }
        },
        exportRequest(evt) {
            const data = JSON.stringify(this.hero)
            const blob = new Blob([data], {type: ''})
            FileSaver.saveAs(blob, "Hero_" + this.hero.name + '.json')
        }
    },
    components: {
      MainLayout
    }
  }
</script>
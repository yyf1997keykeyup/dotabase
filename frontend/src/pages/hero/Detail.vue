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
                            <div v-for="skill in skills" :key="skill.skillid">
                                <div class="col-md-3 col-sm-6">
                                <div class="about-img-box">
                                    <div class="image">
                                        <img :src="skill.imageurl" style="width:90px" :title="skill.info">
                                    </div>
                                </div>
                                </div>
                                <div class="section_title mb-4 text-center"> {{skill.skillname}}</div>

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
                            <!-- <div class="row">
                                <div class="col-lg-4 col-md-6">
                                    <div class="expert-box text-center">
                                        <img src="https://www.dotafire.com/images/hero/icon/sven.png" class="img-fluid" alt="" />
                                        <h3>Best Against</h3>
                                        <p class="mb-0">hahahaha hahah hahahhaa hahahha hahhaha</p>
                                    </div>
                                </div>
                                <div class="col-lg-4 col-md-6">
                                    <div class="expert-box text-center">
                                        <img src="https://www.dotafire.com/images/hero/icon/anti-mage.png" class="img-fluid" alt="" />
                                        <h3>Bad Against</h3>
                                        <p class="mb-0">hahahaha hahah hahahh ahahah haha hhaha</p>
                                    </div>
                                </div>
                                <div class="col-lg-4 col-md-6">
                                    <div class="expert-box text-center">
                                        <img src="https://www.dotafire.com/images/hero/icon/phantom-assassin.png" class="img-fluid" alt="" />
                                        <h3>Best Combo</h3>
                                        <p class="mb-0">haha hahahahah hahahha ahah ahh ahah haha</p>
                                    </div>
                                </div>
                            </div> -->
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
                                        <table style="position:absolute; left:30px">
                                            <tr>
                                                <th>Health</th>
                                                <th>Mana</th>
                                                <th>Damage</th>
                                                <th>Modify Time</th>
                                            </tr>
                                            <tr v-for="log in logs" :key="log.logid">
                                                <th>{{log.attr_health}}</th>
                                                <th>{{log.attr_maga}}</th>
                                                <th>{{log.attr_damage}}</th>
                                                <th>{{log.create_time}}</th>
                                            </tr>
                                        </table>
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
    const mockHeroSkillData = require("../../mock/hero_skill.json");
    const mockHeroLogData = require("../../mock/hero_log.json");

  export default {
    computed: mapState({
      mock: state => state.debug.config.mock,
      token: state => state.login.user.token,
      operateSkillApi: state => state.api.host + state.api.backend.operateSkill,
      operateHeroApi: state => state.api.host + state.api.backend.operateHero,
      getLogByHeroIdApi: state => state.api.host + state.api.backend.getLogByHeroId,
      getSkillByHeroIdApi: state => state.api.host + state.api.backend.getSkillByHeroId,
      getGoodAgainstApi: state => state.api.host + state.api.backend.operateHeroGoodAgainst,

    }),
    data: function() {
      return {
        hero: {},
        skills: [],
        skillId: [],
        logs: [],
        errors: [],
      }
    },
    created() {
        if (this.mock) {
            this.hero = mockHeroData.data
            this.skills= mockHeroSkillData.data
            this.logs = mockHeroLogData.data
        } else {
            var config = {
                useCredentails: true
            };
            // get hero info
            axios({  
                method: 'GET', 
                url: this.operateHeroApi + this.$route.params.heroid + "/", 
                headers: {Authorization: this.token}, 
                data: { config } 
            }).then(response => {
                this.hero = response.data
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
            // get hero skill info
            axios({  
                method: 'GET', 
                url: this.getSkillByHeroIdApi + "?heroid=" + this.$route.params.heroid,
                headers: {Authorization: this.token}, 
            })
            .then(response => {
                var params = []
                for(var i = 0; i < response.data.length; i++) {
                    this.skillId.push(response.data[i].skillid)
                    // alert(this.operateSkillApi)
                    params.push(axios({
                        method: 'GET', 
                        url: this.operateSkillApi + "?skillid=" + response.data[i].skillid,
                        headers: {Authorization: this.token}
                    }))
                }
                axios.all(params)
                    .then(axios.spread((...args) => {
                        for(var i = 0; i < args.length;i++) {
                            this.skills.push(args[i].data[0])
                        }
                        alert(JSON.stringify(this.skills))
                    }))
                    .catch((error) => {
                        console.log(error)
                        if (error.response.status != 401) {
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
            }, error => {
                if (error.response.status != 401) {
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
            // get hero log info
            axios({  
                method: 'GET', 
                url: this.getLogByHeroIdApi + "?hero=" + this.$route.params.heroid,
                headers: {Authorization: this.token}, 
            })
            .then(response => {
                this.logs = response.data
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
        deleteRequest(evt) {
            var r=confirm("Are you sure to delete the hero?");
            if (r==true)
            {
                if (!this.mock) {
                    var config = {
                        useCredentails: true
                    };
                    // axios.delete(this.operateHeroApi + this.hero.heroid + "/", config)
                    axios({  
                        method: 'DELETE', 
                        url: this.operateHeroApi + this.hero.heroid + "/",
                        headers: {Authorization: this.token}, 
                        data: { config }
                    })
                    .then(response => {
                        this.hero = response.data
                        this.$router.push({name: "homepage"})
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

<style>
    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #dddddd;
    }
</style>
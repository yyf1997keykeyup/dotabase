<template>
<main-layout>
    <div class="container">
    <div class="row align-items-center">
        <div class="col-md-12 order-2 order-md-1">
            <div class="p-4 contact-box rounded form-box">
                <h4 class="m-0">Update a new version!</h4>
                                    <div class="custom-form">
                                        <div id="message"></div>
                                        <a>
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group position-relative">
                                                        <label> Name </label>
                                                        <input v-model="hero.name" name="name" id="name" type="text" class="form-control pl-5" placeholder="Name" required>
                                                    </div>
                                                </div><!--end col-->
                                                <div class="col-md-6">
                                                    <div class="form-group position-relative">
                                                        <label> Type </label>
                                                        <input v-model="hero.type" name="type" id="type" type="text" class="form-control pl-5" placeholder="Type" required>
                                                    </div>
                                                </div><!--end col-->
                                                <div class="col-md-3">
                                                    <div class="form-group position-relative">
                                                        <label> Health </label>
                                                        <input v-model="hero.attr_health" name="health" id="health" type="text" class="form-control pl-5" placeholder="Health">
                                                    </div>
                                                </div><!--end col-->
                                                <div class="col-md-3">
                                                    <div class="form-group position-relative">
                                                        <label> Mana </label>
                                                        <input v-model="hero.attr_mana" name="mana" id="mana" type="text" class="form-control pl-5" placeholder="Mana">
                                                    </div>
                                                </div><!--end col-->
                                                <div class="col-md-3">
                                                    <div class="form-group position-relative">
                                                        <label> Damage </label>
                                                        <input v-model="hero.attr_damage" name="damage" id="damage" type="text" class="form-control pl-5" placeholder="Damage">
                                                    </div>
                                                </div><!--end col-->
                                                <div class="col-md-12">
                                                    <div class="form-group position-relative">
                                                        <label> Image Url </label>
                                                        <input v-model="hero.imageurl" name="image" id="image" type="text" class="form-control pl-5" placeholder="Image Url">
                                                    </div>
                                                </div><!--end col-->
                                                <div class="col-md-12">
                                                    <div class="form-group position-relative">
                                                        <div class="image">
                                                            <img :src="hero.imageurl" class="img-fluid" alt="">
                                                        </div>
                                                    </div>
                                                </div><!--end col-->
                                                <div class="col-md-12">
                                                    <div class="form-group position-relative">
                                                        <label>Bio</label>
                                                        <textarea v-model="hero.bio" name="comments" id="comments" rows="4" class="form-control pl-5" placeholder="The Bio..."></textarea>
                                                    </div>
                                                </div>
                                            </div><!--end row-->
                                            <div class="row">
                                                <div class="col-sm-12 text-center">
                                                    <a @click="updateRequest">
                                                        <button name="send" class="btn btn-hover send-btn btn-block">UPDATE</button>
                                                    </a>
                                                    <div id="simple-msg"></div>
                                                </div><!--end col-->
                                            </div><!--end row-->
                                        </a><!--end form-->
                                    </div><!--end custom-form-->
                                </div>
                            </div><!--end col-->
                            <div class="col-md-6 order-1 order-md-2">
                                <div class="contact-img">
                                    <img src="images/contact/contact-vector.png" class="img-fluid " alt="">
                                </div>
                            </div><!--end col-->
                        </div>
                        </div>
                        </main-layout>
</template>

<script>
  import MainLayout from '../../layouts/Main.vue'
  import axios from 'axios';
  import { mapState } from 'vuex'

  const mockHeroData = require("../../mock/hero_detail.json");

  export default {
    computed: mapState({
      mock: state => state.debug.config.mock,
      token: state => state.login.user.token,
      operateHeroApi: state => state.api.host + state.api.backend.operateHero,
    }),
    data: function() {
      return {
        hero: {},
        errors: [],
      }
    },
    created() {
        if (this.mock) {
            this.hero = mockHeroData.data;
        } else {
            var config = {
                useCredentails: true
            };
            // axios.get(this.operateHeroApi + this.$route.params.heroid + `/`, config)
            axios({  
                method: 'GET', 
                url: this.operateHeroApi + this.$route.params.heroid + `/`, 
                headers: {Authorization: this.token}, 
                data: { config } 
            })
            .then(response => {
                this.hero = response.data
            }, error => {
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
        }
    },
    methods: {
        updateRequest(evt) {
            if (!this.mock) {
                // axios.put(this.operateHeroApi + this.hero.heroid + `/`, this.hero)
                var hero = this.hero
                axios({  
                    method: 'PUT', 
                    url: this.operateHeroApi + this.hero.heroid + `/`, 
                    headers: {Authorization: this.token}, 
                    data: hero
                })
                .then(response => {
                    this.hero = response.data
                    alert("succeed to update!")
                    this.$router.push({name: "hero_detail", param: {heroid: this.hero.heroid}})
                }, error => {
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
            } else {
                alert("succeed to update!")
                this.$router.push({name: "hero_detail", param: {heroid: this.hero.heroid}})
            }
        }
    },
    components: {
      MainLayout
    }
  }
</script>
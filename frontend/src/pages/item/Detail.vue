<template>
  <main-layout>
    <section class="section bg-light line-vector" id="aboutus">
            <div class="section-area">
                <div class="section-content">
                    <div class="container">
                        <div class="title-block mx-auto">
                            <div class="section_title mb-4 text-center">
                                <h2><span>{{item.item_name}}</span></h2>
                                <p class="section_subtitle mx-auto">{{item.category}}</p>
                            </div>
                        </div>
                        <div class="row">
                            <ul id="portfolio-filter" class="portfolio-filter filters">
                                <li class="button-border list-inline-item">
                                    <a @click="exportRequest" class="pill-button">Export</a>
                                </li>
                                <!-- <router-link :to="{name: 'item_update', params: {'item_id': item.item_id}}">  -->
                                    <li class="button-border list-inline-item">
                                        <a class="pill-button">Update</a>
                                    </li>
                                <!-- </router-link> -->
                                <li class="button-border list-inline-item">
                                    <a @click="deleteRequest" class="pill-button">Delete</a>
                                </li>
                            </ul>
                        </div>
                        <div class="image">
                            <img :src="item.img_url" class="img-fluid" alt="">
                        </div>
                        <div class="row">
                            <div class="col-lg-4 col-6">
                                <div class="counter-block">
                                    <span class="mdi mdi-fire"></span>
                                    <div class="details">
                                        <h3 class="mb-0 mt-0 number"><em class="count">{{ item.attr_health }}</em></h3>
                                        <p class="mb-0">Shops</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-6">
                                <div class="counter-block">
                                    <span class="mdi mdi-coffee-outline"></span>
                                    <div class="details">
                                        <h3 class="mb-0 mt-0 number"><em class="count">{{ item.attr_mana }}</em></h3>
                                        <p class="mb-0">Recipe Cost</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-6">
                                <div class="counter-block">
                                    <span class="mdi mdi-account-multiple-outline"></span>
                                    <div class="details">
                                        <h3 class="mb-0 mt-0 number"><em class="count">{{ item.attr_damage }}</em></h3>
                                        <p class="mb-0">Total Cost</p>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-12 col-sm-12">
                                <div class="about-text-block">
                                    <div class="about-content">
                                        <h4>
                                            Description
                                        </h4>
                                        <div class="text">{{ item.Description }} </div>
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

  const mockItemData = require("../../mock/item_detail.json");

  export default {
    computed: mapState({
      mock: state => state.debug.config.mock,
      token: state => state.login.user.token,
      operateItemApi: state => state.api.host + state.api.backend.operateItem,
    }),
    data: function() {
      return {
        item: {},
        errors: [],
      }
    },
    created() {
        if (this.mock) {
            this.item = mockItemData.data;
        } else {
            var config = {
                useCredentails: true
            };
            // get hero info
            axios({  
                method: 'GET', 
                url: this.operateItemApi + this.$route.params.heroid + "/", 
                headers: {Authorization: this.token}, 
                data: { config } 
            }).then(response => {
                this.item = response.data
            }, error => {
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
                    axios({  
                        method: 'DELETE', 
                        url: this.operateItemApi + this.hero.heroid + "/",
                        headers: {Authorization: this.token}, 
                        data: { config }
                    })
                    .then(response => {
                        this.item = response.data
                        this.$router.push({name: "homepage"})
                    }, error => {
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
                } else {
                    this.$router.push({name: "homepage"})
                }
                }
        },
        exportRequest(evt) {
            const data = JSON.stringify(this.item)
            const blob = new Blob([data], {type: ''})
            FileSaver.saveAs(blob, "Item_" + this.item.item_name + '.json')
        }
    },
    components: {
      MainLayout
    }
  }
</script>
<template>
  <main-layout>
    <section class="section bg-light line-vector" id="aboutus">
            <div class="section-area">
                <div class="section-content">
                    <div class="container">
                        <div class="title-block mx-auto">
                            <div class="section_title mb-4 text-center">
                                <h2><span>{{item.itemname}}</span></h2>
                                <div class="image">
                                        <img :src="item.imgurl" class="img-fluid" alt="">
                                    </div>
                            </div>
                        </div>
                        <div class="row">
                            <ul id="portfolio-filter" class="portfolio-filter filters">
                                <li class="button-border list-inline-item">
                                    <a @click="exportRequest" class="pill-button">Export</a>
                                </li>
                                <router-link :to="{name: 'item_update', params: {'itemid': item.itemid}}"> 
                                    <li class="button-border list-inline-item">
                                        <a class="pill-button">Update</a>
                                    </li>
                                </router-link>
                                <li class="button-border list-inline-item">
                                    <a @click="deleteRequest" class="pill-button">Delete</a>
                                </li>
                            </ul>
                        </div>
                        <div class="row">
                            <div class="col-md-12 col-sm-12">
                                <div class="about-text-block">
                                    <div class="about-content">
                                        <h4>
                                            Category
                                        </h4>
                                        <div v-html="item.category" class="text"></div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-12 col-sm-12">
                                <div class="about-text-block">
                                    <div class="about-content">
                                        <h4>
                                            More Infomation
                                        </h4>
                                        <div v-html="item.info" class="text"></div>
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
        originItem: {},
        errors: [],
      }
    },
    created() {
        let reg=new RegExp("\n","g")
        if (this.mock) {
            this.originItem = this.mockItemData.data
            this.item = JSON.parse(JSON.stringify(this.originItem))
            this.item.info = this.item.info.replace(reg,"<br>")
            this.item.category = this.item.category.replace(reg,"<br>")
        } else {
            var config = {
                useCredentails: true
            };
            // get hero info
            axios({  
                method: 'GET', 
                url: this.operateItemApi + this.$route.params.itemid + "/", 
                headers: {Authorization: this.token}, 
                data: { config } 
            }).then(response => {
                this.originItem = response.data
                this.item = JSON.parse(JSON.stringify(this.originItem))
                this.item.info = this.item.info.replace(reg,"<br>")
                this.item.category = this.item.category.replace(reg,"<br>")
            }, error => {
                if (error.response.status === 401) {
                    if (error.response.data.detail === "Authentication credentials were not provided.") {
                        alert("Timeout! Please Login!")
                        this.$store.commit('login/logoutRequest')
                        this.$router.push({name: "login"})
                    } else {
                        alert("You don't have the authorization!")
                        this.$router.push({name: "item_list"})
                    }
                }
            })
        }
    },
    methods: {
        deleteRequest(evt) {
            var r = confirm("Are you sure to delete the hero?");
            if (r == true)
            {
                if (!this.mock) {
                    var config = {
                        useCredentails: true
                    };
                    axios({  
                        method: 'DELETE', 
                        url: this.operateItemApi + this.item.itemid + "/",
                        headers: {Authorization: this.token}, 
                        data: { config }
                    })
                    .then(response => {
                        this.$router.push({name: "item_list"})
                    }, error => {
                        if (error.response.status === 401) {
                            if (error.response.data.detail === "Authentication credentials were not provided.") {
                                alert("Timeout! Please Login!")
                                this.$store.commit('login/logoutRequest')
                                this.$router.push({name: "login"})
                            } else {
                                alert("You don't have the authorization!")
                                this.$router.push({name: "item_list"})
                            }
                        }
                    })
                } else {
                    this.$router.push({name: "item_list"})
                }
            }
        },
        exportRequest(evt) {
            const data = JSON.stringify(this.originItem)
            const blob = new Blob([data], {type: ''})
            FileSaver.saveAs(blob, "Item_" + this.item.itemname + '.json')
        }
    },
    components: {
      MainLayout
    }
  }
</script>

<style scoped>

</style>
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
                                                        <input v-model="item.itemname" name="name" id="name" type="text" class="form-control pl-5" placeholder="Name" required>
                                                    </div>
                                                </div><!--end col-->
                                                <div class="col-md-12">
                                                    <div class="form-group position-relative">
                                                        <label> Image Url </label>
                                                        <input v-model="item.imgurl" name="image" id="image" type="text" class="form-control pl-5" placeholder="Image Url">
                                                    </div>
                                                </div><!--end col-->
                                                <div class="col-md-12">
                                                    <div class="form-group position-relative">
                                                        <div class="image">
                                                            <img :src="item.imgurl" class="img-fluid" alt="">
                                                        </div>
                                                    </div>
                                                </div><!--end col-->
                                                <div class="col-md-12">
                                                    <div class="form-group position-relative">
                                                        <label>Category</label>
                                                        <textarea v-model="item.category" name="comments" id="comments" rows="4" class="form-control pl-5" placeholder="The Bio..."></textarea>
                                                    </div>
                                                </div><!--end col-->
                                                <div class="col-md-12">
                                                    <div class="form-group position-relative">
                                                        <label>More Infomation</label>
                                                        <textarea v-model="item.info" name="comments" id="comments" rows="4" class="form-control pl-5" placeholder="The Bio..."></textarea>
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
            axios({  
                method: 'GET', 
                url: this.operateItemApi + this.$route.params.itemid + `/`, 
                headers: {Authorization: this.token}, 
                data: { config } 
            })
            .then(response => {
                this.item = response.data
            }, error => {
                if (error.response.status === 401) {
                    if (error.response.data.detail = "Authentication credentials were not provided.") {
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
                var item = this.item
                axios({  
                    method: 'PUT', 
                    url: this.operateItemApi + this.item.itemid + `/`, 
                    headers: {Authorization: this.token}, 
                    data: item
                })
                .then(response => {
                    this.item = response.data
                    alert("succeed to update!")
                    this.$router.push({name: "item_detail", param: {itemid: this.item.itemid}})
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
                this.$router.push({name: "item_detail", param: {itemid: this.item.itemid}})
            }
        }
    },
    components: {
      MainLayout
    }
  }
</script>
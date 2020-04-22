<template>
  <main-layout>
    <div id="app" class="container my-5">
      <section id="portfolio" class="section portfolio-section">
            <div class="section-area">
                <div class="section-content">
                    <div class="container">
                        <div class="title-block mx-auto">
                            <div class="section_title mb-4 text-center">
                                <h2><span>All Items!!!</span></h2>
                            </div>
                        </div>
                        <div class="position-relative">
                            <label> Item Search... </label>
                            <input v-model="searchName" name="searchName" id="searchName" type="text" placeholder="Search for your item...">
                        </div>
                        <div class="row">
                            <ul id="portfolio-filter" class="portfolio-filter filters">
                                <li class="button-border list-inline-item">
                                    <a @click="exportAllItemsRequest" class="pill-button">Export All Items</a>
                                </li>
                                <!-- <router-link :to="{name: 'item_create'}">  -->
                                    <li class="button-border list-inline-item">
                                        <a class="pill-button">Create a New Item</a>
                                    </li>
                                <!-- </router-link> -->
                            </ul>
                        </div>
                        <div class="portfolio-items row">
                          <Item
                          v-for="item in items"
                          :key="item.itemid"
                          :id="item.itemid"
                          :name="item.itemname"
                          :image="item.imgurl"></Item>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
  </main-layout>
</template>

<script>
import Item from '../../components/Item';
import { mapState } from 'vuex'
import MainLayout from '../../layouts/Main.vue'
import axios from "axios";
import FileSaver from 'file-saver'

const mockItemsData = require("../../mock/items.json");

export default {
    name: 'item_list',
    computed: mapState({
      mock: state => state.debug.config.mock,
      token: state => state.login.user.token,
      getAllItemApi: state => state.api.host + state.api.backend.operateItem,
    }),
    data() {
      return {
        searchName: "",
        items: [],
        allItems: [],
        errors: [],
      };
    },
    watch: {
      searchName: function (val) {
        if (val === "") {
          this.items = this.allItems
        } else {
          this.items = []
          for (var i=0; i<this.allItems.length; i++) {
            var name = this.allItems[i].itemname.toLowerCase()
            if (name.indexOf(val) > -1) {
              this.items.push(this.allItems[i])
            }
          }
        }
      }
    },
    created() {
      if (this.mock) {
        this.items = mockItemsData.data;
        this.allItems = mockItemsData.data;
      } else {
        var config = {
            useCredentails: true
        };
        axios({  
          method: 'GET', 
          url: this.getAllItemApi, 
          headers: {Authorization: this.token}, 
          data: { config } 
        })
        .then(response => {
            this.items = response.data
            this.allItems = response.data
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
        exportAllItemsRequest(evt) {
            const data = JSON.stringify(this.items)
            const blob = new Blob([data], {type: ''})
            FileSaver.saveAs(blob, 'AllItems.json')
        }
    },
    components: {
        Item,
        MainLayout,
    },
};
</script>

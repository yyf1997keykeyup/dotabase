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
                        <div class="row">
                            <ul id="portfolio-filter" class="portfolio-filter filters">
                                <li class="button-border list-inline-item">
                                    <a @click="exportAllItemsRequest" class="pill-button">Export All Items</a>
                                </li>
                                <router-link :to="{name: 'item_create'}"> 
                                    <li class="button-border list-inline-item">
                                        <a class="pill-button">Create a New Item</a>
                                    </li>
                                </router-link>
                            </ul>
                        </div>
                        <div class="portfolio-items row">
                          <Hero
                          v-for="item in items"
                          :key="item.itemid"
                          :id="item.itemid"
                          :name="item.name"
                          :image="item.imageurl"></Hero>
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
        heros: [],
        errors: [],
      };
    },
    created() {
      if (this.mock) {
        this.heros = mockHerosData.data;
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
            // console.log(response)
            this.heros = response.data
        })
        .catch(e => {
            this.errors.push(e)
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

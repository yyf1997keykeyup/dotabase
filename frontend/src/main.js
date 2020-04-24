import Vue from 'vue'
import VueRouter from 'vue-router'
import store from './store/index'
import App from './pages/App.vue'

import HeroHome from './pages/hero/Home.vue'
import HeroDetail from './pages/hero/Detail.vue'
import HeroUpdate from './pages/hero/Update.vue'
import HeroCreate from './pages/hero/Create.vue'
import HeroLog from './pages/hero/Log.vue'
import HeroGoodAgainst from './pages/hero_relation/GoodAgainst.vue'

import ItemList from './pages/item/ItemList.vue'
import ItemDetail from './pages/item/Detail.vue'
import ItemUpdate from './pages/item/Update.vue'
import ItemCreate from './pages/item/Create.vue'



import Login from './pages/Login.vue'
import Register from './pages/Register.vue'


const routes = [
  { path: '/', name: 'homepage', component: HeroHome, props: true},
  { path: '/hero/query/:heroid', name: 'hero_detail', component: HeroDetail , props: true},
  { path: '/hero/update/:heroid', name: 'hero_update', component: HeroUpdate, props: true},
  { path: '/hero/create', name: 'hero_create', component: HeroCreate, props: true},
  { path: '/hero/log', name: 'hero_logs', component: HeroLog, props: true},
  { path: '/hero/goodAgainst', name: 'hero_good_against', component: HeroGoodAgainst, props: true},

  { path: '/item', name: 'item_list', component: ItemList, props: true},
  { path: '/item/query/:itemid', name: 'item_detail', component: ItemDetail , props: true},
  { path: '/item/update/:itemid', name: 'item_update', component: ItemUpdate, props: true},
  { path: '/item/create', name: 'item_create', component: ItemCreate, props: true},



  { path: '/login', name: 'login', component: Login , props: true},
  { path: '/register', name: 'register', component: Register, props: true},
]

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: routes
})

const app = new Vue({
  el: '#app',
  router,
  store,
  render: c => c(App),
})
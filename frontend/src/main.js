import Vue from 'vue'
import VueRouter from 'vue-router'
import store from './store/index'
import App from './pages/App.vue'

import HeroHome from './pages/hero/Home.vue'
import HeroDetail from './pages/hero/Detail.vue'
import HeroUpdate from './pages/hero/Update'
import HeroCreate from './pages/hero/Create'

import ItemHome from './pages/Item/ItemList'

import Login from './pages/Login.vue'
import Register from './pages/Register'


const routes = [
  { path: '/', name: 'homepage', component: HeroHome },
  { path: '/hero/:heroid', name: 'hero_detail', component: HeroDetail },
  { path: '/hero/update/:heroid', name: 'hero_update', component: HeroUpdate},
  { path: '/hero/create', name: 'hero_create', component: HeroCreate},

  { path: '/item', name: 'item', component: ItemHome},

  { path: '/login', name: 'login', component: Login },
  { path: '/register', name: 'register', component: Register},
]

Vue.use(VueRouter)

const router = new VueRouter({
  routes: routes
})

const app = new Vue({
  el: '#app',
  router,
  store,
  render: c => c(App),
})
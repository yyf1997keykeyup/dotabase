import Vue from 'vue'
import VueRouter from 'vue-router'
import store from './store/index'
import App from './pages/App.vue'
import Home from './pages/Home.vue'
import Detail from './pages/Detail.vue'
import Login from './pages/Login.vue'
import Register from './pages/Register'
import Update from './pages/Update'
import Create from './pages/Create'

const routes = [
  { path: '/', name: 'homepage', component: Home },
  { path: '/detail', name: 'detail', component: Detail },
  { path: '/update', name: 'update', component: Update},
  { path: '/create', name: 'create', component: Create},
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
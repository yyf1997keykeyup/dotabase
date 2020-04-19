import Vue from 'vue'
import VueRouter from 'vue-router'
import store from './store/index'
import App from './pages/App.vue'
import Home from './pages/Home.vue'
import Detail from './pages/Detail.vue'

// import routes from './routes'

// const app = new Vue({
//   el: '#app',
//   store,
//   data: {
//     currentRoute: window.location.pathname
//   },
//   computed: {
//     ViewComponent () {
//       const matchingView = routes[this.currentRoute]
//       return matchingView
//         ? require('./pages/' + matchingView + '.vue')
//         : require('./pages/404.vue')
//     }
//   },
//   render (h) {
//     return h(this.ViewComponent.default)
//   }
// })

// window.addEventListener('popstate', () => {
//   app.currentRoute = window.location.pathname
// })

const routes = [
  { path: '/', name: 'homepage', component: Home },
  { path: '/detail', name: 'detail', component: Detail }
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
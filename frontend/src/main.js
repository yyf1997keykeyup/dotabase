import Vue from 'vue'
import store from './store/index'
import routes from './routes'

const app = new Vue({
  el: '#app',
  store,
  data: {
    currentRoute: window.location.pathname
  },
  computed: {
    ViewComponent () {
      const matchingView = routes[this.currentRoute]
      return matchingView
        ? require('./pages/' + matchingView + '.vue')
        : require('./pages/404.vue')
    }
  },
  render (h) {
    return h(this.ViewComponent.default)
  }
})

window.addEventListener('popstate', () => {
  app.currentRoute = window.location.pathname
})
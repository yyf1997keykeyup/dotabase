import Vue from 'vue'
import Vuex from 'vuex'
import login from './modules/login'
import debug from './modules/debug'
import api from './modules/api'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    login,
    debug,
    api,
  },
})
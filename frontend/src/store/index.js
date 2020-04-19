import Vue from 'vue'
import Vuex from 'vuex'
import heros from './modules/heros'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    heros
  },
})
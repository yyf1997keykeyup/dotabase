const state = {
  user: {
    username: "",
    permission: {}
  }
  }

  const getters = {
  }

  
  // actions
  const actions = {
    // login({ dispatch, commit }, payload) {
    //   commit('loginRequest', payload);
    // },
  }
  
  // mutations
  const mutations = {
    loginRequest (state, payload) {
      state.user.username = payload.username
      state.user.permission = payload.permission
    },
    logoutRequest (state) {
      state.user.username = ""
      state.user.permission = {}
    }
  }
  
  export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
  }
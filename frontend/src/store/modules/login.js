const state = {
  user: {
    username: "",
    token: "",
  }
  }

  const getters = {
  }

  
  // actions
  const actions = {
  }
  
  // mutations
  const mutations = {
    loginRequest (state, payload) {
      state.user.username = payload.username
      state.user.token = "JWT " + payload.token
    },
    logoutRequest (state) {
      state.user.username = ""
      state.user.token = ""
    }
  }
  
  export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
  }
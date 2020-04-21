const state = {
  user: {
    username: "",
    token: "",
    permission: {},
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
      state.user.token = payload.token
    },
    logoutRequest (state) {
      state.user.username = ""
      state.user.token = ""
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
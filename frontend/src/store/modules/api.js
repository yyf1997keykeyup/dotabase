const state = {
    backend: {
        getAllHeros: "http://127.0.0.1:8000/api/dotabase/hero",
    }
}


export default {
    namespaced: true,
    state,
  }
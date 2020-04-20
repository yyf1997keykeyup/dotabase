const state = {
    host: "http://127.0.0.1:8000",
    backend: {
        operateHero: "/api/dotabase/hero/",
    }
}


export default {
    namespaced: true,
    state,
  }
const state = {
    host: "http://127.0.0.1:8000",
    backend: {
        operateHero: "/api/dotabase/hero/",
        getLogByHeroId: "/api/dotabase/log/",
        login: "/api/dotabase/login/",            // todo: modify the url
    }
}


export default {
    namespaced: true,
    state,
  }
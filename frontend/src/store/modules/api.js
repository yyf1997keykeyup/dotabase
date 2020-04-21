const state = {
    host: "http://127.0.0.1:8000",
    backend: {
        operateHero: "/api/dotabase/hero/",
        getLogByHeroId: "/api/herolog/log/", // todo: modify the url
        login: "/api/dotabase/login/",            // todo: modify the url
    }
}


export default {
    namespaced: true,
    state,
  }
const state = {
    host: "http://127.0.0.1:8000",
    backend: {
        operateHero: "/api/dotabase/hero/",
        operateItem: "/api/dotabase/item/",
        operateHeroGoodAgainst: "/api/dotabase/hero_good_against/",
        operateHeroBadAgainst: "/api/dotabase/hero_bad_against/",
        operateHeroBestCombos: "/api/dotabase/hero_best_combos/",
        getSkillByHeroId: "/api/dotabase/hero_skill/",
        getLogByHeroId: "/api/dotabase/hero_log/",
        login: "/api/dotabase/user/get_token/",
    }
}


export default {
    namespaced: true,
    state,
  }
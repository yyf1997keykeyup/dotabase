<template>
<main-layout>
    <div>
        <div class="title-block mx-auto">
                            <div class="section_title mb-4 text-center">
                                <h2><span>Hero Logging</span></h2>
                            </div>
                        </div>
        <table style="position:absolute; left:100px">
            <tr>
                <th>hero name</th>
                <th>health</th>
                <th>mana</th>
                <th>damage</th>
                <th>create time</th>
            </tr>
            <tr v-for="log in logs" :key="log.logid">
                <th>{{log.hero_name}}</th>
                <th>{{log.attr_health}}</th>
                <th>{{log.attr_maga}}</th>
                <th>{{log.attr_damage}}</th>
                <th>{{log.create_time}}</th>
            </tr>
        </table>
    </div>
    </main-layout>
</template>

<script>
    import { mapState } from 'vuex'
    import axios from 'axios'
    import MainLayout from '../../layouts/Main.vue'

    const mockHeroLogData = require("../../mock/hero_log.json");

    export default {
        computed: mapState({
            mock: state => state.debug.config.mock,
            token: state => state.login.user.token,
            getLogsApi: state => state.api.host + state.api.backend.getLogByHeroId
        }),
        components: {
            MainLayout,
        },
        data: function() {
            return {
                logs: [],
                errors: [],
            }
        },
        created() {
            if (this.mock) {
                this.logs = mockHeroLogData.data;
            } else {
                var config = {
                    useCredentails: true
                };
                // get hero info
                // axios.get(this.getLogsApi, config)
                axios({  
                    method: 'GET', 
                    url: this.getLogsApi, 
                    headers: {Authorization: this.token}, 
                    data: { config } 
                })
                .then(response => {
                    this.logs = response.data
                }, error => {
                    if (error.response.status === 401) {
                        if (error.response.data.detail === "Authentication credentials were not provided.") {
                            alert("Timeout! Please Login!")
                            this.$store.commit('login/logoutRequest')
                            this.$router.push({name: "login"})
                        } else {
                            alert("You don't have the authorization!")
                            this.$router.push({name: "homepage"})
                        }
                    }
                })
            }
        },
    }
</script>

<style>
    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #dddddd;
    }
</style>
<template>
<div>
<header>
            <div class="header-navbar h-100">
                <a class="navbar-brand">
                  <router-link :to="{name: 'homepage', params: {}}">
                    <div class="row mb-3">
                        <img style="width:80px;position: absolute;right:-0px;" :src="icon_url"/>
                      </div>
                    </router-link>
                  </a>
                <nav class="navbar menu-list">
                    <ul class="list-group text-center" id="menu">
                        <li class="list-group-item">
                          <router-link :to="{name: 'homepage', params: {}}">
                            <a class="active">
                                <span class="menu-icon mx-auto"><i class="mdi mdi-home-outline"></i></span>
                                <span>Home</span>
                            </a>
                          </router-link>
                        </li>
                        <li class="list-group-item">
                            <a>
                              <router-link :to="{name: 'homepage', params: {}}">
                                <span class="menu-icon mx-auto"><i class="mdi mdi-account-outline"></i></span>
                                <span>Heros</span>
                              </router-link>
                            </a>
                        </li>
                        <li class="list-group-item">
                            <a>
                                <span class="menu-icon mx-auto"><i class="mdi mdi-briefcase-outline"></i></span>
                                <span>Items</span>
                            </a>
                        </li>
                        <li v-if="username === ''" class="list-group-item">
                            <a>
                              <router-link :to="{name: 'login'}"> 
                                <span class="menu-icon mx-auto"><i class="mdi mdi-grid-large"></i></span>
                                <span>Login</span>
                              </router-link> 
                            </a>
                        </li>
                        <li v-if="username === ''" class="list-group-item">
                            <a>
                              <router-link :to="{name: 'register'}"> 
                                <span class="menu-icon mx-auto"><i class="mdi mdi-chart-bubble"></i></span>
                                <span>Register</span>
                              </router-link> 
                            </a>
                        </li>
                        <li v-if="username != ''" class="list-group-item">
                            <a>
                                <span class="menu-icon mx-auto"><i class="mdi mdi-grid-large"></i></span>
                                <span>{{ username }}</span>
                            </a>
                        </li>
                        <li v-if="username != ''" class="list-group-item">
                            <a @click="logout">
                                <span class="menu-icon mx-auto"><i class="mdi mdi-chart-bubble"></i></span>
                                <span>Logout</span>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>

        </header>
        <slot></slot>
        </div>
</template>

<script>
import { mapState } from 'vuex' 

  export default {
    data() {
      return {
        icon_url: require("../assets/images/dotabase_icon.png")
      }
    },
    computed: mapState({
          username: state => state.login.user.username
      }),
    methods: {
        logout (evt) {
            evt.preventDefault()
            alert("succeed to logout!")
            this.$store.commit('login/logoutRequest')
        }
    },
    components: {
    }
  }
</script>

<template>
  <div class="container my-5">
    <div class="row mb-3">
        <div class="col-md-9">
          <h1>Dotabase</h1>
        </div>
      </div>
    <ul>
      <li>
        <router-link :to="{name: 'homepage', params: {}}"> Home </router-link>
      </li>
      <li v-if="username === ''">
        <router-link :to="{name: 'login', params: {}}"> login </router-link>
        <router-link :to="{name: 'register', params: {}}"> register </router-link>
      </li>
      <li v-else>
        <a> welcome, {{ username }}! Enjoy yourself or </a>
        <button @click="logout"> LOGOUT </button>
      </li>
    </ul>

    <slot></slot>
  </div>
</template>

<script>
import { mapState } from 'vuex' 

  export default {
    computed: mapState({
          username: state => state.login.user.username
      }),
    methods: {
        logout (evt) {
            evt.preventDefault()
            this.$store.commit('login/logoutRequest')
        }
    },
    components: {
    }
  }
</script>

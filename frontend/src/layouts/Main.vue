<template>
  <div class="container my-5">
    <ul>
      <li>
        <router-link :to="{name: 'homepage', params: {}}"> Home </router-link>
      </li>
    </ul>

    <slot></slot>
  </div>
</template>

<script>
import VLink from '../components/VLink.vue'
  export default {
    components: {
      VLink
    }
  }
</script>

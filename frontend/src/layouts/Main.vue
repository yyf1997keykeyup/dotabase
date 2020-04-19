<template>
  <div class="container my-5">
    <ul>
      <li>
        <v-link href="/">Home</v-link>
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

<template>
    <div class="col-md-3">
        <v-link href="/detail">
        <div class="card">
            <img :src="image" :alt="name" class="card-img-top">
            <div class="card-body">
                <h5>{{ name }}</h5>
            </div>
        </div>
        </v-link>
    </div>
</template>

<script>
import VLink from '../components/VLink.vue'

export default {
  name: 'hero',
  props: ['id', 'name', 'image'],
  filters: {
  },
  methods: {
  },
  components: {
      VLink
      },
};
</script>
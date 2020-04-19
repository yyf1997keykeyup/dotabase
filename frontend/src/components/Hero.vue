<template>
    <div class="col-md-3">
        <router-link :to="{name: 'detail', params: {'id': id}}">
        <div class="card">
            <img :src="image" :alt="name" class="card-img-top">
            <div class="card-body">
                <h5>{{ name }}</h5>
            </div>
        </div>
        </router-link>
    </div>
</template>

<script>

export default {
  name: 'hero',
  props: ['id', 'name', 'image'],
  filters: {
  },
  methods: {
  },
  components: {
  },
};
</script>
<template>
    <div class="col-lg-4 portfolio-item seo">
        <div class="image-border">
            <div class="portfolio-box">
                <img :src="image" class="img-fluid" alt="">
                <div class="img-overlay text-center">
                    <div class="portfolio-icon">
                        <router-link :to="{name: 'hero_detail', params: {'heroid': id}}">
                            <a class="js-zoom-gallery">
                                <i class="mdi mdi-magnify-plus-outline"></i>
                            </a>
                        </router-link>
                    </div>
                    <h5 class="mt-3 mb-0">{{ name }}</h5>
                </div>
            </div>
        </div>
    </div>
    <!-- <div class="col-md-3">
        <router-link :to="{name: 'detail', params: {'id': id}}">
        <div class="card">
            <img :src="image" :alt="name" class="card-img-top">
            <div class="card-body">
                <h5>{{ name }}</h5>
            </div>
        </div>
        </router-link>
    </div> -->
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
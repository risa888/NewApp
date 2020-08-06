<template>
  <div class="home">
    <p>Flowers Home</p>
    
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
export default {
  name: 'home',
  data() {
    return {
      post: []
    }
  },
  methods: {
    getPost() {
      let endpoint = "/api/post/";
      apiService(endpoint)
        .then(data => {
          this.post.push(...data.results)
        })
    }
  },
  created() {
    this.getPost()
    console.log(this.post)
  }
};
</script>

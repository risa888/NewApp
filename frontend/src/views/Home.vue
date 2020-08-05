<template>
  <div class="home">
    <div class="container">
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service"
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

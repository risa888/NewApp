<template>
  <div class="home">
   <div class="containerr mt-2">
      <div v-for="post in posts"
           :key="post.pk">
        <p class="mb-0">Posted by:
          <span class="post-author">{{ post.author }}</span>
        </p>
        <h2>
          <router-link
            :to="{ name: 'post', params: { slug: post.slug } }"
            class="question-link"
            ><img class="post-img" :src="post.photo" alt="">
          </router-link>
        <p class="post-title">{{ post.title }}</p>
        </h2>
        
      <div class="my-4">
        <p v-show="loadingPosts">...loading...</p>
        <button
          v-show="next"
          @click="getPosts"
          class="btn btn-sm btn-outline-success"
          >Load More
        </button>
      </div>
    </div>
  </div>
  <app-footer />
</div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import AppFooter from "@/views/Footer.vue";

export default {
  components: {
    AppFooter
  },
  name: "home",
         
  data() {
    return {
      posts: [],
      next: null,
      loadingPosts: false,
    }
  },
  methods: {
    getPosts() {
      // make a GET Request to the questions list endpoint and populate the questions array
      let endpoint = "/api/post/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingPosts = true;
      apiService(endpoint)
        .then(data => {
          this.posts.push(...data)
          this.loadingPosts = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        })
    }
  },
  created() {
    this.getPosts()
    document.title = "QuestionTime";
  }
};
</script>

<style scoped>
.question-author {
  font-weight: bold;
  color: #DC3545;
}
.question-link {
  font-weight: bold;
  color: black;
}
.question-link:hover {
  color: #343A40;
  text-decoration: none;
}
.post-img {
  width: 400px;
  height: 400px;
}
</style>
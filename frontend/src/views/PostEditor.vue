<template>
 <div class="container mt-2">
     <h1 class="mb-3">PostEditor</h1>
     <form @submit.prevent="onSubmit">
       <div class="form-group">
        <textarea 
            v-model="post_body"
            class="form-control"
            placeholder="What do you want to ask"
            rows='3'
        ></textarea>
       </div>
       <div class="form-group">
           <label for="file1">File:</label>
           <input type="file" id="file1" @change="Upload" class="form-control-file">
       </div>
       <img :src="previewSrc" alt="" width="300" />
        <br>
        <button
            type="submit"
            class="btn btn-success"
         >Publish
        </button>
       </form>
       <p v-if="error" class="muted mt-2">{{ error }}</p>
 </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
    name: "PostEditor",
    data(){
        return{
            post_body: null,
            file: null,
            previewSrc: '',
            error: null
        }
    },
    methods: {
        onSubmit() {
            if(!this.post_body) {
              this.error = "You can't send an empty post!";
            } else if (this.post_body.length > 50) {
              this.error = "Error! " ;
            } else {
              let endpoint = "/api/post/";
              let method = "POST";
              apiService(endpoint, method, { title: this.post_body })
                 .then(post_data => {
                    this.$router.push({ 
                        name: 'post',
                        params: { slug: post_data.slug } 
                    })
                 })
            }
        },

        Upload() {
              let endpoint = "/api/post/";
              let method = "POST";
              apiService(endpoint, method)
                 .then(post_data => {
                    this.$router.push({ 
                        name: 'post',
                        params: { slug: post_data.slug } 
                    })
                })
        }
        },
    
    created() {
        document.title = "Editor - Flowers";
    },
  }   

</script>
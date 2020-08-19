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
           <input type="file" accept='image/*' @change="inputFile" class="selected_file"><br>
       </div>
       <div class="img-view">
           <img :src="PreviewSrc" alt="" width="300" />
       </div> 
       
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

const reader = new FileReader();

export default {
    name: "PostEditor",
    data(){
        return{
            post_body: null,
            file: null,
            PreviewSrc: "",
            error: null
        }
    },
    methods: {
        inputFile:function(e) {
            reader.onload = e => {
                this.PreviewSrc = e.target.result;

            }
            reader.readAsDataURL(e.target.files[0]);
            
              
        },
        onSubmit() {
            if(!this.post_body) {
              this.error = "You can't send an empty post!";
            } else if (this.post_body.length > 25) {
              this.error = "Error! " ;
            } else {
              let endpoint = "/api/post/";
              let method = "POST";
              apiService(endpoint, method, { title: this.post_body },{ photo: this.file })
                 .then(post_data => {
                    this.$router.push({ 
                        name: 'home',
                        params: { slug: post_data.slug } 
                    })
                 })
            }
        },

    //     Upload() {
    //           let endpoint = "/api/post/";
    //           let method = "POST";
    //           apiService(endpoint, method)
    //              .then(post_data => {
    //                 this.$router.push({ 
    //                     name: 'post',
    //                     params: { slug: post_data.slug } 
    //                 })
    //             })
    //     }
       },
    
    created() {
        document.title = "Editor - Flowers";
    },
}   

</script>
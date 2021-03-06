import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import PostEditor from '../views/PostEditor.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  // {
  //   path: '/update',
  //   name: 'post',
  //   component: PostEditor
  // },
  {
    path: '/update',
    name: 'post-editor',
    component: PostEditor
  },
  // {
  //   // with props: true, the slug parameter gets passed as a prop to the component
  //   path: "/post/:slug",
  //   name: "post",
  //   component: PostEditor,
  //   props: true
  // },
  
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes:routes
})

export default router

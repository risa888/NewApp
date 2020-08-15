import Vue from 'vue'
import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/ja'

import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false
Vue.use(ElementUI, {locale})


new Vue({
  router,
  store,
  el: '#app',
  template: '<App/>',
  components: { App },
  render: h => h(App)
}).$mount('#app')
  
// new Vue({
//   el: '#app',
//   template: '<App/>',
//   components: { App }
// })

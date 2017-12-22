// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import 'font-awesome/css/font-awesome.min.css'
import 'element-ui/lib/theme-default/index.css'
import ElementUI from 'element-ui'
import CRUD from 'vue-element-crud'
import components from './components'

import mixins from './mixins'

Vue.use(ElementUI)
Vue.use(CRUD)
Vue.use(components)
Vue.use(mixins)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  template: '<App/>',
  components: { App }
})

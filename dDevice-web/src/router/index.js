import Vue from 'vue'
import Router from 'vue-router'
import { TOKEN_KEY } from '../xhr/configure'
import Login from '../views/login/'
import Layout from '../components/Layout/'
import Welcome from '../views'
import NotFound from '../views/404'
import basicRoutes from './basic'
import modelRoutes from './model'
import deviceRoutes from './device'

Vue.use(Router)

let router = new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/',
      component: Layout,
      redirect: '/welcome',
      children: [
        {
          path: '/welcome',
          component: Welcome,
          name: 'Welcome'
        },
        {
          path: '/404',
          name: 'NotFound',
          component: NotFound
        }
      ].concat(basicRoutes, deviceRoutes, modelRoutes).map(route => {
        route.meta = {
          requiresAuth: true
        }
        return route
      })
    },

    {
      path: '*',
      redirect: '/404'
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (sessionStorage.getItem(TOKEN_KEY) === null && localStorage.getItem(TOKEN_KEY) === null) {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  } else {
    next()
  }  
})

export default router

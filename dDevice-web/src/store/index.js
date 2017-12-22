import Vue from 'vue'
import Vuex from 'vuex'
import app from './modules/app'

Vue.use(Vuex);

let store = new Vuex.Store({
  modules: {
    app
  }
});

export default store

import Vue from 'vue'
import Router from 'vue-router'
//import ResultsScreen from './components/ResultsScreen.vue'
import VideoScreen from './components/VideoScreen.vue'
Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
      {
        path: '/',
        name: 'index',
        component: VideoScreen,
      }
    ]
});
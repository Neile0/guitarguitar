import Vue from 'vue'
import Router from 'vue-router'
import ResultsScreen from './components/ResultsScreen.vue'
import VideoScreen from './components/VideoScreen.vue'
import WhatDoYouLike from './components/WhatDoYouLike.vue'
Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
      {
        path: '/',
        name: 'videoscreen',
        component: VideoScreen,
      },
      {
        path: '/whatdoyoulike',
        name: 'whatdoyoulike',
        component: WhatDoYouLike,
        props:true
      },
      {
        path: '/results/:type/:media',
        name: 'resultsscreen',
        component: ResultsScreen,
        props:true
      }
    ]
});
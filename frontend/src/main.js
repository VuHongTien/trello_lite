import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'
import VueRouter from 'vue-router'
import {sync} from 'vuex-router-sync'
import Router from "vue-router";
import {store} from "@/store/store";
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'
import router from "@/router"
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

const originalPush = Router.prototype.push;
Router.prototype.push = function push(location, onResolve, onReject) {
    if (onResolve || onReject) return originalPush.call(this, location, onResolve, onReject);
    return originalPush.call(this, location).catch(err => err)
};
const unsync = sync(store, router)
unsync()

Vue.component('FontAwesomeIcon', FontAwesomeIcon)

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(Vuex)
Vue.use(VueRouter)


Vue.config.productionTip = false

new Vue({
    render: h => h(App),
    router,
    store: store
}).$mount('#app')

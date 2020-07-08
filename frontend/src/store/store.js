import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";
import users from "@/store/modules/users/users";
import projects from "@/store/modules/projects/projects";
import tasks from "@/store/modules/tasks/tasks";

Vue.use(Vuex);

export const store = new Vuex.Store({
    modules: {
        users,
        projects,
        tasks
    },
    plugins: [createPersistedState({
        key: 'vuex',
        reducer(val) {
            if (localStorage.getItem('token') === null) {
                return null
            }
            return val
        }
    })],
});

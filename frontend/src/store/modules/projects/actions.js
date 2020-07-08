import {api} from "@/api";

export default {
    fetchProjects: context => {
        api.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`;
        return api.get('projects')
            .then(res => {
                context.commit('fetchProjects', res)
            })
    },
    createProject: (context, payload) => {
        api.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`;
        return api.post('projects/create', {
            title: payload.title,
            description: payload.description
        })
            .then(res => {
                context.commit('createProject', res)
            })
    },
    joinProject: (context, payload) => {
        api.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`;
        return api.post(`projects/${payload}/join`)
            .then(res => {
                context.commit('joinProject', res)
            })
    }
}
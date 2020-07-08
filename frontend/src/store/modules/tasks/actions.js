import {api} from "@/api";

export default {
    fetchTasks: (context, payload) => {
        api.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`;
        return api.get(`projects/${payload}`)
            .then(res => {
                context.commit('fetchTasks', res)
            })
    },
    updateTask: (context, payload) => {
        api.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`;
        return api.put(`tasks/${payload.id}/update`, {
            status: payload.status,
            detail: payload.detail
        })
            .then(res => {
                context.commit('updateTask', res)
            })
    },
    deleteTask: (context, payload) => {
        api.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`;
        return api.delete(`tasks/${payload.id}/delete`)
            .then(res => {
                context.commit('deleteTask', res)
            })
    },
    createTask: (context, payload) => {
        api.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`;
        return api.post(`tasks/create`, {
            detail: payload.newTask,
            project_id: payload.projectId
        })
            .then(res => {
                context.commit('createTask', res)
            })
    }
}
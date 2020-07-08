import {api} from "@/api";

export default {
    resetStatus: context => {
        context.commit('resetStatus');
    },
    signIn: (context, payload) => {
        api.defaults.headers.common.Authorization = null
        context.commit('submit');
        return api.post('users/sign_in', payload)
            .then((res) => {
                context.commit('signIn', res);
            })
    },
    signUp: (context, payload) => {
        api.defaults.headers.common.Authorization = null
        context.commit('submit');
        return api.post('users/sign_up', payload)
            .then((res) => {
                context.commit('signUp', res)
            })
    },
    signOut: context => {
        context.commit('signOut');
    },
    updateProfile: (context, payload) => {
        context.commit('submit');
        api.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`;
        return api.put(`users/update`, payload)
            .then((res) => {
                context.commit('updateProfile', res)
            })
    },
    changePassword: (context, payload) => {
        context.commit('submit');
        api.defaults.headers.common.Authorization = `Token ${localStorage.getItem('token')}`;
        return api.put(`users/change_password`, payload)
            .then((res) => {
                context.commit('changePassword', res)
            })
    }
}

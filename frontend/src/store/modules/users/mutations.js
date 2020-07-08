export default {
    submit: state => {
        state.status = 'SUBMITTING'
    },
    resetStatus: state => {
        state.status = ''
    },
    signIn: (state, payload) => {
        let code = payload.data.statusCode;
        console.log(code)
        if (code) {
            state.status = 'FAILED';
        } else {
            localStorage.setItem('token', payload.data.token);
            state.user = payload.data.user;
            state.status = '';
        }
    },
    signUp: (state, payload) => {
        let code = payload.data.statusCode;
        if (code) {
            state.status = 'FAILED';
        } else {
            state.status = '';
        }
    },
    signOut: () => {
        localStorage.clear()
    },
    updateProfile: (state, payload) => {
        state.status = '';
        state.user = payload.data.user
    },
    changePassword: (state, payload) => {
        let code = payload.data.statusCode;
        if (code) {
            state.status = 'FAILED';
        } else {
            state.status = '';
        }
    }
}
export default {
    fetchProjects: (state, payload) => {
        state.projects = payload.data.projects
    },
    createProject: (state, payload) => {
        state.projects.push(payload.data.project)
    },
    joinProject: (state, payload) => {
        let index = state.projects.findIndex(project => project.id === payload.data.project.id)
        state.projects.splice(index, 1, payload.data.project)
    }
}
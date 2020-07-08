export default {
    fetchTasks: (state, payload) => {
        state.tasks = payload.data.project.tasks
    },
    updateTask: (state, payload) => {
        let index = state.tasks.findIndex(task => task.id === payload.data.task.id)
        state.tasks.splice(index, 1, payload.data.task)
    },
    deleteTask: (state, payload) => {
        let index = state.tasks.findIndex(task => task.id === payload.data.task.id)
        state.tasks.splice(index, 1)
    },
    createTask: (state, payload) => {
        state.tasks.push(payload.data.task)
    }
}
<template>
    <div>
        <app-navbar />
        <b-container>
            <b-form-input
                id="input-1"
                v-model="newTask"
                required
                size="lg"
                placeholder="Add new task"
                @keyup.enter="createTask"
            ></b-form-input>
            <task-item
                v-for="task in tasks"
                :key="task.id"
                :task="task"
            />
        </b-container>
    </div>
</template>

<script>
    import TaskItem from "@/views/TaskItem";
    import AppNavbar from "@/views/AppNavbar";

    export default {
        name: "Task",
        components: {AppNavbar, TaskItem},
        data: function () {
            return {
                newTask: '',
                tasks: null,
            }
        },
        created: function () {
            this.$store.dispatch('tasks/fetchTasks', this.$route.params.projectId)
                .then(() => {
                    this.tasks = this.$store.getters['tasks/tasks']
                })
        },
        methods: {
            createTask: function () {
                this.$store.dispatch('tasks/createTask', {
                    newTask: this.newTask,
                    projectId: this.$route.params.projectId
                }).then(() => {
                    this.newTask = ''
                })
            }
        }
    }
</script>

<style scoped>

</style>
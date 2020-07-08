<template>
    <div>
        <b-card
            class="task-card"
            @dblclick="$bvModal.show(modalId)"
        >
            <h3>{{task.detail}}</h3>
            <b-link
                href="#"
                class="card-link"
            >{{dict.find(item => item.value === task.status).text}}
            </b-link>
            <b-button-close
                class="button-close"
                @click="deleteTask"
            />
        </b-card>
        <b-modal
            :id="modalId"
            @ok="updateTask"
        >
            <template v-slot:modal-title>
                Update task
            </template>
            <b-form-group
                id="task"
                label="Task"
                label-for="form-task"
            >
                <b-form-input
                    id="form-task"
                    v-model="form.task"
                    required
                    placeholder="Task"
                ></b-form-input>
            </b-form-group>
            <b-form-group>
                <b-form-select v-model="form.status"
                               :options="dict"
                ></b-form-select>
            </b-form-group>
        </b-modal>
    </div>
</template>

<script>
    export default {
        name: "TaskItem",
        props: {
            task: {
                type: Object,
                required: true
            }
        },
        data: function () {
            return {
                dict: [
                    {
                        value: 0,
                        text: 'Incomplete'
                    },
                    {
                        value: 1,
                        text: 'Work in progress'
                    },
                    {
                        value: 2,
                        text: 'Completed'
                    }
                ],
                form: {
                    task: this.task.detail,
                    status: this.task.status
                }
            }
        },
        computed: {
            modalId: function () {
                return `modal-update-${this.task.id}`
            }
        },
        methods: {
            updateTask: function () {
                this.$store.dispatch('tasks/updateTask', {
                    id: this.task.id,
                    detail: this.form.task,
                    status: this.form.status
                })
            },
            deleteTask: function () {
                this.$store.dispatch('tasks/deleteTask', {
                    id: this.task.id
                })
            }
        }
    }
</script>

<style scoped>
    .task-card {
        border-radius: 15px;
        position: relative;
    }

    .button-close {
        position: absolute;
        top: 15px;
        right: 15px;
    }

    .button-close:hover {
        color: #cb3a63;
    }
</style>
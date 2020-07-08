<template>
    <div>
        <app-navbar />
        <b-container class="page">
            <div
                class="d-flex flex-row-reverse button-create"
            >
                <b-button
                    @click="$bvModal.show('modal-create')"
                    variant="primary"
                >
                    Create new project
                </b-button>
            </div>
            <b-card
                v-for="project in projects"
                :key="project.id"
                class="project-card mb-4"
            >
                <div>
                    <h2>{{project.title}}</h2>
                    <p>{{project.description}}</p>
                </div>
                <div class="d-flex flex-row-reverse">
                    <b-link
                        v-if="!project.users.includes($store.getters['users/user'].id)"
                        href="#"
                        class="card-link"
                        @click="joinProject(project.id)"
                    >Join project
                    </b-link>
                    <b-link
                        v-else
                        href="#"
                        class="card-link"
                        @click="$router.push(`/projects/${project.id}`)"
                    >View tasks
                    </b-link>
                </div>
            </b-card>
            <b-modal
                id="modal-create"
                @ok="createProject"
            >
                <template v-slot:modal-title>
                    Create new project
                </template>
                <b-form-group
                    id="title"
                    label="Title"
                    label-for="form-title"
                >
                    <b-form-input
                        id="form-title"
                        v-model="form.title"
                        required
                        placeholder="Enter project title"
                    ></b-form-input>
                </b-form-group>
                <b-form-group
                    id="description"
                    label="Description"
                    label-for="form-description"
                >
                    <b-form-input
                        id="form-description"
                        v-model="form.description"
                        required
                        placeholder="Enter project description"
                    ></b-form-input>
                </b-form-group>
            </b-modal>
        </b-container>
    </div>
</template>

<script>
    import AppNavbar from "@/views/AppNavbar";

    export default {
        name: "Project",
        components: {AppNavbar},
        data: function () {
            return {
                projects: null,
                form: {
                    title: '',
                    description: ''
                }
            }
        },
        created() {
            this.$store.dispatch('projects/fetchProjects')
                .then(() => {
                    this.projects = this.$store.getters['projects/projects']
                })
        },
        methods: {
            createProject: function () {
                this.$store.dispatch('projects/createProject', this.form)
            },
            joinProject: function (id) {
                this.$store.dispatch('projects/joinProject', id)
            }
        }
    }
</script>

<style scoped>
    .project-card {
        border-radius: 15px;
    }

    .button-create {
        margin-bottom: 20px;
    }

</style>

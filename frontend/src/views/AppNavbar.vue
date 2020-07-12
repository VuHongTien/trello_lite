<template>
    <div class="app-nav">
        <b-navbar
            toggleable="lg"
            type="dark"
            variant="dark"
        >
            <b-navbar-brand href="/projects">
                <img
                    src="../assets/logo.png"
                    alt="Logo"
                    style="width: 80%; height: 80%"
                    type="light"
                >
            </b-navbar-brand>
            <b-navbar-toggle
                target="nav-collapse"
            />
            <b-collapse
                id="nav-collapse"
                is-nav
            >
                <b-navbar-nav
                    class="ml-auto"
                >
                    <b-nav-item-dropdown right>
                        <template
                            #button-content
                        >
                            <font-awesome-icon
                                :icon="['fas', 'cog']"
                                class="folder-icon-svg"
                            />
                        </template>
                        <b-dropdown-item href="/profile">
                            Profile
                        </b-dropdown-item>
                        <b-dropdown-item
                            href="#"
                            @click="signOut"
                        >
                            Sign Out
                        </b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
    import {faCog} from '@fortawesome/free-solid-svg-icons'
    import {library} from '@fortawesome/fontawesome-svg-core'

    library.add(faCog)

    export default {
        name: "AppNavbar",
        methods: {
            signOut: function () {
                this.$store.dispatch('users/signOut')
                    .then(() => {
                        this.$router.push({name: 'sign-in'})
                    })
            }
        }
    }
</script>

<style scoped>
    .app-nav {
        margin-bottom: 30px;
    }
</style>
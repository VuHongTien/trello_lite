<template>
    <div class="page-wrapper">
        <b-container class="page">
            <b-card
                title="Sign in"
                class="mb-2 form-card"
            >
                <b-card-text>
                    <b-form>
                        <b-form-group
                            id="email"
                            label="Email:"
                            label-for="email-form"
                        >
                            <b-form-input
                                id="email-form"
                                type="email"
                                v-model="form.email"
                                required
                                :state="validateState('email')"
                                placeholder="Enter your email"
                            ></b-form-input>
                        </b-form-group>
                        <b-form-group
                            id="password"
                            label="Password:"
                            label-for="password-form"
                        >
                            <b-form-input
                                id="password-form"
                                type="password"
                                v-model="form.password"
                                required
                                :state="validateState('password')"
                                placeholder="Enter your password"
                            ></b-form-input>
                        </b-form-group>
                    </b-form>
                </b-card-text>

                <div class="button-group">
                    <b-button
                        href="#"
                        variant="primary"
                        block
                        @click="signIn"
                    >Sign in
                    </b-button>
                </div>
                <div class="text-footer">
                    Have not an account yet?
                    <b-link
                        href="/sign-up"
                        class="card-link"
                    >
                        Sign up
                    </b-link>
                </div>
            </b-card>
        </b-container>
    </div>
</template>

<script>
    import {validationMixin} from "vuelidate";
    import {required, email, minLength} from "vuelidate/lib/validators"
    import snakecaseKeys from 'snakecase-keys'

    export default {
        name: "SignIn",
        mixins: [validationMixin],
        data: function () {
            return {
                form: {
                    email: null,
                    password: null
                }
            }
        },
        validations: {
            form: {
                email: {
                    required,
                    email
                },
                password: {
                    required,
                    minLength: minLength(6)
                }
            }
        },
        computed: {
            status: function () {
                return this.$store.getters['users/submit']
            }
        },
        methods: {
            validateState: function (name) {
                const {$dirty, $error} = this.$v.form[name];
                return $dirty ? !$error : null;
            },
            makeToast: function () {
                this.$bvToast.toast('Incorrect email or password', {
                    title: 'Login failed',
                    autoHideDelay: 4000,
                    variant: 'danger'
                })
            },
            resetForm: function () {
                this.form = {
                    email: this.form.email,
                    password: null
                }
            },
            signIn: function () {
                this.$v.form.$touch();
                if (this.$v.form.$anyError) {
                    this.makeToast();
                } else {
                    this.$store.dispatch('users/signIn', snakecaseKeys(this.form))
                        .then(() => {
                            if (this.status === 'FAILED') {
                                this.makeToast();
                                this.resetForm();
                                this.$store.dispatch('users/resetStatus');
                            } else {
                                this.$router.push('/projects')
                            }
                        })
                }
            }
        }
    }
</script>

<style scoped>
    .page-wrapper {
        background-color: #EEEEEE;
    }

    .page {
        width: 100%;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .form-card {
        min-width: 500px;
        position: relative;
        bottom: 50px;
        border-radius: 15px;
    }

    .text-footer {
        margin-top: 10px;
    }
</style>
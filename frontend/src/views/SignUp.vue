<template>
    <div class="page-wrapper">
        <b-container class="page">
            <b-card
                title="Sign up"
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
                        <b-form-group
                            id="password-confirm"
                            label="Confirm password:"
                            label-for="password-confirm-form"
                        >
                            <b-form-input
                                id="password-confirm-form"
                                type="password"
                                v-model="form.passwordConfirm"
                                required
                                :state="validateState('passwordConfirm')"
                                placeholder="Confirm your password"
                            ></b-form-input>
                        </b-form-group>
                        <b-form-group
                            id="name"
                            label="Name:"
                            label-for="name-form"
                        >
                            <b-form-input
                                id="name-form"
                                v-model="form.name"
                                required
                                :state="validateState('name')"
                                placeholder="Enter your name"
                            ></b-form-input>
                        </b-form-group>
                        <b-form-group
                            id="tel"
                            label="Telephone number:"
                            label-for="tel-form"
                        >
                            <b-form-input
                                id="tel-form"
                                v-model="form.tel"
                                required
                                :state="validateState('tel')"
                                placeholder="Enter your telephone number"
                            ></b-form-input>
                        </b-form-group>
                    </b-form>
                </b-card-text>

                <div class="button-group">
                    <b-button
                        href="#"
                        variant="primary"
                        block
                        @click="signUp"
                    >Sign up
                    </b-button>
                </div>
                <div class="text-footer">
                    Have an account?
                    <b-link
                        href="/sign-in"
                        class="card-link"
                    >
                        Sign in
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
        name: "SignUp",
        mixins: [validationMixin],
        data: function () {
            return {
                form: {
                    email: null,
                    password: null,
                    passwordConfirm: null,
                    name: null,
                    tel: null,
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
                },
                passwordConfirm: {
                    required,
                    minLength: minLength(6)
                },
                name: {
                    required,
                },
                tel: {
                    required,
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
                this.$bvToast.toast('An error has occurred', {
                    title: 'Sign up failed',
                    autoHideDelay: 4000,
                    variant: 'danger'
                })
            },
            resetForm: function () {
                this.form = {
                    email: this.form.email,
                    password: null,
                    passwordConfirm: null,
                    name: this.form.name,
                    tel: this.form.tel,
                }
            },
            signUp: function () {
                this.$v.form.$touch();
                if (this.$v.form.$anyError) {
                    this.makeToast();
                } else {
                    this.$store.dispatch('users/signUp', snakecaseKeys(this.form))
                        .then(() => {
                            if (this.status === 'FAILED') {
                                this.makeToast();
                                this.resetForm();
                                this.$store.dispatch('users/resetStatus');
                            } else {
                                this.$router.push('/sign-in')
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
        border-radius: 15px;
    }

    .text-footer {
        margin-top: 10px;
    }
</style>
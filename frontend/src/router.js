import VueRouter from 'vue-router'
import SignIn from "@/views/SignIn";
import SignUp from "@/views/SignUp";
import Project from "@/views/Project";
import Task from "@/views/Task";
import Profile from "@/views/Profile";

let routes = [
    {
        path: '/sign-in',
        name: 'sign-in',
        component: SignIn,
        meta: {
            title: 'Sign in',
            requireAuth: false
        }
    },
    {
        path: '/sign-up',
        name: 'sign-up',
        component: SignUp,
        meta: {
            title: 'Sign up',
            requireAuth: false
        }
    },
    {
        path: '/projects',
        name: 'projects',
        component: Project,
        meta: {
            title: 'Project',
            requireAuth: true
        }
    },
    {
        path: '/projects/:projectId',
        name: 'project',
        component: Task,
        meta: {
            title: 'Task',
            requireAuth: true
        }
    },
    {
        path: '/profile',
        name: 'profile',
        component: Profile,
        meta: {
            title: 'Profile',
            requireAuth: true
        }
    }
]

const router = new VueRouter({mode: 'history', routes});

export default router
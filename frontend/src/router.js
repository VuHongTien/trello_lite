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
        component: SignIn
    },
    {
        path: '/sign-up',
        name: 'sign-up',
        component: SignUp
    },
    {
        path: '/projects',
        name: 'projects',
        component: Project
    },
    {
        path: '/projects/:projectId',
        name: 'project',
        component: Task
    },
    {
        path: '/profile',
        name: 'profile',
        component: Profile
    }
]

const router = new VueRouter({mode: 'history', routes});

export default router
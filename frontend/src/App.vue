<template>
    <div id="app">
        <router-view :key="$route.fullPath" />
    </div>
</template>

<script>
    import 'bootstrap/dist/css/bootstrap.css'
    import 'bootstrap-vue/dist/bootstrap-vue.css'


    export default {
        name: 'App',
        components: {}
    }
</script>

<style>

</style>

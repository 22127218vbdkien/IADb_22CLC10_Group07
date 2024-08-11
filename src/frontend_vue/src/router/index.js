import { createWebHistory, createRouter } from "vue-router";
import HomeView from "@/view/HomeView.vue";
import AnimeView from "@/view/AnimeView.vue";
import AnimeBrowseView from "@/view/AnimeBrowseView.vue";
import NotFoundView from "@/view/NotFoundView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes:[
        {
            path: '/',
            name: 'home',
            component: HomeView,
        },
        {
            path: '/animes/',
            name: 'animes',
            component: AnimeBrowseView,
        },
        {
            path: '/animes/:id',
            name: 'animeview',
            component: AnimeView,
        },
        {
            path: '/:catchAll(.*)',
            name: 'not-found',
            component: NotFoundView,
        },
    ],
})

export default router
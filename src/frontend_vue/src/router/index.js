import { createWebHistory, createRouter } from "vue-router";
import HomeView from "@/view/HomeView.vue";
import AnimeView from "@/view/anime/AnimeView.vue";
import AnimeBrowseView from "@/view/anime/AnimeBrowseView.vue";
import NotFoundView from "@/view/NotFoundView.vue";
import LoginView from "@/view/authentication/LoginView.vue";
import SearchView from "@/view/SearchView.vue";
import CharacterBrowseView from "@/view/character/CharacterBrowseView.vue";
import CharacterView from "@/view/character/CharacterView.vue";
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes:[
        {
            path: '/',
            name: 'home',
            component: HomeView,
        },
        {
            path: '/login/',
            name: 'login',
            component: LoginView
        },
        {
            path: '/animes/',
            name: 'animes',
            component: AnimeBrowseView,
        },
        {
            path: '/characters/',
            name: 'characters',
            component: CharacterBrowseView,
        },
        {
            path: '/characters/:id/',
            name: 'characters_view',
            component: CharacterView,
        },
        {
            path: '/animes/search/',
            name: 'searchAnime',
            component: SearchView
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
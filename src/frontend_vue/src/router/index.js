import { createWebHistory, createRouter } from "vue-router";
import HomeView from "@/view/HomeView.vue";
import AnimeView from "@/view/anime/AnimeView.vue";
import AnimeBrowseView from "@/view/anime/AnimeBrowseView.vue";
import NotFoundView from "@/view/NotFoundView.vue";
import LoginView from "@/view/authentication/LoginView.vue";
import SearchView from "@/view/SearchView.vue";
import CharacterBrowseView from "@/view/character/CharacterBrowseView.vue";
import CharacterView from "@/view/character/CharacterView.vue";
import StaffBrowseView from "@/view/staff/StaffBrowseView.vue";
import StaffView from "@/view/staff/StaffView.vue";
import SignUpView from "@/view/authentication/SignUpView.vue";
import UserProfileView from "@/view/UserProfileView.vue";
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
            path: '/signup/',
            name: 'signup',
            component: SignUpView
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
            path: '/staffs/',
            name: 'staffs',
            component: StaffBrowseView,
        },
        {
            path: '/staffs/:id/',
            name: 'staffs_view',
            component: StaffView,
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
            path: '/profile/',
            name: 'profile',
            component: UserProfileView,
        },
        {
            path: '/:catchAll(.*)',
            name: 'not-found',
            component: NotFoundView,
        },
        
    ],
})

export default router
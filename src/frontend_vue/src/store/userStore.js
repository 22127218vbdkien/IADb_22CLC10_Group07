import { defineStore } from "pinia";
import axios from "axios";
export const userState = defineStore('user_auth', {
    state: () =>{
        const storedState = localStorage.getItem('authState')
        return storedState ? JSON.parse(storedState):{
            userAuth: null,
            isAuthenticated: false
        }
    },
    actions: {
        async login(_username, _password, router=null){
            const response =  await axios.post("/api/user/login/", {
                password: _password,
                username: _username
            },
            {
                headers:{
                    "Content-Type":"application/json"
                }
            })
            if (response.status === 200){
                this.userAuth = response.data
                this.isAuthenticated = true
                this.saveState()
                if (router){
                    router.push(('/')) //push to homepage
                }
            }
            else{
                this.userAuth = null
                this.isAuthenticated = false
                this.saveState()
            }
        },
        logout(router=null){
            this.userAuth = null
            this.isAuthenticated = false
            localStorage.removeItem('authState')
            router.push('/')
        },
        saveState(){
            localStorage.setItem('authState', JSON.stringify({
                userAuth: this.userAuth,
                isAuthenticated: this.isAuthenticated
            }))
        }
    }
}) 
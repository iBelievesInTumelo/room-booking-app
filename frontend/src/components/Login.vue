<template>
    <div class="container justify-content-center">
        <dialog id="dialog">
            <form @submit.prevent="handleLogin" method="dialog">
                <div v-if="msg">
                    <h3>{{ msg }}</h3>
                </div>

                <div class="mb-6">
                    <label for="email" class="form-label" >Email address</label>
                    <input type="email" class="form-control" aria-describedby="emailHelp"v-model="email">
                    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                </div>
                <div class="mb-6">
                    <label for="password" class="form-label">Password</label>
                    <input type="password" class="form-control" v-model="password">
                </div>

                <button type="submit" class="btn btn-primary">Login</button><span><button class="btn btn-secondary"
                     @click.stop.prevent="closeDialog">Close</button></span>
            </form>
        </dialog>
        <button class="btn btn-success" @click="handleDialog">Login</button>
    </div>
</template>
<script>
    import axios from 'axios'
    export default {
        data(){
            return {
            email: '',
            password: '',
            msg:'',
            }
        },

        methods:{
            handleLogin(){
                 // Function handles the submission of user information
                const data = {
                    email: this.email,
                    password: this.password,
                }

                axios.post('login', data, {withCredentials: true})
                .then(
                    response => {
                        this.$emit('loggedIn')

                        let user = sessionStorage.setItem('jwt',response.data.jwt)
                        
                        this.closeDialog()

                    }
                ).catch(
                    err =>{
                        this.msg = 'Incorrect email or password'    
                    }
                )
            },

            handleDialog(){
                // Displays a modal when a login button is clicked
                dialog.show();
            },

            closeDialog(){
                // Closes the modal when cancel button is clicked
                dialog.close();
            }
        },
    }
</script>
<style scoped>

</style>



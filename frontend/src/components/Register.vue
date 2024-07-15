<template>
    <div class="container justify-content-center">
        <dialog id="registerDialog">
            <form @submit.prevent="handleSubmit" method="dialog">

                <div class="h4">Register</div>

                <label for="name" class="form-label" >Name</label>
                <input type="text" class="form-control" id="name" v-model="name">
            
                <label for="email" class="form-label" >Email address</label>
                <input type="email" class="form-control" aria-describedby="emailHelp"v-model="email">
                <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
            
                <label for="password" class="form-label">Password</label>
                <input type="password" class="form-control" v-model="password">
            
                <button type="submit" class="btn btn-success">submit</button><button @click.stop.prevent="closeDialog"
                class="btn btn-secondary">Close</button>

            </form>
        </dialog>
        <button @click="handleDialog" class="btn btn-primary">Register</button>
    </div>
</template>
<script>
    import axios from 'axios'
    export default {
        data(){
            return {
            name: '',
            email: '',
            password: '',
            success:'false',
            }
        },
        methods:{
            handleSubmit(){
                // Function handles the submission of user information

                const data = {
                    name: this.name,
                    email: this.email,
                    password: this.password,
                }
            
                axios.post('register',data)
                .then(
                    response => {
                        
                        this.$emit('loggedIn', data)

                        this.handleLogin()

                        this.closeDialog()

                    }
                ).catch(
                    err =>{
                        alert('User could not be registered. Check your input fields for correctness.')
                    }
                )
                
            },
            handleDialog(){
                // Displays a modal when a register button is clicked
                
                registerDialog.show();
            },

            closeDialog(){
                // Closes the modal when cancel button is clicked

                registerDialog.close();
            },
            handleLogin(){
                 // Function handles the submission of user information and logs the user in
                const data = {
                    email: this.email,
                    password: this.password,
                }

                axios.post('login', data, {withCredentials: true})
                .then(
                    response => {
                        this.$emit('loggedIn', data)

                        let user = sessionStorage.setItem('jwt',response.data.jwt)
                        this.success = 'true'
                        
                    }
                ).catch(
                    err =>{
                        this.msg = 'Incorrect email or password'    
                    }
                ).finally(() =>{
                    if(this.success == 'true')
                        window.location.reload()
                    })
            }
        },
    }
</script>



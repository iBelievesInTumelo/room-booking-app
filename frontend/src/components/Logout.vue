<template>
    <div>
        <button class="btn btn-danger float-end" @click="handleLogout">Logout</button>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        methods: {

            handleLogout() {
                // Method logs the user out and clears the session storage and local storage
                
                axios.post('logout')
                
                .then(response => {

                    sessionStorage.clear()

                    localStorage.clear()

                    this.$emit('loggedOut')
                }).
                catch(err =>{
                    alert("Something went wrong logging out. Please close the tap to force a logout")
                })
            }
        }
    }
</script>

<style>

</style>
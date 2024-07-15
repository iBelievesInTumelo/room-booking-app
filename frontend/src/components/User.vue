<template>
 
    <div class="container justify-content-start">
        <h5>Hi {{ name }}</h5>
        <p>Here's your bookings page. You can make bookings or create your own page where people
            can book a room at your property. Look around to find something for yourself.
            You can use {{ id }} as you code when filling out forms.
        </p>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        data () {
            return {
                'id': '',
                'name': '',
            }
        },
        created () {
            // Each time the user component is created, user details will be queried from the backend
            axios.get('user', { withCredentials: true}).

            then( response => {
                this.id = response.data.id
                this.name = response.data.name
                window.sessionStorage.setItem('id',this.id)

                
            }).catch(err => {
                this.$emit('loggedOut')
                alert('User is logged out. Please login!')
            })
            
        },
        
    }
</script>

<style scoped>

</style>
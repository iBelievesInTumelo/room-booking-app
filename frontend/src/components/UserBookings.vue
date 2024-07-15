<template>
    <div class="text-center" v-for="booking in bookings" :key="booking.id">
        <p>Booking for Room: {{booking.room_id}}</p>
        <p>From: {{booking.booking_start}}</p>
        <p>To: {{booking.booking_end}}</p>
        <button class='btn btn-danger' @click="cancelBooking(booking.id)">Cancel booking</button>
    </div>
</template>

<script>
import axios from 'axios';
    export default {
        name: 'UserBookings',
        data(){
            return {
                'userID':'',
                'bookings':{},
                'url': 'bookings/'
            }
        },
    
        methods:{
            cancelBooking(bookingID){
                // Method sends a request to delete an entry in the database

                axios.delete(this.url+bookingID).
                then(response =>{
                    if(response.status == 200){

                        alert("Booking has been deleted!")
                        
                        this.$emit('update')
                    }
                }).catch(err =>{
                    alert(err.message)
                })
            },
            getUserBookings(){
                // Method sends a request to get logged in user details

                this.userID = window.sessionStorage.getItem('id')
                axios.post('userbookings',{'user':this.userID}).
                then(response =>{
                    this.bookings = response.data
                }).catch(err =>{
                    console.log(err)
                })
            },


        },
        beforeMount(){
            // Assigns a user id to logged user instance before component loads

            this.userID = window.sessionStorage.getItem('id')
            
        }
        ,
        mounted(){
            // Calls the method each time the component is loaded
            if(this.userID == null){

                // Check if the promise has executed setting the user id
            setTimeout(()=>{

                this.userID = window.sessionStorage.getItem('id')
                this.getUserBookings()
            },500)
            
            }
            else{
                this.getUserBookings()
            }
        }
    }

</script>

<style scoped>

</style>
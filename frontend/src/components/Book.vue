<template>
    <div>
 
        <form @submit.prevent="handleBooking">
            <div class="mb-6">
                <label for="BookIn" class="form-label" >Start date:</label>
                <input type="date" class="form-control" v-model="booking_start">
                
            </div>
            <div class="mb-6">
                <label for="BookOut" class="form-label">End date:</label>
                <input type="date" class="form-control" v-model="booking_end">
            </div>

            <button type="submit" class="btn btn-primary">Complete Booking</button><span><button class="btn btn-secondary"
                    @click.stop.prevent="closeDialog">Close</button></span>

        </form>

    </div>
</template>

<script>
import axios from 'axios';

    export default {
        name: 'Book',
        data () {
            return {
            
                'booking_start' : '',
                'booking_end' : '',
            }
            
        },
        props: [
            'roomID',
        ]
        ,
        methods:{
            closeDialog(){
                this.$emit('close')
            },
            handleBooking(){

                // Create a payload object for sending booking information to the backend
                
                const payload = {
                    booking_start :this.booking_start,
                    booking_end : this.booking_end,
                    user : window.sessionStorage.getItem('id'),
                    room_id: this.roomID
                }
        
                // Create a new booking using booking details from the user
                
                axios.post('bookings',payload).
                then( response =>{
                    if( response.status == 201){
                        alert('Successful!')
                        this.$emit('close')
                        this.$emit('bookUpdate')
                    }
                }).catch(err =>{
                    alert('Booking not completed, try again!')
                })
                this.$emit('close')
            }
        }
    }
</script>

<style scoped>

</style>
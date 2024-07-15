<template>
<div class="container justify-content-center">
    <dialog id="bookDialog">
        <Book :roomID="room_id"
            @close="closeDialog"
            @open="showDialog"
            @bookUpdate="updateBookings" 
            />
    </dialog>
    <div id="room" v-for="room in rooms" :key="room.id">
        <h5 class="h5 text-center">{{ room.title }}</h5>
        <h4>Room {{ room.id }}</h4>
        <img :src="handleImg(room.image)" alt="..."/>
        <p>{{ room.description }}</p>
        <button @click.stop.prevent="handleBooking(room.id)"
        class="btn btn-primary">Book This Room</button>
    </div> 
</div>

</template>
<script>
    import axios from 'axios';
    import Book from './Book.vue';

    export default {
        name : 'RoomComponent',

        data () {
            return {
                'rooms' : {},
                'pageLoaded': 'false',
                'loggedIn': 'false',
                'link': '../assets/img/',
                'room_id': '',
            }
        },
        components:{
            Book,
        }
        ,

        beforeMount(){
            this.getRoom()
            
        },
        mounted(){
            if(window.sessionStorage.getItem('jwt') != null){
            this.loggedIn = 'true';
            }
        },

        methods: {

            handleBooking(id){
            //Function to get details of logged in user. Only when user is logged in can the function be accessible
            if(sessionStorage.getItem('jwt') != null){
                this.room_id = id;
                bookDialog.show();
            }
            else {
                alert('Please login or register to complete your booking!')
                bookDialog.close();
            }

            },

            getRoom(){
                axios.get('rooms'). then( response =>{
                this.rooms = response.data
                this.pageLoaded = 'true'
                window.localStorage.setItem('rooms',JSON.stringify(response.data))

                }).catch(err =>{
                    alert('Rooms could not be loaded')
                })
            },

            closeDialog(){
                bookDialog.close()
            },

            showDialog(){
                bookDialog.show()
            },
            updateBookings(){
                /* method transfers a method call from child component (Book.vue)
                 to grandparent App.vue to render UserComponent.vue */
                 
                this.$emit('update')
            },
            handleImg(img){
                return new URL(img, import.meta.url).href
            }
        },
    }
</script>
<style scoped>
img{
    height: 400px;
    width: 90%;
    border-radius: 5%;

    margin-left: auto;
    margin-right: auto;
}
#room{
    text-align: center;
}
</style>
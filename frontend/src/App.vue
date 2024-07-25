<script>
import Login from './components/Login.vue';
import Logout from './components/Logout.vue';
import Register from './components/Register.vue';
import User from './components/User.vue';
import RoomComponent from './components/RoomComponent.vue';
import UserBookings from './components/UserBookings.vue';



export default {
  name: "App",
  data () {
    return {
      'loggedIn' : 'false',
      'user_id': '',
      'bookingsKey' : 0,
    }
  },

  components: {
    Login,
    Logout,
    Register,
    User,
    RoomComponent,
    UserBookings,
  },

  mounted() {
    if(window.sessionStorage.getItem('jwt') != null){
      this.loggedIn = 'true'

    }

  },

  methods: {
    userDetails() {
    // Function sets the state of the page to avoid loss of state during refresh
    
      this.loggedIn = 'true'
      this.updateComponent()

    },
    userLoggedOut() {
      // Function clears the cookie from the local storage

      this.loggedIn = 'false'
      window.localStorage.clear()
    },
    updateComponent(){
      this.bookingsKey +=1
    }

  }
}


</script>

<template>
  <div class="container">
    <nav>
      <ul class="nav justify-content-center">
        <li class="nav-item text-left">
          <img src="./assets/home.jpeg" id="img">
        </li>
      </ul>
      <ul class="nav justify-content-center">
      
        <li class="nav-item" v-if="loggedIn == 'false'">
          <Login 
          @loggedIn="userDetails"
          @update="updateComponent"
          />
        </li>

        <li class="nav-item" v-if="loggedIn == 'false'">
          <Register/>
        </li>

        <li class="nav-item text-right" v-if="loggedIn == 'true'">
          <Logout @loggedOut="userLoggedOut"/>
        </li>

      </ul>
  </nav>
</div>
<div class="container">
  <div class="row">

    <div class="col-md-6 col-xs-12 overflow-auto rounded" id="bookings">
        <div class="justify-content-start" v-if="loggedIn == 'true'">
          <User @loggedOut="userLoggedOut"/>
          <UserBookings 
          @update="updateComponent"
          :key="bookingsKey"/>
        </div>

        <div class="h4 text-center"  v-else="loggedIn == 'false'">
          <h4>Login to access your bookings</h4>
        
          <div class="justify-content-end">
            <h4 class="text-center">Your bookings will appear HERE!</h4>
          </div>
        </div>
    </div>

    <div class="col-md-6 col-xs-12 justify-content-center overflow-auto rounded" id="rooms">
      <h4 class=" h4 text-center">Have a look at our range of rooms</h4>
      <RoomComponent 
      @update="updateComponent"/>
    </div>
  </div>
</div>
</template>

<style scoped>
#img {
  height: 120px;
  width: 120px;
}
#bookings{
  background-color:#f0f0f5;
  padding-right: 6px;
  padding-bottom: 6px;
  
}
#rooms{
  background-color:#b3d1ff;
  padding: 6px;
 
}
.container{
  padding: 6px;
}

</style>

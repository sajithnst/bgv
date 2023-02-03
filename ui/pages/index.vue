<template>
<v-app index >
<v-app-bar app color="white">
    <img class="mr-3" :src="require('../assets/blockedge-logo.svg')" height="40"/>
    <v-spacer></v-spacer>
    <v-btn text @click="signin()"  color="indigo darken-4"   >Sign In</v-btn>
    <v-btn text @click="signup()" color="indigo darken-4"   >Sign Up</v-btn>
</v-app-bar>
<v-main>
  <v-container class="text-center">
  </v-container>
  <v-container >
    <v-sheet elevation="4" color="indigo darken-4">
     <h1 class="verifychain" > VERIFI EDGE</h1>
     </v-sheet>
  </v-container>
  <v-container >
    <h1 class="bgv"> Background verification Simplified</h1>
  </v-container>
  <v-container  class="text-center">
    <v-row dense >
    <v-col>
    <img src="../assets/blockedge-logo.svg" height="80" width="250"/><br/>
    <h4 class="text-center"> Plaform Partner</h4> 
  </v-col>
  <v-col>
    <img src="../assets/SecureKloud_Logo.jpg" height="80" width="250"/><br/>
    <h4 class="text-center">Product Partner</h4> 
  </v-col>
  <v-col>
    
    <img src="../assets/healthcaretriangle.png" height="80" width="250"/><br/>
    <h4 class="text-center"> Service Partner</h4> 
  </v-col>
    </v-row>
  </v-container>
  <br/><br/><br/><br/>
   <v-container class="text-center">
    <v-row>
        <v-col>
            <v-btn outlined color="indigo darken-2" width="200px" @click="hr()"> HR SECTION </v-btn>
        </v-col>
        <v-col>
            <v-btn outlined color="indigo darken-2" width="200px" @click="process()"> How it Works ?</v-btn>
        </v-col>
        <v-col>
            <v-btn outlined color="indigo darken-2" width="200px" @click="tech()"> Techical Details</v-btn>
        </v-col>
    </v-row>
   </v-container>
</v-main>
<v-footer dark padless>
  <v-card class="flex" flat tile>
    <v-card-subtitle class="indigo darken-1">
   Copyright : Securekloud
    </v-card-subtitle>
  </v-card>
</v-footer>
</v-app>
</template>

<script>
export default {
  name: 'IndexPage',
  async mounted(){
    this.$vuetify.theme.dark=false;
  },
  data:() =>({
  }),
  methods:{
    async signup(){
      this.$router.push('/signup')
    },
    async signin(){
      this.$router.push('/signin')
    },
    async hr(){
      this.$router.push('/hrsignin')
    },
  }
}
</script>
<style>
.button{
  font-family:  Helvetica, Arial, sans-serif;
}
.bgv{
  font-size: 200%;
  margin-bottom: 5%;
  color: indigo;
  text-align: center;
}
.verifychain{
  font-size: 400%;
  margin-top: 5%;
  color: whitesmoke;
  text-align: center;
}

</style>
<template>
<v-app :dark="false">
<v-app-bar app>
    <v-btn icon> <v-icon>mdi-home</v-icon></v-btn> 
    <v-spacer></v-spacer>
    <v-btn text @click="signin()">Sign In</v-btn>
    <v-btn text @click="signup()">Sign Up</v-btn>
</v-app-bar>
<v-main>
  <v-container>
   <notary/>
  </v-container>
  <v-container>
    
  </v-container>
  <v-container>
   
  </v-container>
  <v-container>
    
  </v-container>
</v-main>
</v-app>
</template>

<script>
export default {
  name: 'IndexPage',
  methods:{
    async signup(){
      this.$router.push('/signup')
    },
    async signin(){
      this.$router.push('/signin')
    },
  }
}
</script>

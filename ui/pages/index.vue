<template>
<v-app index >
<v-app-bar app color="white">
    <img class="mr-3" :src="require('../assets/blockedge-logo.svg')" height="40"/>
    <v-spacer></v-spacer>
    <v-btn text @click="signin()"  color="indigo darken-4"   >Sign In</v-btn>
    <v-btn text @click="signup()" color="indigo darken-4"   >Sign Up</v-btn>
</v-app-bar>
<v-main>
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
<style>
.button{
  font-family:  Helvetica, Arial, sans-serif;
}
</style>
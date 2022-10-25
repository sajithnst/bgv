<template>
<v-app>
<v-app-bar app>
<v-btn icon><v-icon size="32">mdi-home</v-icon></v-btn>
<v-spacer></v-spacer>
<v-btn text @click="signin()">Sign In</v-btn>
<v-btn text @click="signup()">Sign Up</v-btn>
</v-app-bar>
</v-app>
</template>

<script>
export default {
  name: 'IndexPage',
  methods:{
    async signup(){
      this.$router.push('/signup')
    },
  }
}
</script>

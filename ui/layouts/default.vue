<template>
<v-app index >
<v-app-bar app color="white">
    <img class="mr-3" :src="require('../assets/blockedge-logo.svg')" height="40"/>
    <v-spacer></v-spacer>
    <v-btn text @click="signin()"  color="indigo darken-4" width="100px">Sign In</v-btn>
    <v-btn text @click="signup()" color="indigo darken-4"  width="100px" >Sign Up</v-btn>
</v-app-bar>
<v-main>
    <Nuxt/>
</v-main>
<v-footer dark padless>
  <v-card class="flex" flat tile>
    <v-card-subtitle class="indigo darken-1">
        Copyright @ Securekloud Technologies Ltd {{ new Date().getFullYear() }}<br/> Author - Sajith Surendran
    </v-card-subtitle>
  </v-card>
</v-footer>
</v-app>
</template>
<script>
export default {
    name : 'indexlayout',
    async mounted(){
        this.$vuetify.theme.dark=false
    },
    data :() =>({

    }),
    methods : {
        async signup() {
            this.$router.push("/signup");
        },
        async signin() {
            this.$router.push("/signin");
        },
    }
}
</script>
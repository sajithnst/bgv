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

<v-footer
      color="indigo darken-1"
      dark
    >
      <v-row
        justify="center"
        class="my-4 text-center"
      >
        <v-col cols="12"
          >Copyright @ Securekloud Technologies Ltd {{ new Date().getFullYear() }}</v-col
        >
        <v-col cols="12" style="width: 30%;">
          <v-btn
            v-for="icon in icons"
            :key="icon"
            text
            dark
          >
            <v-icon>{{ icon }}</v-icon>
          </v-btn>
        </v-col>
        <v-col
          cols="12"
          class="align-center"
          >&copy; 2023 VerifiEdge</v-col>
      </v-row>
    </v-footer>
</v-app>
</template>
<script>
export default {
    name : 'indexlayout',
    async mounted(){
        this.$vuetify.theme.dark=false
    },
    data: () => {
    return {
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-instagram',
        'mdi-youtube',
      ],
    };
  },
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

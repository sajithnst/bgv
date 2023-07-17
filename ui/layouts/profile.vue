<template>
    <v-app userprofile>
        <v-app-bar app  color="indigo darken-4">
            <v-app-bar-title style="color: ghostwhite;">User Profile</v-app-bar-title>
            <v-spacer></v-spacer>
            <v-btn text style="color: ghostwhite;width: 100px;" @click="logout()">Close</v-btn>
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
        <v-col cols="12" style="width: 10%;">
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
          >&copy; 2023 VerifiEdge</v-col
        >
      </v-row>
    </v-footer>
    </v-app>
</template>
<script>
export default {
  name:'profile',
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
    methods:{
        async logout (){
          this.$router.push('/signin')

        }
    }
}
</script>

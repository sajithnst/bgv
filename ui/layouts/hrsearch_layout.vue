<template>

  <v-app>
  <v-app-bar app color="indigo darken-4" :clipped-left="clipped" fixed>
    &ensp; &ensp; &ensp;
    <v-btn icon @click="home()" ><v-icon color="white">mdi-home</v-icon></v-btn>
    <v-spacer></v-spacer>
    <v-spacer></v-spacer>
    <v-toolbar-title style="color: white;">User Profile</v-toolbar-title>
    <v-spacer></v-spacer>
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
        >Copyright @ Securekloud Technologies Ltd {{ new Date().getFullYear() }}<br/> Author - Sajith Surendran</v-col
      >
      <v-col cols="12">
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

<script >
export default {
  name:'user_profile',
  async mounted () {
  this.$vuetify.theme.dark = false
},
data() {
  return {
    drawer: false,
  };
},


methods: {
  async logout() {
      this.$router.push("/hrpage")
  }
}

}
</script>

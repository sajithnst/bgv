<template>

  <v-app>
    <v-navigation-drawer
  color="indigo darkern-4"
  v-model="drawer"
  app

  >
  <v-list>
    <v-list-item >
      <v-divider></v-divider>
      <v-list-item-action>

      </v-list-item-action>
      &emsp;
      <v-list-item-title style="color:white"><h2>Hello Admin</h2></v-list-item-title>
    </v-list-item>
<br>
    <v-list-item @click="profile()">
      <v-divider></v-divider>
      <v-list-item-action>
        <v-icon color="white">mdi-account</v-icon>
      </v-list-item-action>
      &emsp; &emsp;
      <v-list-item-title style="color:white">Admin Profile</v-list-item-title>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item @click="user()">
      <v-divider></v-divider>
      <v-list-item-action>
        <v-icon color="white">mdi-account</v-icon>
      </v-list-item-action>
      &emsp; &emsp;
      <v-list-item-title style="color:white">User Requests</v-list-item-title>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item @click="logout()">
      <v-divider></v-divider>
      <v-list-item-action>
        <v-icon color="white">mdi-logout</v-icon>
      </v-list-item-action>
      &emsp; &emsp;
      <v-list-item-title style="color:white">Logout</v-list-item-title>
    </v-list-item>
    <v-divider></v-divider>
  </v-list>

  </v-navigation-drawer>
  <v-app-bar app color="indigo darken-4" :clipped-left="clipped" fixed>
    &ensp; &ensp; &ensp;
    <v-app-bar-nav-icon color="white" variant="text" @click.stop="drawer = !drawer"><v-icon color="white">mdi-account-circle</v-icon></v-app-bar-nav-icon>
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

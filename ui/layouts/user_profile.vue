<template>

    <v-app>
    <v-app-bar app color="indigo darken-4" :clipped-left="clipped" fixed>
      &ensp; &ensp; &ensp;
      <v-toolbar-title style="color: white;">User Profile</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
        <v-btn icon text color="white" @click="logout()">
        <v-icon>mdi-logout</v-icon>
        <v-spacer></v-spacer>
      </v-btn>
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
          >&copy; 2023 Verify Edge</v-col
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
        this.$router.push("/signin")
    }
  }

  }
</script>

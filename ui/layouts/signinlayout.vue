<template>
     <v-app signin>
        <v-app-bar app color="indigo darken-3">
            <v-btn icon @click="home()"><v-icon size="32" color="white">mdi-home</v-icon></v-btn>
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
          >Copyright @ Securekloud Technologies Ltd {{ new Date().getFullYear() }}</v-col>
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
<script>
export default {
    name:'signin',
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
        async home(){
            this.$router.push('/')
        },
    }
}
</script>

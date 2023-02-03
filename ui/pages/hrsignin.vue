<template>
    <v-app hr>
        <v-app-bar app color="indigo darken-3"> 
           <v-btn icon @click="home()" ><v-icon color="white">mdi-home</v-icon></v-btn>
           <v-spacer></v-spacer>
        </v-app-bar>
        <v-main>
            <v-container  class="signin" >
            <hrlogin/>
        </v-container>
        </v-main>
        <v-footer dark padless>
    <v-card class="flex" flat tile>
      <v-card-subtitle class="indigo darken-1">
     Copyright : Securekloud
      </v-card-subtitle>
    </v-card>
  </v-footer>
    </v-app>
</template>
<script>
export default{
    name: "hrsignin",
    async mounted(){
        this.$vuetify.theme.dark=false;
    },
    data: () => ({

    }),
    methods:{
        async home(){
            this.$router.push('/');
        },
    }
}
</script>
<style>
.signin{
    width: 30%;
    margin: 0% auto;
    text-align: center;
}
</style>

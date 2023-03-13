<template>
 <v-app notary>
    <v-app-bar app color="indigo darken-4">
      <v-btn icon @click="home()" color="white"><v-icon size="32">mdi-home</v-icon></v-btn>
      <v-spacer></v-spacer>
      <v-btn icon @click="logout()" color="white"><v-icon size="32">mdi-logout</v-icon></v-btn>
    </v-app-bar>
    <v-main>
        <v-row>
          <v-col>
            <incomingmail/>
          </v-col>
          <v-col>
              <outgoing/>
          </v-col>
        </v-row>
    </v-main>
 </v-app>
</template>
<script>
export default{
    name :"mailmodel",
    async mounted(){
        this.$vuetify.theme.dark=false;
    },
    data:() =>({
    }),
    
}
</script>

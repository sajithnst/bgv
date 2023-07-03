<template>
    <v-app notary>

    <v-app-bar app color="indigo darken-4">
      <v-btn icon @click="home()" color="white"><v-icon size="32">mdi-home</v-icon></v-btn>

      &emsp; &emsp;
      <h2 style="color: ghostwhite;">Super Admin</h2>
      <v-spacer></v-spacer>
      <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-btn icon

            v-on="on"
          >
            <v-icon color="white">mdi-account-circle</v-icon>
          </v-btn>
        </template>
        <v-list color="indigo darken-4">

<v-list-item @click="profile()">
  <v-divider></v-divider>
  <v-list-item-action>
    <v-icon color="white">mdi-account</v-icon>
  </v-list-item-action>
  &emsp; &emsp;
  <v-list-item-title style="color:white"> Profile</v-list-item-title>
</v-list-item>
</v-list>
        <v-list color="indigo darken-4">

          
          <v-list-item @click="logout()">
            <v-divider></v-divider>
            <v-list-item-action>
              <v-icon color="white">mdi-logout</v-icon>
            </v-list-item-action>
            &emsp; &emsp;
            <v-list-item-title style="color:white">Logout</v-list-item-title>
          </v-list-item>
        </v-list>

      </v-menu>
    </v-app-bar>
        <v-main>
            <Nuxt/>
        </v-main>
    </v-app>
</template>
<script>
export default {
  name:'SuperAdmin_layout',
 
  data: () => {
    return {
      drawer: false,
    };
  },
    methods:{
        async logout (){
          console.log('logout');
          this.$router.push('/SuperAdminLogin');

        },
        async home(){
          this.$router.push('/')
        },
       
    }
}
</script>

<template>
  <v-app notary>
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
  <v-app-bar app color="indigo darken-4" fixed>
    <v-app-bar-nav-icon color="white" variant="text" @click.stop="drawer = !drawer"><v-icon color="white">mdi-account-circle</v-icon></v-app-bar-nav-icon>

    &emsp; &emsp;
    <h2 style="color: ghostwhite;"> Admin</h2>
    <v-spacer></v-spacer>
    <v-btn icon @click="home()" color="white"><v-icon size="32">mdi-home</v-icon></v-btn>


  </v-app-bar>
   <v-main>
      <Nuxt/>
   </v-main>
  </v-app>
</template>
<script>
export default {
name:'notary_page',
async mounted(){
  let nurl ="http://127.0.0.1:8000/notary"
      this.notary_email = this.$storage.getUniversal('notaryemail')
      let nres = await this.$axios.get(nurl,{
        params :{
          email : this.notary_email
        }
      });
      this.notary_name = nres.data.name
},
data: () => {
  return {
    drawer: false,

  };
},
  methods:{
      async logout (){
        console.log('logout');
        this.$router.push('/notarysignin');

      },
      async home(){
        this.$router.push('/');
      },
      async user(){
        this.$router.push('/notary')
      },
      async profile(){
        this.$router.push('/notary_profile')
      }
  }
}
</script>

<template>
  <v-app notary>
  <v-app-bar app color="indigo darken-4" fixed>
    <v-btn icon @click="home()" color="white"><v-icon size="32">mdi-home</v-icon></v-btn>
    &emsp; &emsp;
    <h2 style="color: ghostwhite;"> Admin</h2>
    <v-spacer></v-spacer>
    <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-btn icon
          color="blue"

          v-on="on"
        >
          <v-icon color="white">mdi-account-circle</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item >
          <v-divider></v-divider>
          &emsp;
          <v-list-item-title style="color:black"><h2>Hello Admin</h2></v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item @click="profile()">
          <v-divider></v-divider>
          <v-list-item-action>
            <v-icon color="black">mdi-account</v-icon>
          </v-list-item-action>
          &emsp; &emsp;
          <v-list-item-title style="color:black">Admin Profile</v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item @click="user()">
          <v-divider></v-divider>
          <v-list-item-action>
            <v-icon color="black">mdi-account</v-icon>
          </v-list-item-action>
          &emsp; &emsp;
          <v-list-item-title style="color:black">User Profiles</v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item @click="logout()">
          <v-divider></v-divider>
          <v-list-item-action>
            <v-icon color="black">mdi-logout</v-icon>
          </v-list-item-action>
          &emsp; &emsp;
          <v-list-item-title style="color:black">Logout</v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
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

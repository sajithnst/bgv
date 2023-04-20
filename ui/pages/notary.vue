<template>
 <v-app notary>
    <v-app-bar app color="indigo darken-4">
      <v-btn icon @click="home()" color="white"><v-icon size="32">mdi-home</v-icon></v-btn>
      &emsp;
      <h2 style="color: ghostwhite;"> {{ notary_name }}</h2>
      <v-spacer></v-spacer>
      <v-btn icon @click="logout()" color="white"><v-icon size="32">mdi-logout</v-icon></v-btn>
    </v-app-bar>
    <v-main>
      <v-container class="text-center">
          <h1 style="color: indigo;">INR {{ wallet }}</h1>
          <v-container class="text-center">
            <v-btn text @click="sync()" outlined>sync</v-btn>
          </v-container>
      </v-container>
      <v-container>
        <v-divider class="border-opacity-100 " color="indigo" inset></v-divider>
      </v-container>
      <v-container>
        <h2 class="text-center" style="color: darkblue;"> Profiles</h2>
      </v-container>
  <v-card
    class="mx-auto pa-2"
    style="width: 80%;"
  >
    <v-list density="compact">
      <v-list-item
        v-for="profile in profiles"
        :key="profile.email"
        :value="profile.email"
        active-color="primary"
      >
        <v-list-item-title v-text="profile.name"></v-list-item-title>
        <v-list-item-subtitle v-text="profile.email"></v-list-item-subtitle>
        <v-list-item-title v-text="profile.status"></v-list-item-title>
        <v-btn icon @click="view(profile.email)"><v-icon color="indigo darken-4">mdi-card-account-details-outline</v-icon></v-btn>
        <v-btn icon @click="approve(profile.email)"><v-icon color="green">mdi-account-check-outline</v-icon></v-btn>&emsp;&emsp;
        <v-btn icon @click="deny(profile.email)"><v-icon color="error">mdi-account-remove-outline</v-icon></v-btn>
      </v-list-item>
    </v-list>
  </v-card>
    </v-main>
 </v-app>
</template>
<script>
export default{
    name :"mailmodel",
    async mounted(){
        this.$vuetify.theme.dark=false;
        let nurl ="http://127.0.0.1:8000/notary"
        this.notary_email = this.$storage.getUniversal('notaryemail')

        let nres = await this.$axios.get(nurl,{
          params :{
            email : this.notary_email
          }
        });
        this.notary_name = nres.data.name
        this.wallet = nres.data.wallet
        let url = "http://127.0.0.1:8000/pendinguser"
        let res = await this.$axios.get(url)
        this.profiles = res.data
    },
    data:() =>({
      profiles: [],
      notary_email: null,
      notary_name: null,
      wallet:0,


    }),
    methods:{
      async home(){
        this.$router.push("/");
      },
      async logout(){
        this.$router.push("/notarysignin");
      },
      async view(email){
        this.$storage.setUniversal('user_email',email)
        this.$storage.setUniversal('hrlogin',0)
        this.$router.push("/userprofile");
      },
      async approve(email){
        let url = "http://127.0.0.1:8000/verify"
        let verify ={
          user_email: email,
          notary_email : this.notary_email,
          notary_name: this.notary_name
        }
        let res = await this.$axios.post(url,verify)
        console.log(res.data)
      },
      async deny(email){
        let url = "http://127.0.0.1:8000/verify"
        let verify ={
          user_email: email,
          notary_email : this.notary_email,
          notary_name: this.notary_name,
          status: 'rejected'
        }
        let res = await this.$axios.post(url,verify)
        console.log(res.data)
      },
      async sync(){
        let nurl ="http://127.0.0.1:8000/notary"
        let nres = await this.$axios.get(nurl,{
          params :{
            email : this.notary_email
          }
        });
        this.wallet = nres.data.wallet
      }
    }

  }
</script>

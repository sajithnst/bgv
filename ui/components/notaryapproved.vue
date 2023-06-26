<template>
  <v-container>
    <v-container v-if="show">
      <h2 class="text-center" style="color: darkblue;"> Completed </h2><br /><br/>
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
          <v-btn icon @click="view(profile.email)"><v-icon color="indigo darken-4">mdi-card-account-details-outline</v-icon></v-btn>
          <!--<v-btn icon @click="approve(profile.email)"><v-icon color="green">mdi-account-check-outline</v-icon></v-btn>&emsp;&emsp;
          <v-btn icon @click="deny(profile.email)"><v-icon color="error">mdi-account-remove-outline</v-icon></v-btn>-->
        </v-list-item>
      </v-list>
      </v-card>
    </v-container>
    <v-container v-if="hide">
      <h2 class="text-center" style="color: darkblue;">No Profiles </h2><br /><br/>
    </v-container>

    </v-container>
</template>

<script>
export default{
    name :"notaryapproved",
    layout: "notary_layout",
    async mounted(){
        this.$vuetify.theme.dark=false;
        let url = "http://127.0.0.1:8000/verifiedusers"
        let res = await this.$axios.get(url)
        this.profiles = res.data.list

        if(this.profiles == false){
          this.hide = true
          this.show = false
        }
        else{
          this.show = true
          this.hide = false
        }
    },

    data:() =>({
      profiles: [],
      notary_email: null,
      notary_name: null,
      wallet:0,
      show: false,
      hide:false
    }),
    methods:{
      async home(){
        this.$router.push("/");
      },

      async view(email){
        this.$storage.setUniversal('user_email',email)
        this.$storage.setUniversal('hrlogin',0)
        this.$router.push("/userprofile");
      },
     // async approve(email){
     // let url = "http://127.0.0.1:8000/verify"
     // let verify ={
     //  user_email: email,
     //   notary_email : this.notary_email,
     //   notary_name: this.notary_name
     // }
     //   let res = await this.$axios.post(url,verify)
     //   console.log(res.data)
     // },
     // async deny(email){
     //   let url = "http://127.0.0.1:8000/verify"
     //   let verify ={
     //     user_email: email,
     //     notary_email : this.notary_email,
     //     notary_name: this.notary_name,
     //     status: 'rejected'
     //   }
      //  let res = await this.$axios.post(url,verify)
      //  console.log(res.data)
      //},

    }

  }
</script>

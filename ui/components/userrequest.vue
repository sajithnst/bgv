<template>
<v-container>
     <v-container>
        <h2 class="text-center" style="color: darkblue;">Requests</h2>
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
        <v-list-item-title v-text="profile.hr_name"></v-list-item-title>
        <v-list-item-subtitle v-text="profile.hr_email"></v-list-item-subtitle>
        <v-list-item-title v-text="profile.status"></v-list-item-title>
        <v-btn icon @click="approve(profile.user_email,profile.hr_email)"><v-icon color="green">mdi-book-check-outline</v-icon></v-btn>
        <v-btn icon @click="reject(profile.user_email,profile.hr_email)"><v-icon color="red">mdi-book-remove</v-icon></v-btn>
      </v-list-item>
    </v-list>
  </v-card>
</v-container>
</template>
<script>
export default{
    name : "userrequest",
    async mounted(){
      this.email = this.$storage.getUniversal('Email')
      let url= "http://127.0.0.1:8000/user/pendingrequest"
      let response = await this.$axios.get(url,{params:{email: this.email}})
      this.profiles = response.data
      console.log(response.data)
    },
    data : () => ({
      email :"",
      profiles:[]

    }),
    methods:{
      async approve(email,hr_email){
        let uurl ="http://127.0.0.1:8000/userwallet"
        let udata={
          email:email,
        }
        let res = await this.$axios.post(uurl,udata);
        console.log(res.data)
        let url= "http://127.0.0.1:8000/request/update"
        let update ={
          user_email : email,
          hr_email : hr_email,
          status : "approved"
        }
        let response = await this.$axios.post(url,update)
        if (response.data == true){
          this.$nuxt.refresh()
        }
      },

    }
}
</script>
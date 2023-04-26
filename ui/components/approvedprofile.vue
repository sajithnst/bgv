<template>
   <v-container>
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
        <v-list-item-title >{{ profile.name }}</v-list-item-title>
        <v-list-item-subtitle>{{ profile.email }}</v-list-item-subtitle>
        <v-list-item-title >{{ profile.status }}</v-list-item-title>
        <v-btn icon @click="view(profile.email)"><v-icon color="indigo darken-4">mdi-card-account-details-outline</v-icon></v-btn>
      </v-list-item>
    </v-list>
  </v-card>
</v-container>
</template>
<script>
export default{
   name:"approvedprofile",
   async mounted(){
      let url= "http://127.0.0.1:8000/verifiedusers"
      let res = await this.$axios.get(url)
      this.profiles=res.data
      console.log(this.profiles)
   },
   data:() =>({
      profiles:[]
   }),
   methods:{
      async view(email){
        this.$router.push("/payment");
      },
   }
}
</script>
<template>
 <v-app notary>
    <v-app-bar app color="indigo darken-4">
      <v-btn icon @click="home()" color="white"><v-icon size="32">mdi-home</v-icon></v-btn>
      <v-spacer></v-spacer>
      <v-btn icon @click="logout()" color="white"><v-icon size="32">mdi-logout</v-icon></v-btn>
    </v-app-bar>
    <v-main>
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
        <v-list-item-title v-text="profile.status"></v-list-item-title>
        <v-list-item-subtitle v-text="profile.email"></v-list-item-subtitle>
        <v-btn icon @click="view()"><v-icon color="indigo darken-4">mdi-card-account-details-outline</v-icon></v-btn>
        <v-btn icon @click="approve()"><v-icon color="green">mdi-account-check-outline</v-icon></v-btn>&emsp;&emsp;
        <v-btn icon @click="deny()"><v-icon color="error">mdi-account-remove-outline</v-icon></v-btn>

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
        let url = "http://127.0.0.1:8000/pendinguser"
        let res = await this.$axios.get(url)
        console.log(res.data)
        this.profiles =  res.data
    },
    data:() =>({
      profiles: [{
        'doc' : "SSLC",
        'regno': "DFADF",
        'email': "sajithsurendran007@gmail.com",
        'marks': 98
      },
      {
        'doc' : "HSE",
        'regno': "9787",
        'email': "sajithindra.si@gmail.com",
        'marks': 80
      },
      {
        'doc' : "UG",
        'regno' : "FDF9077",
        'email': "sajithsurendran@gmail.com",
        'marks': 70
      },]
    }),
    
}
</script>

<template>
      <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
    <v-container class="nav-pic">
        <v-avatar size="130">
          <v-icon size="100">mdi-account-circle</v-icon>
        </v-avatar>
      </v-container>
      <v-divider></v-divider>
      <v-container class="nav-pic">
        <h2 class="text-center">{{name}}</h2>
    </v-container>
    <v-btn icon > <v-icon size="30">mdi-account-circle</v-icon></v-btn>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>{{name}}</v-toolbar-title> 
        <v-spacer></v-spacer>
        <v-btn icon @click="logout()"><v-icon>mdi-logout</v-icon></v-btn>
    </v-app-bar>

    <v-main>
      <!--  -->
    </v-main>
</v-app>
</template>
<script>
export default {
    name: 'userpage',
    async mounted(){
        let url ='http://127.0.0.1:8000/user'
        this.email= await this.$storage.getUniversal('Email');
        await this.$axios.get(url,{params:{email : this.email}}).then(res=>{
            this.name = res.data.name
            this.firstlogin = res.data.firstlogin
        }).catch(error => console.log(error));
    },
   
    data :()=>({
        email :'fasdf',
        name : '',
        firstlogin:null,
        drawer: null
        
    }),
    methods:{
        async logout(){
            this.$router.push('/signin')
        }
    }
};
</script>
<style>
.nav-pic {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
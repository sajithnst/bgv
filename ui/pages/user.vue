<template>
      <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
    <v-container class="nav-pic">
          <v-icon size="120">mdi-account-circle</v-icon>
      </v-container>
      <v-divider></v-divider>
      <v-list>
        <v-list-item>
          <v-list-item-title class="font-weight-light"> {{ email }} </v-list-item-title>
        </v-list-item>
      </v-list>
        <v-list dense nav>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          @click="router(item.title)"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>{{name}}</v-toolbar-title> 
        <v-spacer></v-spacer>
        <v-btn icon @click="logout()"><v-icon>mdi-logout</v-icon></v-btn>
    </v-app-bar>

    <v-main>
      <v-container v-if="empdata">
        <h1 class="text-center"> Empdata</h1>
      </v-container>
      <v-container v-if="uploaddata">
        <h1 class="text-center"> Upload data</h1>
      </v-container>
    </v-main>
</v-app>
</template>
<script>
export default {
    name: 'userpage',
    async mounted(){
        var url ='http://52.27.5.60:8000/user'
        this.email= await this.$storage.getUniversal('Email');
        await this.$axios.get(url,{params:{email : this.email}}).then(res=>{
            this.name = res.data.name
        }).catch(error => console.log(error));

    },
   
    data :()=>({
        email :'fasdf',
        name : '',
        drawer: null,
        empdata:null,
        items: [
      { title: "Profile", icon: "mdi-certificate-outline" },
      { title: "Upload", icon: "mdi-upload" },
    ],
        
    }),
    methods:{
        async logout(){
            this.$router.push('/signin')
        },
        async router(title){
           switch(title){
            case "Profile" : 
                this.empdata = true; 
                break;
           }
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
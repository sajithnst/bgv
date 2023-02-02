<template>
      <v-app id="inspire" >
    <v-app-bar app color="indigo darken-2">
        <v-btn icon @click="home()" ><v-icon color="white">mdi-home</v-icon></v-btn>
        <v-toolbar-title>{{name}}</v-toolbar-title> 
        <v-spacer></v-spacer>
        <v-btn text @click="exp()" color="white">Experience</v-btn>
        <v-btn text @click="pg()"  color="white">PG</v-btn>
        <v-btn text @click="skill()" color="white">Skills</v-btn>
        <v-btn icon @click="logout()" color="white"><v-icon>mdi-logout</v-icon></v-btn>
    </v-app-bar>

    <v-main>
      <br/><br/><br/><br/>
      <v-container>
        <h1 class="text-center indigo--text text--lighten-2" > You have completed the onboarding process</h1>
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
        
    }),
    methods:{
        async logout(){
            this.$router.push('/signin')
        },
        async home(){
            this.$router.push('/');
        },
      
    }
};
</script>

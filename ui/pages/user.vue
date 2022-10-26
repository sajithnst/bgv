<template>
    <v-app user>
    <v-app-bar app>
        {{name}}
        <v-spacer></v-spacer>
        <v-btn icon @click="logout()"><v-icon>mdi-logout</v-icon></v-btn>
    </v-app-bar>
    <v-main>
      {{firstlogin}}
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
        
    }),
    methods:{
        async logout(){
            this.$router.push('/signin')
        }
    }
};
</script>
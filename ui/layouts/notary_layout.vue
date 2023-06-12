<template>
    <v-app notary>
    <v-app-bar app color="indigo darken-4">
      <v-btn icon @click="home()" color="white"><v-icon size="32">mdi-home</v-icon></v-btn>
      &emsp;
      <h2 style="color: ghostwhite;"> Admin</h2>
      <v-spacer></v-spacer>
      <v-btn icon @click="logout()" color="white"><v-icon size="32">mdi-logout</v-icon></v-btn>
    </v-app-bar>
        <v-main>
            <Nuxt/>
        </v-main>
    </v-app>
</template>
<script>
export default {
  name:'notary_layout',
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
   
    };
  },
    methods:{
        async logout (){
          console.log('logout');
          this.$router.push('/notarysignin');

        }
    }
}
</script>

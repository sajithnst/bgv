<template>

  <v-container>

      <userbannerpage/>

      <persondetailspage/>

      <sslcviewpage/>

      <hseviewpage/>

      <ugviewpage/>

      <expviewpage/>
  </v-container>

</template>
<script>
export default{
name: 'profile',
layout:'profile',
async mounted (){
this.$vuetify.theme.dark =false;
this.email = this.$storage.getUniversal('login_mail')
let url = "http://127.0.0.1:8000/user"
let res = await this.$axios.get(url,{params:{ email :this.email}});
this.name=res.data.name
},
data: () =>({
name : "Sajith Surendran",
email:"",
}),
methods: {

}
}
</script>

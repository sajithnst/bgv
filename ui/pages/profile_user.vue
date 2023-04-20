<template>

  <v-container>
      <userbanner/>
      <br>
      <v-row justify="center">
      <v-card width="900px">
        <personaldetails/>
      </v-card>

      </v-row>
      <br><br>
      <v-row justify="center">
        <v-card justify="center" width="900px">
          <sslcview/>
        </v-card>

        </v-row>
        <br><br>
        <v-row justify="center">
          <v-card justify="center" width="900px">
            <hseview/>
          </v-card>

          </v-row>
          <br><br>
          <v-row justify="center">
            <v-card justify="center" width="900px">
              <ugview/>
            </v-card>

            </v-row>
            <br><br>
            <v-row justify="center">
              <v-card justify="center" width="900px">
                <expview/>
              </v-card>

              </v-row>
              <br><br>

  </v-container>

</template>
<script>
import { mapState } from 'vuex';
export default{
  props: {
    userEmail: {
      type: String,
      required: true,
    },
  },
  computed: {
    ...mapState(['user']),
  },
name: 'profile',
layout:'user_profile',
async mounted (){
this.$vuetify.theme.dark =false;
var url ='http://127.0.0.1:8000/user'
        this.email= await this.$storage.getUniversal('Email');
        await this.$axios.get(url,{params:{email : this.userEmail}}).then(res=>{
            this.name = res.data.name
        }).catch(error => console.log(error));
},
data: () =>({
name : "Sajith Surendran",
email:"",
}),
methods: {

}
}
</script>

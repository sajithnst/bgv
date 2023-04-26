<template>
  <v-container style="width: 80%; ">
    <v-card>
      <v-card-title>Personal Details</v-card-title>
      <v-card-content>
        <v-container>
          <v-row>
            <v-col style="padding-left: 4%;">
              <h3 class="text-subtitle-1"> Mobile number : {{ pdata.mob }}</h3>
              <h3 class="text-subtitle-1"> PAN Number : {{ pdata.pan }}</h3>
              <h3 class="text-subtitle-1"> Company Name : {{ pdata.company_name }}</h3>
              <h3 class="text-subtitle-1"> Designation : {{ pdata.designation }}</h3>
              <h3 class="text-subtitle-1"> Status : {{ pdata.status }}</h3>
            </v-col>
            <v-col >
              <v-container v-if="pending">
                <v-icon x-large>mdi-av-timer</v-icon>
              </v-container>
              <v-container v-if="verified">
                <v-icon x-large>mdi-check-decagram</v-icon>

              </v-container>
            </v-col>

          </v-row>
        </v-container>
      </v-card-content>



    </v-card>

  </v-container>
</template>

<script>
export default{
name: 'userprofile',
async mounted (){
  this.$vuetify.theme.dark =false;
  this.email = this.$storage.getUniversal('login_mail')
  let url = "http://127.0.0.1:8000/user"
  let res = await this.$axios.get(url,{params:{ email :this.email}});
  this.pdata=res.data
  console.log(this.pdata)
  if (this.pdata.status == "pending"){
    this.pending = true
    this.verified = false
  }
  if(this.pdata.status == "verified"){
    this.verified = true
    this.pending = false
  }



},
data: () =>({
  email:"",
  pdata :{},
  pending: false,
  verified: false,
}),
}
</script>

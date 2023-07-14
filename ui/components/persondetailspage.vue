<template>
  <v-container style="width: 100%; ">
    <v-card>
      <v-card-title>Personal Details</v-card-title>
      <v-card-content>
        <v-container v-if="data_s">
          <v-row>
            <v-col style="padding-left: 4%;">
              <h3 class="text-subtitle-1"> Mobile number : {{ pdata.mob }}</h3>
              <h3 class="text-subtitle-1"> PAN Number : {{ pdata.pan }}</h3>
              <h3 class="text-subtitle-1"> Company Name : {{ pdata.company_name }}</h3>
              <h3 class="text-subtitle-1"> Designation : {{ pdata.designation }}</h3>
              <br>
              <h6 class="text-subtitle-3"> Submitted on : {{ pdata.submitted_on }}</h6>
              <h6 v-if="pdata.edited_on" class="text-subtitle-3"> Edited on : {{ pdata.edited_on }}</h6>
              <h6 v-if="pdata.approved_on, verified" class="text-subtitle-3"> Approved on : {{ pdata.approved_on }}</h6>




            </v-col>
            <v-col >
              <v-container v-if="pending" class="text-center">
              </v-container>
              <v-container v-if="pdata.status == 'verified'" class="text-center">
                <v-icon size="100px" color="green">mdi-check-decagram</v-icon>
              </v-container>
              <v-container v-if="pdata.status == 'rejected'" class="text-center">
                <v-icon size="90px" color="red">mdi-cancel</v-icon>
                <br>
                <v-btn color="indigo darken-3" style="color: white;" @click="edit()">EDIT</v-btn>
              </v-container>

            </v-col>


          </v-row>
        </v-container>
      </v-card-content>
      <v-card-action >
        <v-container v-if="data_">
          <v-btn text icon @click="addpersonal()"><v-icon color="indigo darken-4">mdi-plus</v-icon></v-btn>

        </v-container>

      </v-card-action>


    </v-card>

  </v-container>
</template>

<script>
export default{
name: 'userprofile',
async mounted (){
  this.$vuetify.theme.dark =false;
  this.email = this.$storage.getUniversal('login_mail')
  let url = "http://127.0.0.1:8000/personal"
  let res = await this.$axios.get(url,{params:{ email :this.email}});
  this.pdata=res.data
  console.log(this.pdata)

  if(this.pdata == false){
        this.data_ = true,
        this.data_s = false
      }
      else{
        this.data_s = true,
        this.data_ = false
      }
  if (this.pdata.status == "pending"){
          this.pending = true
          this.verified = false
          this.rejected = false
        }
        if(this.pdata.status == "verified"){
          this.verified = true
          this.pending = false
          this.rejected = false
        }
        if(this.pdata.status == "rejected"){
          this.rejected = true
          this.pending = false
          this.verified = false
        }


},
data: () =>({
  email:"",
  pdata :{},
  pending: false,
  verified: false,
  rejected: false,
  data_: false,
  data_s: false
}),
methods:{
  async edit(){
    this.$router.push("/personal_edit")
  },
  async addpersonal(){
    this.$router.push('/onboard')
  }
}
}
</script>

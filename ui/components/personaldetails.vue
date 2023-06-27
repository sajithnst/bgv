<template>


        <v-container style="width: 100%; ">
          <v-card>
            <v-card-title>Personal Details</v-card-title>
            <v-card-content>
              <v-container>
                <v-row>
                  <v-col style="padding-left: 4%;">
                    <h3 class="text-subtitle-1"> Aadhaar Number : {{ pdata.aadhaar }} </h3>
                    <h3 class="text-subtitle-1"> Mobile number : {{ pdata.mob }}</h3>
                    <h3 class="text-subtitle-1"> PAN Number : {{ pdata.pan }}</h3>
                    <h3 class="text-subtitle-1"> Company Name : {{ pdata.company_name }}</h3>
                    <h3 class="text-subtitle-1"> Designation : {{ pdata.designation }}</h3>
                    <br>
          <h6 class="text-subtitle-3"> Submitted on : {{ pdata.submitted_on }}</h6>
              <h6 v-if="pdata.edited_on" class="text-subtitle-3"> Edited on : {{ pdata.edited_on }}</h6>
              <h6 v-if="pdata.approved_on" class="text-subtitle-3"> Approved on : {{ pdata.approved_on }}</h6>


                  </v-col>
                  <v-col >
                    <v-container v-if="pending" class="text-center">
                      <v-icon size="150px" color="yellow" ></v-icon>
                    </v-container>
                    <v-container v-if="verified" class="text-center">
                      <v-icon size="150px" color="green">mdi-check-decagram</v-icon>
                    </v-container>
                    <v-container v-if="rejected" class="text-center">
                      <v-icon size="150px" color="red">mdi-cancel</v-icon>
                    </v-container>
                  </v-col>
                </v-row>
              </v-container>
              <v-row>
                <v-container>
                  <br>
                  &emsp;&emsp;

                  <v-btn color="indigo darken-4" style="color:white;" @click="approve(pdata.email, ndata.name)">Approve</v-btn>&emsp;

                  <v-btn color="indigo darken-4" style="color:white;" @click="deny(pdata.email, ndata.name)">Reject</v-btn>

                </v-container>
              </v-row>


            </v-card-content>

          </v-card>


        </v-container>
</template>

<script>
export default{
    name: 'userprofile',
    async mounted (){
        this.$vuetify.theme.dark =false;
        this.email = this.$storage.getUniversal('user_email')
        let url = "http://127.0.0.1:8000/personal"
        let res = await this.$axios.get(url,{params:{ email :this.email}});
        this.pdata=res.data

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

        this.notary = this.$storage.getUniversal('notaryemail')
        let nurl = "http://127.0.0.1:8000/notary"
        let nres = await this.$axios.get(nurl,{params:{email: this.notary}})
        this.ndata = nres.data
        console.log(this.pdata)

    },
    data: () =>({
        email:"",
        pdata :{},
        ndata:{},
        error: false,
        success: false,
        pending: false,
        verified: false,
        rejected: false
    }),
    methods:{
      async approve(email, name){
        let url = "http://127.0.0.1:8000/verify/personaldetails"
        let verify={
          user_email: email,
          notary_email: this.ndata.email,
          notary_name: name
        }
        let res = this.$axios.post(url,verify)
        window.location.reload()

      },
      async deny(email, name){
        console.log(email, name)
        let url = "http://127.0.0.1:8000/verify/personaldetails"
        let reject={
          user_email: email,
          notary_email: this.ndata.email,
          notary_name: name,
          status: "rejected"
        }
        let res = this.$axios.post(url,reject)
        window.location.reload()

    }
  }
}
</script>

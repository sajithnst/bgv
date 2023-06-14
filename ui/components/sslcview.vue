<template>
  <v-container style="width: 100%; ">
    <v-card>
      <v-card-title>SSLC Details</v-card-title>
      <v-card-content>
        <v-container>
          <v-row>
            <v-col style="padding-left: 4%;">
              <h3 class="text-subtitle-1"> Register Number :{{ data.regno}}</h3>
           <h3 class="text-subtitle-1"> Marks : {{ data.marks }}</h3>
           <h3 class="text-subtitle-1"> School : {{ data.school }} </h3>
           <h3 class="text-subtitle-1"> Board : {{ data.board }}</h3>
           <h3 class="text-subtitle-1"> Year of Completion : {{ data.passout }}</h3>

            </v-col>
            <v-col style="margin-top: -7%;" >
              <v-container v-if="pending" class="text-center">
                <v-icon size="100px" color="yellow" >mdi-timer</v-icon>
              </v-container>
              <v-container v-if="verified" class="text-center">
                <v-icon size="100px" color="green">mdi-check-decagram</v-icon>
              </v-container>
              <v-container v-if="rejected" class="text-center">
                <v-icon size="100px" color="red">mdi-cancel</v-icon>
              </v-container>

              <v-container class="text-center">
                <v-card-action>
                  <v-btn color="indigo darken-4" style="color: white;" @click="doc(data.email, data.regno)">Document</v-btn>
                </v-card-action>
                <v-container>

                  <v-btn icon @click="approve(data.email, data.regno)"><v-icon size="40px" color="green">mdi-account-check-outline</v-icon></v-btn>&emsp;&emsp;
                <v-btn icon @click="deny(data.email, data.regno)"><v-icon size="40px" color="error">mdi-account-remove-outline</v-icon></v-btn>
                </v-container>
              </v-container>

            </v-col>
          </v-row>
        </v-container>
      </v-card-content>
      <v-alert border="top" color="red lighten-1" dismissible  v-if="error"> No Documents uploaded</v-alert>



    </v-card>


       </v-container>
</template>
<script>
export default{
   name: 'userprofile',
   async mounted (){
       this.$vuetify.theme.dark =false;
       this.email = this.$storage.getUniversal('user_email')
       let url = "http://127.0.0.1:8000/sslc"
       let res = await this.$axios.get(url,{params:{email: this.email}})
       this.data= res.data

       this.notary = this.$storage.getUniversal('notaryemail')
       let nurl = "http://127.0.0.1:8000/notary"
        let nres = await this.$axios.get(nurl,{params:{email: this.notary}})
        this.ndata = nres.data

        if (this.data.status == false){
          this.pending = true
          this.verified = false
          this.rejected = false
        }
        if(this.data.status == "verified"){
          this.verified = true
          this.pending = false
          this.rejected = false
        }
        if(this.data.status == "rejected"){
          this.rejected = true
          this.pending = false
          this.verified = false
        }

   },
   data: () =>({
       email:"",
       data:{},
       pending: false,
       error:false,
       verified: false,
       rejected: false
   }),
   methods:{
    async doc(email, regno){
      let url = "http://127.0.0.1:8000/getpdf"

      this.$axios.get(url,{
        params:{
          email: email,
          regno: regno
        },
        responseType: 'arraybuffer'
      })
      .then(response => {
        console.log(response)
        if(response.data == false){
          this.error == true
        }
        else{
          this.error = false
          let blob = new Blob([response.data], { type: 'application/pdf'}),
        url = window.URL.createObjectURL(blob)

        window.open(url)
        }
      })
      console.log(regno)
    },
    async approve(email, regno){
      let url = "http://127.0.0.1:8000/verify/sslc"
      let vdata={
        user_email: email,
        regno: regno,
        notary_email: this.ndata.email,
        notary_name: this.ndata.name
      }
      let res = await this.$axios.post(url, vdata)
      console.log(res.data)

    },
    async deny(email, regno){
        console.log(email, name)
        let url = "http://127.0.0.1:8000/verify/sslc"
        let reject={
          user_email: email,
          regno: regno,
          notary_email: this.ndata.email,
          notary_name: this.ndata.name,
          status: "rejected"
        }
        let res = this.$axios.post(url,reject)
    }
   }
}
</script>

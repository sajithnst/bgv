<template>
    <v-container style="width: 100%; ">
      <v-card>
        <v-card-title>HSE Details</v-card-title>
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
              <v-col >
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

                    <v-btn icon @click="approve(data.email, data.regno, ndata.name)"><v-icon size="40px" color="green">mdi-account-check-outline</v-icon></v-btn>&emsp;&emsp;
                  <v-btn icon @click="deny(data.email, data.regno, ndata.name)"><v-icon size="40px" color="error">mdi-account-remove-outline</v-icon></v-btn>
                  </v-container>
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
    name: 'hse',
    async mounted (){
        this.$vuetify.theme.dark =false;
        this.email = this.$storage.getUniversal('user_email')
        let url = "http://127.0.0.1:8000/hse"
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
        ndata: {},
        pending: false,
        verified: false,
        rejected: false
    }),
    methods:{
    async doc(email, regno){
      this.$axios.get("http://127.0.0.1:8000/getpdf",{
        params:{
          email: email,
          regno: regno
        },
        responseType: 'arraybuffer'
      })
      .then(response => {
        console.log(response)

        let blob = new Blob([response.data], { type: 'application/pdf'}),
        url = window.URL.createObjectURL(blob)

        window.open(url)
      })
      console.log(regno)

    },
    async approve(email, regno, name){
      let url= "http://127.0.0.1:8000/verify/hse"
      let verify = {
        user_email: email,
        regno: regno,
        notary_email: this.ndata.email,
        notary_name: name
      }
      let res = this.$axios.post(url, verify)

    },
    async deny(email, regno, name){
        console.log(email, name)
        let url = "http://127.0.0.1:8000/verify/hse"
        let reject={
          user_email: email,
          regno: regno,
          notary_email: this.ndata.email,
          notary_name: name,
          status: "rejected"
        }
        let res = this.$axios.post(url,reject)
    }
   }
}
</script>

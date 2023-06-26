<template>
  <v-container style="width: 100%; " v-if="data_s">
    <v-card>
      <v-card-title>PG Details</v-card-title>
      <v-card-content>
        <v-container >
          <v-row>
            <v-col style="padding-left: 4%; ">
              <h3 class="text-subtitle-1"> Register Number :{{ data.regno}}</h3>
          <h3 class="text-subtitle-1"> Marks : {{ data.marks }}</h3>
          <h3 class="text-subtitle-1"> Specialization : {{ data.specialization }}</h3>
          <h3 class="text-subtitle-1"> College : {{ data.college }} </h3>
          <h3 class="text-subtitle-1"> University : {{ data.university }}</h3>
          <h3 class="text-subtitle-1"> Year of Completion : {{ data.passout }}</h3>
          <br>
          <h6 class="text-subtitle-3"> Submitted on : {{ data.submitted_on }}</h6>
              <h6 v-if="data.edited_on" class="text-subtitle-3"> Edited on : {{ data.edited_on }}</h6>

            </v-col>
            <v-col>
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
      </v-card-content>
      <v-row>
        <v-container>
          <br>
          &emsp;&emsp;
          <v-btn color="indigo darken-4" style="color:white;" @click="approve(data.email, data.regno, ndata.name)">Approve</v-btn>&emsp;
          <v-btn color="indigo darken-4" style="color:white;" @click="deny(data.email, data.regno, ndata.name)">Reject</v-btn>&emsp;
          <v-btn color="indigo darken-4" style="color: white;" @click="doc(data.email, data.regno)">Document</v-btn>
        </v-container>
      </v-row>
    </v-card>

      </v-container>
</template>
<script>
export default{
  name: 'hse',
  async mounted (){
      this.$vuetify.theme.dark =false;
      this.email = this.$storage.getUniversal('user_email')
      let url = "http://127.0.0.1:8000/pg"
      console.log(this.email)
      let res = await this.$axios.get(url,{params:{email: this.email}})
      this.data= res.data
      console.log(this.data)

      if(this.data == false){
        this.data_ = true,
        this.data_s = false
      }
      else{
        this.data_s = true,
        this.data_ = false
      }

      this.notary = this.$storage.getUniversal('notaryemail')
        let nurl = "http://127.0.0.1:8000/notary"
        let nres = await this.$axios.get(nurl,{params:{email: this.notary}})
        this.ndata = nres.data


      console.log(this.data)
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
      data:{

      },
      pending: false,
      verified: false,
      rejected: false,
      data_: false,
      data_s: false


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
      let url = "http://127.0.0.1:8000/verify/pg"
      let verify={
        user_email: email,
        regno: regno,
        notary_email: this.ndata.email,
        notary_name: name
      }
      let res = await this.$axios.post(url, verify)
      window.location.reload()

    },
    async deny(email, regno, name){
        console.log(email, name)
        let url = "http://127.0.0.1:8000/verify/pg"
        let reject={
          user_email: email,
          regno: regno,
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

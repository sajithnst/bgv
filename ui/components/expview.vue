<template>
  <v-container style="width: 100%; " v-if="data_s">
    <v-card>
      <v-card-title>Exp Details</v-card-title>
      <v-card-content v-for="data in datas" :key="data.email">
        <v-container >
          <v-row>
            <v-col style="padding-left: 4%; ">
              <h3 class="text-subtitle-1"> Emp ID :{{ data.empid}}</h3>
           <h3 class="text-subtitle-1"> Company : {{ data.company_name }}</h3>
           <h3 class="text-subtitle-1"> Start Date : {{ data.start_date }} </h3>
           <h3 class="text-subtitle-1"> End Date : {{ data.end_date }}</h3>
           <h3 class="text-subtitle-1"> Designation : {{ data.designation }}</h3>
           <br>
          <h6 class="text-subtitle-3"> Submitted on : {{ data.submitted_on }}</h6>
          <h6 v-if="data.edited_on" class="text-subtitle-3"> Edited on : {{ data.edited_on }}</h6>
          <h6 v-if="data.approved_on" class="text-subtitle-3"> Approved on : {{ data.approved_on }}</h6>


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
        <v-row>
          <v-container>
            &emsp;&emsp;
            <v-btn color="indigo darken-4" style="color: white;"  @click="approve(data.email, data.empid, ndata.name)">Approve</v-btn>&emsp;
            <v-btn color="indigo darken-4" style="color: white;"  @click="deny(data.email, data.empid, ndata.name)">Reject</v-btn>&emsp;
            <v-btn color="indigo darken-4" style="color: white;" @click="doc(data.email, data.empid)">Document</v-btn>
          </v-container>
        </v-row>
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
      let url = "http://127.0.0.1:8000/exp"
      console.log(this.email)
      let res = await this.$axios.get(url,{params:{email: this.email}})
      this.datas= res.data
      console.log(this.datas)

      if(this.datas == false){
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


      console.log(this.datas)
      if (this.datas.status == false){
          this.pending = true
          this.verified = false
          this.rejected = false
        }
        if(this.datas.status == "verified"){
          this.verified = true
          this.pending = false
          this.rejected = false
        }
        if(this.datas.status == "rejected"){
          this.rejected = true
          this.pending = false
          this.verified = false
        }
  },
  data: () =>({
      email:"",
      data:[],
      pending: false,
      verified: false,
      rejected: false,
      data_: false,
      data_s: false


  }),
  methods:{
    async doc(email, empid){
      this.$axios.get("http://127.0.0.1:8000/getpdf",{
        params:{
          email: email,
          empid: empid
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
    async approve(email, empid, name){
      let nurl = "http://127.0.0.1:8000/exp/inprogress"
      let data={
        'email':this.email,
      }
      let nres= await this.$axios.post(nurl,data)

      
       
      
      let url = "http://127.0.0.1:8000/verify/exp"
      let verify={
        user_email: email,
        empid: empid,
        notary_email: this.ndata.email,
        notary_name: name
      }
      let res = await this.$axios.post(url, verify)
      window.location.reload()

    },
    async deny(email, empid, name){
        console.log(email, name)
        let url = "http://127.0.0.1:8000/verify/exp"
        let reject={
          user_email: email,
          empid: empid,
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

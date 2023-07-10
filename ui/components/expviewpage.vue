<template>
  <v-container style="width: 100%; ">
    <v-container>
      <v-switch
      v-model="expshow"
      hide-details
      inset
      label="I am Fresher"
      >

      </v-switch>
    </v-container>

    <v-card v-if="!expshow">
      <v-card-title>Experience Details</v-card-title>
      <v-card-content  v-for="data in datas" :key="data.email">
        <v-container v-if="data_s">
          <v-row>
            <v-col style="padding-left: 4%;">
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
            <v-col style="margin-top: -5%;">
              <v-container v-if="pending" class="text-center">
                <v-icon size="100px" color="yellow" ></v-icon>
              </v-container>
              <v-container v-if="data.status == 'verified'" class="text-center">
                <v-icon size="100px" color="green">mdi-check-decagram</v-icon>
              </v-container>
              <v-container v-if="data.status == 'rejected'" class="text-center">
                <v-icon size="100px" color="red">mdi-cancel</v-icon>
                <br>
                <v-btn color="indigo darken-3" style="color: white;" @click="edit()">EDIT</v-btn>
              </v-container>

              

            </v-col>
          </v-row>
          <v-row>
            <v-container>
              &emsp;&emsp;
              <v-btn text outlined color="indigo darken-4" style="color: white;" @click="doc(data.email, data.empid)">Document</v-btn>
            </v-container>
          </v-row>
        </v-container>
        

        
      </v-card-content>
      <v-card-action >
        <v-container v-if="data_">
          <v-btn text icon @click="addsslc()"><v-icon color="indigo darken-4">mdi-plus</v-icon></v-btn>

        </v-container>
        <v-container v-if="data_s">
          <v-btn text icon @click="addsslc()"><v-icon color="indigo darken-4">mdi-plus</v-icon></v-btn>
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
       let url = "http://127.0.0.1:8000/exp"
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


   },
   data: () =>({
       email:"",
       datas:[],
       pending: false,
       verified: false,
       rejected: false,
       data_s: false,
       data_: false,
       expshow: false

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
    async edit(){
      this.$router.push('/exp_edit')
    },
    async addsslc(){
      this.$router.push('/exppage')
    }
   }
}
</script>

<template>
  <v-container style="width: 100%; ">
    <v-card>
      <v-container v-if="data_">
        <h6 class="text-subtitle-3" style="color:red">*UG Data is mandatory.</h6>
      </v-container>
      <v-card-title>UG Details</v-card-title>
      <v-card-content>
        <v-container v-if="data_s">
          <v-row>
            <v-col style="padding-left: 4%; ">
              <h3 class="text-subtitle-1"> Register Number :{{ data.ug_regno}}</h3>
          <h3 class="text-subtitle-1"> Marks : {{ data.ug_marks }}</h3>
          <h3 class="text-subtitle-1"> Specialization : {{ data.ug_specialization }}</h3>
          <h3 class="text-subtitle-1"> College : {{ data.ug_college }} </h3>
          <h3 class="text-subtitle-1"> University : {{ data.ug_university }}</h3>
          <h3 class="text-subtitle-1"> Year of Completion : {{ data.ug_passout }}</h3>
          <br>
          <h6 class="text-subtitle-3"> Submitted on : {{ data.submitted_on }}</h6>
          <h6 v-if="data.edited_on" class="text-subtitle-3"> Edited on : {{ data.edited_on }}</h6>
          <h6 v-if="data.approved_on, verified" class="text-subtitle-3"> Approved on : {{ data.approved_on }}</h6>


            </v-col>
            <v-col >
              <v-container v-if="pending" class="text-center">
                <v-icon size="150px" color="yellow" ></v-icon>
              </v-container>
              <v-container v-if="data.status == 'verified'" class="text-center">
                <v-icon size="150px" color="green">mdi-check-decagram</v-icon>

              </v-container>
              <v-container v-if="data.status == 'rejected'" class="text-center">
                <v-icon size="150px" color="red">mdi-cancel</v-icon>
                <br>
                <v-btn color="indigo darken-3" style="color: white;" @click="edit()">EDIT</v-btn>

              </v-container>


            </v-col>

          </v-row>
          <v-row>
            <v-container v-if="this.datapdf == 'True' || show">
              &emsp;&emsp;
              <v-btn size="30%" text outlined color="indigo darken-4" style="color: white;" @click="doc(data.email, data.ug_regno)">Document</v-btn>
  
            </v-container>
          </v-row>
          <v-row>
            <v-col v-if="this.datapdf == 'False'  &&!isLoading">
           
                <v-file-input  style="width:60%;" @change="fileselect"  label = "Upload UG doc" ></v-file-input>
      
            </v-col>
            <v-col>
              <v-container v-if="this.datapdf == 'False'  &&!isLoading">
                <v-btn size="30%" v-on:click="show = true"  :loading="isLoading" :disabled="isLoading"  text outlined color="indigo darken-4" style="color: white;" @click="upload()">Upload</v-btn>
              </v-container>
            </v-col>
          </v-row>

        </v-container>'
        
      </v-card-content>

      <v-card-action >
        <v-container v-if="data_">
          <v-btn text icon @click="addug()"><v-icon color="indigo darken-4">mdi-plus</v-icon></v-btn>

        </v-container>

      </v-card-action>

    </v-card>

      </v-container>
</template>
<script>
export default{
  name: 'hse',
  async mounted (){
      this.$vuetify.theme.dark =false;
      this.email = this.$storage.getUniversal('login_mail')
      let url = "http://127.0.0.1:8000/ug"
      console.log(this.email)
      let res = await this.$axios.get(url,{params:{email: this.email}})
      this.data= res.data
      this.regno = res.data.ug_regno
      console.log(this.data)

      if(this.data == false){
        this.data_ = true,
        this.data_s = false
      }
      else{
        this.data_s = true,
        this.data_ = false
      }

        let nurl = "http://127.0.0.1:8000/checkpdf"
      let nres = await this.$axios.get(nurl,{params:{email: this.email, regno: this.regno}})
      this.datapdf = nres.data

  },
  data: () =>({
      email:"",
      regno:"",
      datapdf:"",
      isLoading: false,
      data:{

      },
      pending: false,
      verified: false,
      rejected: false,
      data_: false,
      data_s: false,
      show: false

  }),
  methods:{
    async fileselect(event){
      this.file=event
    },
    async upload(){
      let nurl = "http://127.0.0.1:8000/user/expupdation"
        let ndata={
          'email': this.email
        }
        let nres = await this.$axios.post(nurl, ndata)
        
            let formdata= new FormData()
            formdata.append('email',this.email)
            formdata.append('sslc_regno',this.regno)
            formdata.append('file',this.file)
            let furl = "http://127.0.0.1:8000/uploadsslcpdf"
            let res = await this.$axios.post(furl,formdata,{ headers : {'Content-Type': 'application/json',}});
            
            this.isLoading = true;
            // Simulate an asynchronous operation, such as an API call
     
   },
    async doc(email, ug_regno){
      this.$axios.get("http://127.0.0.1:8000/getpdf",{
        params:{
          email: email,
          regno: this.regno
        },
        responseType: 'arraybuffer'
      })
      .then(response => {
        console.log(response)

        let blob = new Blob([response.data], { type: 'application/pdf'}),
        url = window.URL.createObjectURL(blob)

        window.open(url)
      })
      console.log(ug_regno)

    },
    async addug(){
      this.$router.push('/ugpage')
    },
    async edit(){
      this.$router.push('/ug_edit')
    }
   }
}
</script>

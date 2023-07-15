<template>
  <v-container style="width: 100%; ">
    <v-container>
      <v-switch
      v-model="pgshow"
      hide-details inset
      label="Not Applicable"
      >

      </v-switch>
    </v-container>
    <v-card v-if="!pgshow">
      <v-card-title>PG Details</v-card-title>
      <v-card-content>
        <v-container v-if="data_s">
          <v-row>
            <v-col style="padding-left: 4%; ">
              <h3 class="text-subtitle-1"> Register Number :{{ data.pg_regno}}</h3>
          <h3 class="text-subtitle-1"> Marks : {{ data.pg_marks }}</h3>
          <h3 class="text-subtitle-1"> Specialization : {{ data.pg_specialization }}</h3>
          <h3 class="text-subtitle-1"> College : {{ data.pg_college }} </h3>
          <h3 class="text-subtitle-1"> University : {{ data.pg_university }}</h3>
          <h3 class="text-subtitle-1"> Year of Completion : {{ data.pg_passout }}</h3>
          <br>
          <h6 class="text-subtitle-3"> Submitted on : {{ data.submitted_on }}</h6>
          <h6 v-if="data.edited_on" class="text-subtitle-3"> Edited on : {{ data.edited_on }}</h6>
          <h6 v-if="data.approved_on, verified" class="text-subtitle-3"> Approved on : {{ data.approved_on }}</h6>

            </v-col>
            <v-col >
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
            <v-container v-if="this.datapdf == 'True'">
              &emsp;&emsp;
    
              <v-btn text outlined color="indigo darken-4" style="color: white;" @click="doc(data.email, data.pg_regno)">Document</v-btn>
    
            </v-container>
          </v-row>
          <v-row>
            <v-col v-if="this.datapdf == 'False'">
           
                <v-file-input  style="width:60%;" @change="fileselect"  label = "Upload PG doc" ></v-file-input>
      
            </v-col>
            <v-col>
              <v-container v-if="this.datapdf == 'False'">
                <v-btn  :loading="isLoading" :disabled="isLoading"  text outlined color="indigo darken-4" style="color: white;" @click="upload()">Upload</v-btn>
              </v-container>
            </v-col>
          </v-row>
        </v-container>
        

        
      </v-card-content>
      

      <v-card-action >
        <v-container v-if="data_">
          <v-btn text icon @click="addpg()"><v-icon color="indigo darken-4">mdi-plus</v-icon></v-btn>

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
      let url = "http://127.0.0.1:8000/pg"
      console.log(this.email)
      let res = await this.$axios.get(url,{params:{email: this.email}})
      this.data= res.data
      this.regno = res.data.pg_regno
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
      data:{

      },
      isLoading: false,

      pending: false,
      verified: false,
      rejected: false,
      data_: false,
      data_s: false,
      pgshow: false

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
            setTimeout(() => {
              // After the operation is complete, set isLoading to false
              this.isLoading = false;
              location.reload();
            }, 2000);
   },
    async doc(email, pg_regno){
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
      console.log(pg_regno)

    },
    async addpg(){
      this.$router.push('/pgpage')
    },
    async edit(){
      this.$router.push('/pg_edit')
    }
   }
}
</script>

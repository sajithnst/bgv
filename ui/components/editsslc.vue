<template>
  <v-container class="personalform" >
  <v-form v-model="formvalid" >
      <br/>
      <h3 class="text-center"> SSLC Details</h3>
      <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
      <v-alert class="success" dismissible v-if="success"> Data insertion succeeded</v-alert>
      <v-text-field label="Registration Number" v-model="sslc_regno" :rules="[rules.required,rules.sslc_regno]"></v-text-field>
      <v-text-field label="Marks in %" v-model="sslc_marks" :rules="[rules.required,rules.percents]"></v-text-field>
      <v-text-field label="School" v-model="sslc_school" :rules="[rules.required,rules.sslc_school]"></v-text-field>
     <v-text-field label="Board" v-model="sslc_board" :rules="[rules.required,rules.sslc_board]"></v-text-field>
     <v-select
     v-model="sslc_passout"
     :items="sslc_passout"
     label="Year of Completion"
     :rules="[rules.required]"
     prepend-icon="mdi-calendar"
   ></v-select>
      <v-file-input @change="fileselect"  label = "Upload Files" :rules="[rules.required]" ></v-file-input>
      <v-container class="text-center">
          <v-btn text  @click="submit()" color="indigo lighten-2"> Submit </v-btn>
      </v-container>
  </v-form>
</v-container>
</template>
<script>
export default{
  name: "sslc",
  async mounted(){
      var url ='http://127.0.0.1:8000/user'
      this.generateYearRange();
      this.email= await this.$storage.getUniversal('Email');
      await this.$axios.get(url,{params:{email : this.email}}).then(res=>{
          this.name = res.data.name
      }).catch(error => console.log(error));

  },
  data : () => ({
      formvalid: false,
      sslc_regno : '',
      email : '',
      sslc_marks : '',
      sslc_school : '',
      sslc_passout: '',
      success: null,
      name : '',
      fail : null,
      sslc_board : '',
      rules : {
        required: (v) => !!v || "Required",
            percents : (v) => (v>=0 && v<=100) || "Value must be between 0 and 100",
            email : (v) => v.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/) || "Email format is wrong",
            name : (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters in Name",
            sslc_regno : (v) => v.match(/^[a-zA-Z0-9]+$/) || "Register number format is wrong",
            sslc_school : (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters",
            sslc_board : (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters",
        },
        sslc_passout: [],
      
  }),
  methods:{
      async fileselect(event){
    this.file=event
  },
      async submit(){
        let nurl = "http://127.0.0.1:8000/user/expupdation"
        let ndata={
          'email': this.email
        }
        let nres = await this.$axios.post(nurl, ndata)
        
          let url ="http://127.0.0.1:8000/sslcupdate"
          let sslcdata = {
              sslc_regno : this.sslc_regno,
              email : this.email,
              sslc_marks : this.sslc_marks,
              sslc_school : this.sslc_school,
              sslc_passout : this.sslc_passout,
              name : this.name,
              sslc_board : this.sslc_board
          }
          let result = await this.$axios.post(url,sslcdata);
          console.log(result.data);
          let formdata= new FormData()
          formdata.append('email',this.email)
          formdata.append('sslc_regno',this.sslc_regno)
          formdata.append('file',this.file)
          let furl = "http://127.0.0.1:8000/uploadsslcpdf"
          let res = await this.$axios.post(furl,formdata,{ headers : {'Content-Type': 'application/json',}});
          if (res.data === result.data){
              this.$router.push('/user')
          }
          else{
              this.fail =true
          }
      },
    generateYearRange() {
      const currentYear = new Date().getFullYear();
      const startYear = currentYear - 50;

      for (let year = currentYear; year >= startYear; year--) {
        this.sslc_passout.push(year);
      }
    },
  
  }

}
</script>
<style scoped>
.v-menu__content {
  max-height: 200px;
  overflow-y: auto;
}
</style>
<template>
  <v-container class="personalform">
      <v-form>
          <h3 class="text-center"> Last Experience Details</h3>
          <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
          <v-text-field label="Employee ID"
          v-model="empid"
          :rules="[rules.required]"></v-text-field>
          <v-text-field label="Company Name" v-model="company" :rules="[rules.required]"></v-text-field>
          <v-text-field label="HR Email" v-model="hr_mail" :rules="[,rules.email,rules.required]"></v-text-field>
          <v-text-field label="Start Date (DD/MM/YYYY)" v-model="start_date" :rules="[rules.required,rules.date]"></v-text-field>
          <v-text-field label="End Date (DD/MM/YYYY)" v-model="end_date" :rules="[rules.required,rules.date]"></v-text-field>
          <v-text-field label="Designation" v-model="designation" :rules="[rules.required]"></v-text-field>
          <v-text-field label="CTC (Cost To Company)" v-model="lpa" :rules="[rules.required]"></v-text-field>
          <v-text-field label="Reporting Manager" v-model="reporting_manager" :rules="[rules.required]"></v-text-field>
          <v-file-input @change="fileselect" label="Experience Letter as PDF" :rules="[rules.required]"></v-file-input>
          <v-container class="text-center">
              <v-btn text  @click="submit()" color="indigo lighten-2"> Submit </v-btn>
          </v-container>
          <v-container class="text-center">
              <v-btn text  @click="skip()" color="indigo lighten-2"> I'm a fresher </v-btn>
          </v-container>
      </v-form>
  </v-container>
</template>
<script>
export default{
  name : "exp",
  async mounted(){
      var url ='http://127.0.0.1:8000/user'
      this.email= await this.$storage.getUniversal('Email');
      await this.$axios.get(url,{params:{email : this.email}}).then(res=>{
          this.name = res.data.name
      }).catch(error => console.log(error));

  },
  data : () => ({
      fail: null,
      empid :null,
      name: null,
      email:null,
      company:null,
      hr_mail: null,
      start_date:"",
      end_date:"",
      designation: null,
      lpa:null,
      reporting_manager:null,
      rules : {
          required: (v) => !!v || "Required",
          email : (v) => v.match(/\S+@\S+\.\S+/) || "Email format is wrong",
          percents : (v) => (v>=0 && v<=100) || "Value must be between 0 and 100",
          date : (v) => (v.match(/^\d{2}\/\d{2}\/\d{4}$/)) || "Date format is not correct"
      },
  }),
  methods:{
      async fileselect(event){
    this.file=event
  },
   async submit(){
      let url="http://127.0.0.1:8000/expupdate"
      let edata = {
          empid : this.empid,
          name: this.name,
          email : this.email,
          company : this.company,
          hr_mail : this.hr_mail,
          start_date : this.start_date,
          end_date : this.end_date,
          designation : this.designation,
          lpa : this.lpa,
          reporting_manager: this.reporting_manager
      }
      let result = await this.$axios.post(url,edata);
      let furl = "http://127.0.0.1:8000/uploadexppdf"
      let formdata= new FormData()
          formdata.append('email',this.email)
          formdata.append('empid',this.empid)
          formdata.append('file',this.file)
          let res = await this.$axios.post(furl,formdata,{ headers : {'Content-Type': 'application/json',}});
          if (result.data === res.data){
              this.$router.push('/user')
          }else{
              this.fail= true
          }

   },
   async skip(){
      let url ="http://127.0.0.1:8000/user/firstlogin"
      let response = await this.$axios.get(url,{params:{email:this.email}})
      this.$router.push('/user')
   }
  }
}
</script>

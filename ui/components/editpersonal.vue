<template>
  <v-container class="personalform">
      <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
      <v-form v-model="formValid" >
              <br/>
              <h3 class="text-center"> Personal Data</h3> <br />
              <h5 class="text-center"> Here you have to fill the form again without any mistakes</h5>
              <v-text-field label="Employee ID " v-model="empid" :rules="[rules.required,rules.alphnum]"></v-text-field>
              <v-text-field label="Date of Join (DD/MM/YYYY)(Current Company)" v-model="doj" :rules="[rules.required,rules.date]"></v-text-field>
              <v-text-field label="Company Name " v-model="company" :rules="[rules.required]"></v-text-field>
              <v-text-field label="Designation" v-model="designation" :rules="[rules.required]"></v-text-field>
              <v-text-field label="Company Email" v-model="company_email" :rules="[rules.required,rules.email]"></v-text-field>
              <v-text-field label="Mobile Number" v-model="mob" :rules="[rules.required,rules.mob]"></v-text-field>
              <v-text-field label="Aadhaar" v-model="aadhaar" :rules="[rules.required,rules.aadhaar]"></v-text-field>
              <v-text-field label="PAN" v-model="pan" :rules="[rules.required,rules.pan]"></v-text-field>
              <v-text-field label="Passport" v-model="passport" :rules="[rules.required]"></v-text-field>
              <v-container class="text-center">
                  <v-btn text color="indigo  lighten-2"  @click="submit()" :disabled="!formValid" class="button">submit</v-btn>
              </v-container>

      </v-form>
  </v-container>
</template>
<script>
export default {
  name: 'personaldata',
  async mounted(){
      this.email =  this.$storage.getUniversal('Email');
      console.log(this.email);
  },
  data:() =>({
      empid:"",
      doj:"",
      email:"",
      designation: "",
      company :"",
      company_email:"",
      mob:"",
      aadhaar : "",
      fail: null,
      pan:"",
      passport : "",
      formValid: null,
      rules:{
          required: (v) => !!v || "Required",
          mob: (v) => v.match(/^[0-9]{10}$/) || "check your mobile number",
          aadhaar : (v) =>  v.match(/^\d{12}$/) || "Check the aadhaar number for errors",
          pan : (v) => v.match(/^([A-Z]){5}([0-9]){4}([A-Z]){1}?$/) || "Check the PAN number for errors",
          email : (v) => v.match(/\S+@\S+\.\S+/) || "Email format is wrong",
          name: (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters in Name",
          alphnum: (v) => v.match(/^[A-Za-z0-9\s]+$/) || "No special Characters",
          date : (v) => (v.match(/^\d{2}\/\d{2}\/\d{4}$/)) || "Date format is not correct"

      }
  }),
  methods:{
      async submit(){
          let url = "http://127.0.0.1:8000/personal/update";
          let pdata= {
              empid : this.empid,
              doj : this.doj,
              email:this.email,
              designation :this.designation,
              company_name : this.company,
              company_mail : this.company_email,
              mob : this.mob,
              aadhaar : this.aadhaar,
              pan : this.pan,
              passport: this.passport,
          }
          let result = await this.$axios.post(url, pdata);
          if (result.data == true){
              this.$router.push('/user')
          }else{
              this.fail=true;
          }

      },
  },

}
</script>
<style>
.personalform{
  width: 50%;
}
</style>

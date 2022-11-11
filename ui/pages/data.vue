<template>
<v-app data>
<v-app-bar app>
    <v-btn icon @click="home()"><v-icon size="32">mdi-home</v-icon></v-btn>
    <v-spacer></v-spacer>
    <v-toolbar-title> User Data Collection </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn icon><v-icon size="32">mdi-arrow-left-bold-outline</v-icon></v-btn>
</v-app-bar>
<v-main>
<v-container class="personal">
  <v-form v-model="valid" >
      <v-alert type="error" v-model="fail"> Certificate Upload Failed</v-alert>
      <h1 class="text-center " > Personal Data</h1><br/>
      <v-divider></v-divider><br/>
      <v-col>
        <v-row>
            <v-text-field v-model="empid" label="Employee ID" :rules="[rules.required]"></v-text-field>
        </v-row>
        <v-row>
            <v-text-field v-model="doj" label="Date of Joining ( DD.MM.YYYY)" :rules="[rules.required ,rules.dateformat]"></v-text-field>
        </v-row>
        <v-row>
            <v-text-field v-model="company_mail" label="Official Email" :rules="[rules.required,rules.email]"></v-text-field>
        </v-row>
        <v-row>
            <v-text-field v-model="mob" label="Mobile Number" :rules="[rules.required,rules.number ,rules.mobile]"></v-text-field>
        </v-row>
        <v-row>
            <v-text-field v-model="aadhaar" label="Aadhaar  Number" :rules="[rules.required,rules.number , rules.aadhaar ]"></v-text-field>
        </v-row>
        <v-row>
              <v-text-field v-model="pan" label="PAN  Number" :rules="[rules.required, rules.pan ]"></v-text-field>
        </v-row>
        <v-row>
              <v-text-field v-model="passport" label="Passport Number" :rules="[rules.required, rules.passport]"></v-text-field>
        </v-row>
        <v-row>
              <v-btn :disabled="!valid" block large color="teal" @click="save()">Save </v-btn>
        </v-row>
    
      </v-col>
  </v-form>
  
</v-container>
</v-main>
<h1 class="text-center"></h1>
</v-app>
</template>
<script>
export default{
    name :  "profiledata",
    async mounted(){
      this.email = await this.$storage.getUniversal('Email');
    },
    data : () =>({
      email :'',
      empid :'',
      doj :'',
      company_mail:'',
      valid:'',
      mob:'',
      aadhaar:'',
      pan: '',
      fail : null,
      passport:'',
      rules : {
            required: (v) => !!v || "Required",
            email : (v) => v.match(/\S+@\S+\.\S+/) || "Email format is wrong",
            aadhaar : (v) => v.length ==12 || "length should be 12",
            number: (v) => v.match(/([1-9][0-9]*)|0/) || "Pleas use only numbers",
            mobile : (v) => v.length == 10 || "10 digits is required",
            pan : (v) => v.match(/[A-Z]{5}[0-9]{4}[A-Z]{1}/) || "PAN format is wrong",
            dateformat : (v) => v.match(/[0-9]{2}.[0-9]{2}.[0-9]{4}/) || "Date format is wrong",
            passport : (v) => v.match(/^[A-Z]{1}[0-9]{7}$/) || "Passport is not valid",
            nospecchar: (v) => v.match(/^[A-Za-z]+$/) || "No special Characters allowed"
          
        },
    }),
    methods:{
    
      async save(){
          let url ='http://192.168.26.93:8000/user'
         let p = {
          email : this.email,
          empid : this.empid,
          doj : this.doj,
          company_mail: this.company_mail,
          mob : this.mob,
          aadhaar : this.aadhaar,
          pan : this.pan,
          passport : this.passport

         }
        let res= await this.$axios.put(url,p)
        console.log(res.data)
        if(res.data == true) {
          this.$router.push('/sslc')
        }

      },
      async home(){
        this.$router.push('/signin')
      },
    }

}
</script>
<style>
.personal{
  width: 40%;
  margin: 5% auto;
}
</style>
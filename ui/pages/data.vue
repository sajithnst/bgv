<template>
<v-app data>
<v-app-bar app>
    <v-btn icon><v-icon size="32">mdi-home</v-icon></v-btn>
    <v-spacer></v-spacer>
    <v-toolbar-title> User Data Collection </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn icon><v-icon size="32">mdi-arrow-left-bold-outline</v-icon></v-btn>
</v-app-bar>
<v-main>
<v-container class="personal">
  <v-form v-model="valid" >
      <h1 class="text-center " > Personal Data</h1><br/>
      <v-divider></v-divider><br/>
      <v-col>
        <v-row>
            <v-text-field v-model="empid" label="Employee ID" :rules="[rules.required, rules.nospecchar]"></v-text-field>
        </v-row>
        <v-row>
            <v-text-field v-model="doj" label="Date of Joining" :rules="[rules.required ,rules.nospecchar]"></v-text-field>
        </v-row>
        <v-row>
            <v-text-field v-model="email" label="Personal Email" :rules="[rules.required]"></v-text-field>
        </v-row>
        <v-row>
            <v-text-field v-model="cmail" label="Official Email" :rules="[rules.required,rules.email]"></v-text-field>
        </v-row>
        <v-row>
            <v-text-field v-model="mob" label="Mobile Number" :rules="[rules.required,rules.number ,rules.mobile,rules.nospecchar]"></v-text-field>
        </v-row>
        <v-row>
            <v-text-field v-model="aadhaar" label="Aadhaar  Number" :rules="[rules.required,rules.number , rules.aadhaar ]"></v-text-field>
        </v-row>
        <v-row>
              <v-text-field v-model="pan" label="PAN  Number" :rules="[rules.required, rules.pan ,rules.nospecchar]"></v-text-field>
        </v-row>
        <v-row>
              <v-text-field v-model="passport" label="Passport Number" :rules="[rules.required, rules.passport, rules.nospecchar]"></v-text-field>
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
      cmail:'',
      valid:'',
      mob:'',
      aadhaar:'',
      pan: '',
      passport:'',
      rules : {
            required: (v) => !!v || "Required",
            email : (v) => v.match(/\S+@\S+\.\S+/) || "Email format is wrong",
            aadhaar : (v) => v.length ==12 || "length should be 12",
            number: (v) => v.match(/([1-9][0-9]*)|0/) || "Pleas use only numbers",
            mobile : (v) => v.length == 10 || "10 digits is required",
            pan : (v) => v.length == 10 || "10 Characters is required",
            passport : (v) => v.match(/^[A-Z]{1}[0-9]{7}$/) || "Passport is not valid",
            nospecchar: (v) => v.match(/^[A-Za-z]+$/) || "No special Characters allowed"
          
        },
    }),
    methods:{
      async save(){
        
      }
    }

}
</script>
<style>
.personal{
  width: 30%;
  margin: 5% auto;
}
</style>
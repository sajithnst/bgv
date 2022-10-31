<template>
<v-app >
<v-app-bar app>
    <v-btn icon><v-icon size="32">mdi-home</v-icon></v-btn>
    <v-spacer></v-spacer>
    <v-toolbar-title> User Data Collection </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn icon><v-icon size="32">mdi-arrow-left-bold-outline</v-icon></v-btn>
</v-app-bar>
<v-main>
<v-container class="personal">
  <v-form v-model="isFormvalid" >
      <h1 class="text-center " > Personal Data</h1><br/>
      <v-divider></v-divider><br/>
      <v-col>
        <v-row>
            <v-text-field v-model="empid" label="Employee ID" :rules="[rules.required]"></v-text-field>
        </v-row>
        <v-row>
            <v-text-field v-model="doj" label="Date of Joining" :rules="[rules.required]"></v-text-field>
        </v-row>
        <v-row>
            <v-text-field v-model="email" label="Personal Email" :rules="[rules.required]"></v-text-field>
        </v-row>
        <v-row>
            <v-text-field v-model="cmail" label="Official Email" :rules="[rules.required,rules.email]"></v-text-field>
        </v-row>
        <v-row>
            <v-text-field v-model="mob" label="Mobile Number" :rules="[rules.required]"></v-text-field>
        </v-row>
        <v-row>
            <v-text-field v-model="aadhaar" label="Aadhaar  Number" :rules="[rules.required]"></v-text-field>
        </v-row>
        <v-row>
              <v-text-field v-model="pan" label="PAN  Number" :rules="[rules.required]"></v-text-field>
        </v-row>
        <v-row>
              <v-text-field v-model="passport" label="Passport Number" :rules="[rules.required]"></v-text-field>
        </v-row>
        <v-row>
              <v-btn :disabled="!isFormvalid" block large color="teal" :rules="[rules.required]">Save </v-btn>
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
      email : '',
      rules : {
            required: (v) => !!v || "Required",
            min : (v) =>  v.length > 8 || "Minimun 8 Characters is required",
            email : (v) => v.match(/\S+@\S+\.\S+/) || "Email format is wrong",
        },
    }),
    methods:{

    }

}
</script>
<style>
.personal{
  width: 30%;
  margin: 5% auto;
}
</style>
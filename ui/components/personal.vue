<template>
    <v-container class="personalform">
        <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
        <v-form v-model="isFormValid" >
                <br/>
                <h3 class="text-center"> Personal Data</h3> <br />
                <v-text-field label="Employee ID " v-model="empid" :rules="[rules.required,rules.alphnum]"></v-text-field>
                <v-menu v-model="menu" :close-on-content-click="false" :nudge-right="40" :return-value.sync="doj" transition="scale-transition" offset-y min-width="auto">
                    <template v-slot:activator="{ on }">
                      <v-text-field v-model="formattedDoj" label="Date of Join (Current Company)"  readonly v-on="on"></v-text-field>
                    </template>
                    <v-date-picker v-model="doj" :max="today" no-title scrollable>
                      <v-spacer></v-spacer>
                      <v-btn text color="primary" @click="cancelDate()">Cancel</v-btn>
                      <v-btn text color="primary" @click="saveDate()">OK</v-btn>
                    </v-date-picker>
                  </v-menu>                <v-text-field label="Company Name " v-model="company" :rules="[rules.required,rules.company]"></v-text-field>
                <v-text-field label="Designation" v-model="designation" :rules="[rules.required,rules.designation]"></v-text-field>
                <v-text-field label="Company Email" v-model="company_email" :rules="[rules.required,rules.email]"></v-text-field>
                <v-text-field label="Mobile Number" v-model="mob" :rules="[rules.required,rules.mob]"></v-text-field>
                <v-text-field label="Aadhaar" v-model="aadhaar" :rules="[rules.required,rules.aadhaar]"></v-text-field>
                <v-text-field label="PAN" v-model="pan" :rules="[rules.required,rules.pan]"></v-text-field>
                <v-text-field label="Passport" v-model="passport" :rules="[rules.required,rules.passport]"></v-text-field>
                <v-container class="text-center">
                    <v-btn text color="indigo  lighten-2"  @click="submit()" :disabled="!isFormValid" class="button">Submit</v-btn>
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
        isFormValid: null,
        rules:{
            required: (v) => !!v || "Required",
            mob: (v) => v.match(/^[0-9]{10}$/) || "check your mobile number",
            aadhaar : (v) =>  v.match(/^\d{12}$/) || "Check the aadhaar number for errors",
            pan : (v) => v.match(/^([A-Z]){5}([0-9]){4}([A-Z]){1}?$/) || "Check the PAN number for errors",
            designation : (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters",
            email : (v) => v.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/) || "Email format is wrong",
            company: (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters",
            empid : (v) => v.match(/^[A-Za-z0-9_-]{1,20}$/) || 'Emp ID format is wrong',
            passport : (v) => v.match(/^[A-Za-z0-9]{6,15}$/) || "Passport format is wrong",
            company_email : (v) => v.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/) || "Email format is wrong",
            alphnum: (v) => v.match(/^[A-Za-z0-9\s]+$/) || "No special Characters",
            date : (v) => (v.match(/^\d{2}\/\d{2}\/\d{4}$/)) || "Date format is not correct"

        },
      menu: false,
      today: new Date().toISOString().substring(0, 10),
      formattedDoj:''
    }),
    methods:{
        async submit(){
            let url = "http://127.0.0.1:8000/personal";
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
        cancelDate() {
      this.menu = false;
    },
    saveDate() {
      this.formattedDoj = this.getFormattedDate(this.doj);
      this.menu = false;
    },
    getFormattedDate(date) {
      if (date) {
        const dateObj = new Date(date);
        const day = String(dateObj.getDate()).padStart(2, '0');
        const month = String(dateObj.getMonth() + 1).padStart(2, '0');
        const year = dateObj.getFullYear();
        return `${day}/${month}/${year}`;
      }
      return '';
    },
    },

}
</script>
<style>
.personalform{
    width: 50%;
}
</style>

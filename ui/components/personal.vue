<template>
    <v-container class="personalform">
        <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
        <v-form  >
                <br/>
                <h3 class="text-center"> Personal Data</h3> <br />
                <v-text-field label="Employee ID " v-model="empid" :rules="[rules.required,rules.alphnum]"></v-text-field>
                <v-text-field label="Date of Join (DD/MM/YYYY)" v-model="doj" :rules="[rules.required]"></v-text-field>
                <v-text-field label="Company Email" v-model="company_email" :rules="[rules.required,rules.email]"></v-text-field>
                <v-text-field label="Mobile Number" v-model="mob" :rules="[rules.required,rules.pan]"></v-text-field>
                <v-text-field label="Aadhaar" v-model="aadhaar" :rules="[rules.required,rules.aadhaar]"></v-text-field>
                <v-text-field label="PAN" v-model="pan" :rules="[rules.required,rules.pan]"></v-text-field>
                <v-text-field label="Passport" v-model="passport" :rules="[rules.required]"></v-text-field>
                <v-container class="text-center">
                    <v-btn text color="indigo  lighten-2"  @click="submit()">submit</v-btn>
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
        company_email:"",
        mob:"",
        aadhaar : "",
        fail: null,
        pan:"",
        passport : "",
        rules:{
            required: (v) => !!v || "Required",
            aadhaar : (v) =>  v.length === 12 || "Minimun 12 Characters is required",
            pan : (v) => v.length ===10 || "Minimun 10 characters is required",
            email : (v) => v.match(/\S+@\S+\.\S+/) || "Email format is wrong",
            name: (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters in Name",
            alphnum: (v) => v.match(/^[A-Za-z0-9\s]+$/) || "No special Characters"

        }
    }),
    methods:{
        async submit(){
            let url = "http://127.0.0.1:8000/userupdate";
            let pdata= {
                empid : this.empid,
                doj : this.doj,
                email:this.email,
                company_mail : this.company_email,
                mob : this.mob,
                aadhaar : this.aadhaar,
                pan : this.pan,
                passport: this.passport,
            }
            let result = await this.$axios.post(url, pdata);
            if (result.data == true){
                this.$router.push('/sslcpage')
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
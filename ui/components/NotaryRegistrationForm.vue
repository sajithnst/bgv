<template>
    <v-container class="personalform">
        <v-alert border="top" color="red lighten-1" dismissible  v-if="fail"> Data insertion failed</v-alert>
        <v-form  >
                <br/>
                <h3 class="text-center"> Notary Registration Data</h3> <br />
                <v-text-field label="Name " v-model="name" :rules="[rules.required,rules.name]"></v-text-field>
                <v-text-field label="Email" v-model="email" :rules="[rules.required,rules.email]"></v-text-field>
                <v-text-field label="Enter the password" v-model="password" type="password" :rules="[rules.required,rules.password]"></v-text-field>
                <v-text-field label="Mobile Number" v-model="mob" :rules="[rules.required,rules.mob]"></v-text-field>
                <v-text-field label="Aadhaar" v-model="aadhaar" :rules="[rules.required,rules.aadhaar]"></v-text-field>
                <v-text-field label="PAN" v-model="pan" :rules="[rules.required,rules.pan]"></v-text-field>

                <v-container class="text-center">
                    <v-btn text color="indigo  lighten-2"  @click="submit()">submit</v-btn>
                </v-container>
        
        </v-form>
    </v-container>
</template>
<script>
export default {
    name: 'Notarydata',
    async mounted(){
        this.email =  this.$storage.getUniversal('Email');
        console.log(this.email);
    },
    data:() =>({
        name: "",
        email:"",
        password: "",
        mob:"",
        aadhaar : "",
        fail: null,
        pan:"",
        
        rules:{
            required: (v) => !!v || "Required",
            mob: (v) => v.match(/^[0-9]{10}$/) || "check your mobile number",
            aadhaar : (v) =>  v.match(/^\d{12}$/) || "Check the aadhaar number for errors",
            pan : (v) => v.match(/^([A-Z]){5}([0-9]){4}([A-Z]){1}?$/) || "Check the PAN number for errors",
            email : (v) => v.match(/\S+@\S+\.\S+/) || "Email format is wrong",
            name: (v) => v.match(/^[A-Za-z\s]+$/) || "No special Characters in Name",
            password: (v) =>  v.match(/^(?=.*[A-Z])(?=.*[@])(?=.*[a-z])(?=.*\d).{8,}$/)|| "Enter Password with One Cap letter ,@,small letter and with the number is required",

        }
    }),
    methods:{
        async submit(){
            let url = "http://127.0.0.1:8000/notary";
            let pdata= {
                name:this.name,
                email:this.email,
                password:this.password,
                mob : this.mob,
                aadhaar : this.aadhaar,
                pan : this.pan,
            }
            let result = await this.$axios.post(url, pdata);
            if (result.data == true){
                this.$router.push('/')
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

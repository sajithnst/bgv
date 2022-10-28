<template>
    <v-container>
        <v-form>
            <v-alert v-model="error" type="error"  dismissible>OTP verification failed</v-alert>
            <v-col>
                <v-row>
                    <caption> An OTP is send to your provided email. Please enter the OTP below for verification</caption>
                </v-row>
                <v-row>
                    <v-text-field label ="Enter OTP Here" v-model="utop"></v-text-field>
                </v-row>
                <v-row>
                    <v-btn large block color="teal" @click="submit()">submit</v-btn>
                </v-row>
            </v-col>
           
        </v-form>
    </v-container>
</template>
<script>
export default {
    name : "otpcheck",
    async mounted() {
        this.email = await this.$storage.getUniversal('Email');
        let url = 'http://127.0.0.1:8000/otp'
        await this.$axios.get(url,{ params:{ email : this.email}}).then(res => {
            this.otp = res.data
        }).catch(err => { console.log( err)})
    },
    data : () =>({
        otp :'',
        uotp:'',
        email: '',
        error:false,
    }),
    methods:{
        async submit(){
            if(uotp == otp){
                let url = 'http://127.0.0.1:8000/emailverified'
                await this.$axios.post(url,{params:{ email : this.email}}).then( res => {
                    if (res.data == true){
                        this.$router.push('/data')
                    }
                    else{
                        this.error = true;
                    }
                }
                )
            }
        }
    }
}

</script>
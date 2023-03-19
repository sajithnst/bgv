<template>
    <v-app>
        <v-app-bar app color="indigo darken-4">
            <v-app-bar-title style="color: antiquewhite;">Payments</v-app-bar-title>
        </v-app-bar>
        <v-main>
            <v-container style="width: 50%;margin: 10% auto;">
                <h3 class="text-h6"> Payment Receipt </h3><br/>
                <h3 class="text-subtitle-1"> Data Charges : INR 100 </h3>
                <h3 class="text-subtitle-1"> Platform Service Charges : INR 100 </h3>
                <h3 class="text-subtitle-1"> Blockchain Service Charges : INR 100</h3>
                <h3 class="text-subtitle-1"> Total : INR 300 </h3>
                <br/>
                <v-btn @click="pay()" width="100px" color="success">Pay</v-btn>
                <v-btn @click="decline()" width="100px" color="error">Decline</v-btn>
            </v-container>
        </v-main>
    </v-app>
</template>
<script>
export default{
    name:"payment",
    async mounted(){
        this.$vuetify.theme.dark=false
        this.email = await this.$storage.getUniversal('user_email')
    },
    data:()=>({
        email :"",
    }),
    methods:{
        async pay(){
            let url="http://127.0.0.1:8000/userwallet"
            let res = await this.$axios.post(url,{email:this.email });
            if(res.data == true){
                this.$router.push("/userprofile");
            }
            
        },
        async decline(){
            this.$router.push("/hrpage");
        }
    }

}
</script>
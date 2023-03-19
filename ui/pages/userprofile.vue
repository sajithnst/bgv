<template>
    <v-app userprofile>
        <v-app-bar app  color="indigo darken-4">
            <v-app-bar-title style="color: ghostwhite;">User Profile</v-app-bar-title>
            <v-spacer></v-spacer>
            <v-btn text style="color: ghostwhite;" @click="logout()">Close</v-btn>
        </v-app-bar>
        <v-main>
            <v-container>
                <userbanner/>
                <v-divider class="border-opacity-100" inset color="blue"></v-divider>
                <personaldetails/>
                <v-divider class="border-opacity-100" inset color="blue"></v-divider>
                <sslcview/>
                <v-divider class="border-opacity-100" inset color="blue"></v-divider>
                <hseview/>
                <v-divider class="border-opacity-100" inset color="blue"></v-divider>
                <ugview/>
                <v-divider class="border-opacity-100" inset color="blue"></v-divider>
                <expview/>
            </v-container>
        </v-main>
    </v-app>
</template>
<script>
export default{
    name: 'userprofile',
    async mounted (){
        this.$vuetify.theme.dark =false;
        this.email = this.$storage.getUniversal('user_email')
        let url = "http://127.0.0.1:8000/user"
        let res = await this.$axios.get(url,{params:{ email :this.email}});
        this.name=res.data.name
    },
    data: () =>({
        name : "Sajith Surendran",
        email:"",
    }),
   methods: {
    async logout (){
        if (this.$storage.getUniversal('hrlogin') == 1){
            this.$router.push("/hrpage");
        }
        else{
            this.$router.push("/notary");
        }

    }
   }
}
</script>
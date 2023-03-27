<template>
    <v-app userprofile>
        <v-app-bar app  color="indigo darken-4">
            <v-app-bar-title style="color: ghostwhite;">User Profile</v-app-bar-title>
            <v-spacer></v-spacer>
            <v-btn text style="color: ghostwhite;" @click="logout()">Close</v-btn>
        </v-app-bar>
        <v-main>
            <Nuxt/>
        </v-main>
        <v-footer dark padless>
        <v-card class="flex" flat tile>
            <v-card-subtitle class="indigo darken-1">
            Copyright @ Securekloud Technologies Ltd {{ new Date().getFullYear() }}<br/> Author - Sajith Surendran
            </v-card-subtitle>
        </v-card>
  </v-footer>
    </v-app>
</template>
<script>
export default {
    data:()=>({

    }),
    methods:{
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
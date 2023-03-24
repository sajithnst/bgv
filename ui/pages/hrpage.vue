<template>
    <v-app>
        <v-app-bar app color="indigo darken-3"> 
           <v-btn icon @click="home()" ><v-icon color="white">mdi-home</v-icon></v-btn>
           <v-spacer></v-spacer>
           <h3 class="white--text">{{ name }}</h3>
           <v-spacer></v-spacer>
           <v-btn icon @click="logout()" ><v-icon color="white">mdi-logout</v-icon></v-btn>
        </v-app-bar>
        <v-main>
            <approvedprofile/>
            <hrrequested/>
            <hrapproved/>
        </v-main>
    </v-app>
</template>
<script>
import Hrapproved from '../components/hrapproved.vue';

export default{
    name: "hrpage",
    async mounted() {
        this.$vuetify.theme.dark = false;
        this.company_mail = await this.$storage.getUniversal("hrmail");
        let url = "http://127.0.0.1:8000/hrprofile";
        let hr = {
            "company_mail": this.company_mail,
        };
        let result = await this.$axios.post(url, hr);
        this.name = result.data.name;
    },
    data: () => ({
        company_mail: "",
        name: "",
    }),
    methods: {
        async home() {
            this.$router.push("/");
        },
        async logout() {
            this.$router.push("/hrsignin");
        },
    },
    components: { Hrapproved }
}
</script>
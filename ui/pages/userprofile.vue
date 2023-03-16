<template>
    <v-app userprofile>
        <v-app-bar app  color="indigo darken-4">
            <v-app-bar-title style="color: ghostwhite;">{{ name }}</v-app-bar-title>
            <v-spacer></v-spacer>
            <v-app-bar-subtitle style="color: ghostwhite;">Close</v-app-bar-subtitle>
        </v-app-bar>
        <v-main>
            <personaldetails/>
            <education/>
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
}
</script>
<template>

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

</template>
<script>
export default{
    name: 'profile',
    layout:'profile',
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

   }
}
</script>

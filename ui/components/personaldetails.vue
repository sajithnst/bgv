<template>
        <v-container style="width: 50%; ">
            <h1 class="text-h6">Personal Details</h1>
            <h3 class="text-subtitle-1"> Aadhaar Number : {{ pdata.aadhaar }} </h3>
            <h3 class="text-subtitle-1"> Mobile number : {{ pdata.mob }}</h3>
            <h3 class="text-subtitle-1"> PAN Number : {{ pdata.pan }}</h3>
            <h3 class="text-subtitle-1"> Company Name : {{ pdata.company_name }}</h3>
            <h3 class="text-subtitle-1"> Designation : {{ pdata.designation }}</h3>
            <h3 class="text-subtitle-1"> Status : {{ pdata.status }}</h3>
        </v-container>
</template>

<script>
export default{
    name: 'userprofile',
    async mounted (){
        this.$vuetify.theme.dark =false;
        this.email = this.$storage.getUniversal('user_email')
        let url = "http://127.0.0.1:8000/user"
        let res = await this.$axios.get(url,{params:{ email :this.email}});
        this.pdata=res.data
        console.log(this.pdata)

    },
    data: () =>({
        email:"",
        pdata :{},
    }),
}
</script>
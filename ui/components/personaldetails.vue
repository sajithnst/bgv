<template>
         <v-container style="width: 70%;">
                <v-card>
                    <v-card-title>Personal Details</v-card-title>
                    <v-card-subtitle>Name:{{ pdata.name }}</v-card-subtitle>
                    <v-card-text>
                        Email : {{ pdata.email }}<br/>
                        Aadhaar : {{ pdata.aadhaar }}<br/>
                        PAN :{{ pdata.pan }}<br/>
                        Mobile:{{ pdata.mob }}<br/>
                        Status : {{ pdata.status }}
                    </v-card-text>
                </v-card>
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

    },
    data: () =>({
        email:"",
        pdata :{},
    }),
}
</script>
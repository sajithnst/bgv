<template>
    <v-container style="width: 70%;">
                <v-card>
                    <v-card-title>Eductional Details</v-card-title>
                    <v-card-text>
                       {{ this.education }}
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
        let eurl = "http://127.0.0.1:8000/usereducation"
        let eres = await this.$axios.get(eurl,{params:{email: this.email}})
        this.education= eres.data

    },
    data: () =>({
        email:"",
        education:{},


    }),
}
</script>
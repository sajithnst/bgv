<template>
    <v-container style="width: 50%; ">
            <h1 class="text-h6">UG Details</h1>
            <h3 class="text-subtitle-1"> Register Number :{{ data.regno}}</h3>
            <h3 class="text-subtitle-1"> Marks : {{ data.marks }}</h3>
            <h3 class="text-subtitle-1"> Specialization : {{ data.specialization }}</h3>
            <h3 class="text-subtitle-1"> College : {{ data.college }} </h3>
            <h3 class="text-subtitle-1"> University : {{ data.university }}</h3>
            <h3 class="text-subtitle-1"> Year of Completion : {{ data.passout }}</h3>
            <h3 class="text-subtitle-1"> Status : {{ data.status }}</h3>
        </v-container>
</template>
<script>
export default{
    name: 'hse',
    async mounted (){
        this.$vuetify.theme.dark =false;
        this.email = this.$storage.getUniversal('user_email')
        let url = "http://127.0.0.1:8000/ug"
        let res = await this.$axios.get(url,{params:{email: this.email}})
        this.data= res.data

    },
    data: () =>({
        email:"",
        data:{},


    }),
}
</script>
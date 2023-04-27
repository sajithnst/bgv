<template>
  <v-container style="width: 80%;">
         <h1 class="text-h6"> Work Experience</h1>
         <v-container v-for="data in data_set" :key="data.empid">
         <h3 class="text-h8">{{ data.company }}</h3>
         <h3 class="text-subtitle-1"> Employee ID :{{ data.empid}}</h3>
         <h3 class="text-subtitle-1"> Designation : {{ data.designation }}</h3>
         <h3 class="text-subtitle-1"> Start Date : {{ data.start_date }} </h3>
         <h3 class="text-subtitle-1"> End Date : {{ data.end_date }}</h3>
         <h3 class="text-subtitle-1"> CTC : {{ data.lpa }}</h3>
         <h3 class="text-subtitle-1"> Status : {{ data.status }}</h3>
         </v-container>
     </v-container>
</template>
<script>
export default{
 name: 'expview',
 async mounted (){
     this.$vuetify.theme.dark =false;
     this.email = this.$storage.getUniversal('login_mail')
     let url = "http://127.0.0.1:8000/exp"
     let res = await this.$axios.get(url,{params : {email : this.email}})
     this.data_set=res.data

 },
 data: () =>({
     email:"",
     data_set:[],


 }),
}
</script>

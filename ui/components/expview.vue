<template>
     <v-container style="width: 100%; " >
      <v-card>
        <v-card-title>Work Experience</v-card-title>
        <v-card-content>
          <v-container>
            <v-row>
              <v-col style="padding-left: 4%;">
                           <v-container v-if="data_s"  v-for="data in datas" :key="data.empid">
            <h3 class="text-h8">{{ data.company }}</h3>
            <h3 class="text-subtitle-1"> Employee ID :{{ data.empid}}</h3>
            <h3 class="text-subtitle-1"> Designation : {{ data.designation }}</h3>
            <h3 class="text-subtitle-1"> Start Date : {{ data.start_date }} </h3>
            <h3 class="text-subtitle-1"> End Date : {{ data.end_date }}</h3>
            <h3 class="text-subtitle-1"> CTC : {{ data.lpa }}</h3>
            <h3 class="text-subtitle-1"> Status : {{ data.status }}</h3>
                  </v-container>

              </v-col>
              <v-col >
                <v-container v-if="pending" class="text-center">
                  <v-icon size="100px" color="yellow">mdi-timer</v-icon>
                </v-container>
                <v-container v-if="verified" class="text-center">
                  <v-icon size="100px" color="green">mdi-check-decagram</v-icon>
                </v-container>


              </v-col>
              <v-container v-if="data_" class="text-center">
                <v-icon size="100px" color="red">mdi-briefcase-remove</v-icon>
                <h3 class="text-h8">No Data Found</h3>
              </v-container>


            </v-row>


          </v-container>
        </v-card-content>

  <br/>

      </v-card>


            </v-container>

</template>
<script>
export default{
    name: 'expview',
    async mounted (){
        this.$vuetify.theme.dark =false;
        this.email = this.$storage.getUniversal('user_email')
        let url = "http://127.0.0.1:8000/exp"
        let res = await this.$axios.get(url,{params : {email : this.email}})
        this.datas=res.data

    },
    data: () =>({
        email:"",
        datas:[],
        data_ : false,
        data_s : false,


    }),
    async mounted(){
  if(this.datas == 0){
      this.data_ = true
      this.data_s = false
     }
     if(this.datas == 1){
      this.data_s = true
      this.data_ = false
     }
 }
}
</script>
